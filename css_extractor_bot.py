import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import re
import argparse

# A common User-Agent to make requests appear more like a browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def make_request(url, stream=False):
    """Helper function to make an HTTP GET request with error handling."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10, stream=stream)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response
    except requests.exceptions.ConnectionError as e:
        print(f"[ERROR] Connection error for {url}: {e}")
    except requests.exceptions.Timeout as e:
        print(f"[ERROR] Timeout error for {url}: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"[ERROR] HTTP error for {url}: {e.response.status_code} - {e.response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] An unexpected request error occurred for {url}: {e}")
    return None

def get_absolute_url(base_url, relative_url):
    """Converts a relative URL to an absolute URL."""
    return urljoin(base_url, relative_url)

def fetch_css_content(css_url, visited_urls, base_page_url):
    """
    Fetches CSS content from a URL, handles @import rules recursively,
    and prevents infinite loops.
    """
    if css_url in visited_urls:
        print(f"    [INFO] Skipping already visited CSS: {css_url}")
        return ""

    visited_urls.add(css_url)
    css_text = ""
    response = make_request(css_url)
    if response:
        css_text = response.text
        print(f"    [SUCCESS] Fetched CSS from: {css_url}")

        # Find and recursively fetch @import rules
        # Regex to find @import url(...) or @import "...";
        # It handles single/double quotes and url() function.
        import_pattern = re.compile(r'@import\s+(?:url\()?[\'\"]?([^\'\"\)]+)[\'\"]?\)?(?:\s*[^;]*);?')
        
        # Use a list to store new imports to avoid modifying the string while iterating
        new_imports_content = []
        
        # Find all matches first, then iterate to avoid issues with string modification
        matches = list(import_pattern.finditer(css_text))
        
        for match in matches:
            imported_path = match.group(1).strip()
            if imported_path:
                imported_url = get_absolute_url(css_url, imported_path)
                print(f"      [INFO] Found @import: {imported_url}")
                imported_css = fetch_css_content(imported_url, visited_urls, base_page_url)
                if imported_css:
                    new_imports_content.append(f"/* Imported from {imported_url} */\n{imported_css}\n/* End import from {imported_url} */")
                
                # Replace the @import rule with an empty string or a comment to avoid re-processing
                # This is a simple replacement; for more robust handling, one might parse CSS properly
                css_text = css_text.replace(match.group(0), f"/* Removed @import {imported_path} */")

        if new_imports_content:
            # Prepend imported CSS to the current CSS content
            css_text = "\n".join(new_imports_content) + "\n" + css_text

    return css_text

def extract_css(url):
    """
    Extracts CSS from a given URL and returns it as a string.
    Focuses on linked stylesheets, inline <style> tags, and recursively handles @import rules.
    Does NOT handle JavaScript-generated styles or reliably bypass advanced anti-bot measures.
    """
    visited_urls = set() # To prevent infinite loops with @import

    # Basic URL validation
    if not url.startswith(('http://', 'https://')):
        return f"[ERROR] Invalid URL format: {url}. URL must start with http:// or https://", None

    print(f"[INFO] Starting CSS extraction for: {url}")
    response = make_request(url)
    if not response:
        return f"[ERROR] Could not fetch HTML from {url}. Aborting.", None

    soup = BeautifulSoup(response.text, 'html.parser')
    all_css_content = []

    # 1. Extract CSS from <link rel=\"stylesheet\"> tags
    print("[INFO] Extracting linked stylesheets...")
    for link_tag in soup.find_all('link', rel='stylesheet'):
        href = link_tag.get('href')
        if href:
            css_url = get_absolute_url(url, href)
            css_from_link = fetch_css_content(css_url, visited_urls, url)
            if css_from_link:
                all_css_content.append(css_from_link)

    # 2. Extract CSS from <style> tags
    print("[INFO] Extracting inline <style> blocks...")
    for style_tag in soup.find_all('style'):
        if style_tag.string:
            all_css_content.append(style_tag.string)

    if not all_css_content:
        return "[WARNING] No CSS content found or extracted.", None

    # Combine
    combined_css = "\n\n/* --- Extracted CSS --- */\n\n" + "\n\n".join(all_css_content)
    return None, combined_css

def main():
    parser = argparse.ArgumentParser(description='Extract CSS from a website.')
    parser.add_argument('--url', required=True, help='The URL of the website to extract CSS from.')
    parser.add_argument('--output', default='extracted_styles.css', help='The desired output filename (e.g., styles.css).')

    args = parser.parse_args()

    target_url = args.url
    output_file = args.output

    if not output_file.endswith('.css'):
        output_file += '.css'

    error, css_content = extract_css(target_url)
    if error:
        print(error)
        return

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(css_content)
        print(f"[SUCCESS] Successfully extracted CSS to {output_file}")
    except IOError as e:
        print(f"[ERROR] Error writing to file {output_file}: {e}")

if __name__ == "__main__":
    main()
