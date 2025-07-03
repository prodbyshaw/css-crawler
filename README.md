# CSS Crawler

CSS Crawler is a Python script that extracts all CSS from a website and saves it to a single file. It's a great tool for web developers and designers who want to analyze the styling of a website.

## Features

*   **Comprehensive Extraction:** Gathers CSS from `<link>` tags, `<style>` blocks, and `@import` rules.
*   **User-Agent Spoofing:** Simulates a real browser to avoid being blocked by simple anti-bot measures.
*   **Command-Line Interface:** Easy to use from the terminal.
*   **Error Handling:** Provides feedback on common issues like invalid URLs or connection problems.

## Limitations

*   **Dynamic Content:** The script does not execute JavaScript, so it won't capture styles generated dynamically.
*   **Advanced Anti-Bot:** May not work on websites with sophisticated anti-crawling technologies.
*   **Inline Styles:** Does not extract styles from `style` attributes on individual HTML elements.

## Getting Started

### Prerequisites

*   Python 3.6 or higher
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/prodbyshaw/css-crawler.git
    cd css-crawler
    ```

2.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

To use the CSS Crawler, run the following command in your terminal:

```bash
python css_extractor_bot.py --url <website_url> --output <output_filename>
```

**Example:**

```bash
python css_extractor_bot.py --url https://www.w3schools.com/css/default.asp --output w3schools_styles
```

This will extract the CSS from the given URL and save it to `w3schools_styles.css`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.