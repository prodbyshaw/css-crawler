# Website CSS Extractor Bot

This tool helps you grab all the styling (CSS) from any website and save it into a single `.css` file on your computer. It's great for understanding how a website looks, getting design ideas, or checking its styles.

**What this tool can do:**

*   **Collects Stylesheets:** Gathers CSS from links like `<link rel="stylesheet">` on a webpage.
*   **Pulls Inline Styles:** Includes CSS written directly within `<style>` tags inside the webpage's code.
*   **Follows `@import` rules:** If a CSS file tells it to look for more CSS files using `@import`, it will go and get those too!
*   **Acts like a Browser:** It sends a common "User-Agent" message so websites think it's a regular web browser visiting.
*   **Easy to Use:** You tell it which website to check and what to name the output file using simple commands.
*   **Handles Errors:** It tries its best to tell you if something goes wrong (like a website not responding or a bad web address).

**Important Things to Know (Limitations):**

*   **Not for Super Protected Sites:** This tool works best on websites that don't have strong anti-robot defenses. If a site uses advanced security, CAPTCHAs, or complex JavaScript to hide content, this tool might not work.
*   **Doesn't See JavaScript Styles:** If a website uses JavaScript to create or change styles *after* the page loads, this tool won't be able to capture those. It only sees what's there when the page first loads.
*   **Ignores `style="..."` attributes:** It won't collect styles that are written directly inside HTML tags like `<div style="color: red;">`. These are usually very specific to one part of the page and hard to combine meaningfully.

---

## Quick Start Guide (For Everyone!)

Follow these steps to get the CSS Extractor Bot running on your computer.

### Step 1: Get Python Ready

This tool needs Python to run. If you don't have it, don't worry, it's easy to install!

1.  **Download Python:** Go to the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2.  **Install Python:**
    *   **Windows:** Download the "Windows installer" and run it. **IMPORTANT:** Make sure to check the box that says "Add Python X.X to PATH" during installation. This makes it much easier to use Python from your command prompt.
    *   **macOS:** Download the "macOS installer" and run it. Follow the instructions.
    *   **Linux:** Python is usually pre-installed. If not, use your distribution's package manager (e.g., `sudo apt install python3` for Ubuntu/Debian).

    After installing, open a new **Command Prompt** (Windows) or **Terminal** (macOS/Linux) and type:
    ```bash
    python --version
    ```
    You should see something like `Python 3.9.0` or similar. If you see an error, try restarting your computer or searching online for "add python to path" for your operating system.

### Step 2: Get the Tool's Ingredients (Libraries)

The bot needs a couple of extra "ingredients" to work. We'll use something called `pip` (which comes with Python) to get them.

1.  Open your **Command Prompt** (Windows) or **Terminal** (macOS/Linux).
2.  Type the following command and press Enter:
    ```bash
    pip install requests beautifulsoup4
    ```
    You'll see some text scrolling by. Once it stops, it means the ingredients are ready!

### Step 3: Save the Bot

You should have a file named `css_extractor_bot.py` in the same folder as this `README.txt` file. If you don't, make sure you've saved the Python code provided to you into a file with that exact name.

### Step 4: Run the Bot!

Now for the fun part! We'll tell the bot which website to extract CSS from.

1.  **Open Command Prompt/Terminal:** Make sure you are in the same folder where `css_extractor_bot.py` is located.
    *   **Tip for Windows:** Open the folder where `css_extractor_bot.py` is. In the address bar at the top, type `cmd` and press Enter. This will open a Command Prompt directly in that folder.
    *   **Tip for macOS/Linux:** Open Terminal. Type `cd ` (note the space after `cd`) then drag and drop the folder containing `css_extractor_bot.py` into the Terminal window and press Enter.

2.  **Run the Command:** Now, type the following command. You'll need to change two things:
    *   `<website_address>`: Replace this with the full web address of the site you want to check (e.g., `https://www.google.com`). **Always start with `http://` or `https://`!**
    *   `<your_output_filename>`: Replace this with a name you want for the CSS file that will be created (e.g., `my_website_styles`). You don't need to add `.css` at the end; the bot will do that for you.

    ```bash
    python css_extractor_bot.py --url <website_address> --output <your_output_filename>
    ```

    **Example:** Let's say you want to extract CSS from `https://www.w3schools.com/css/default.asp` and save it as `w3schools_styles.css`. You would type:
    ```bash
    python css_extractor_bot.py --url https://www.w3schools.com/css/default.asp --output w3schools_styles
    ```

3.  **Watch it Work:** The bot will start printing messages in your Command Prompt/Terminal, telling you what it's doing.

4.  **Find Your CSS File:** Once it's done, you'll see a message like `[SUCCESS] Successfully extracted CSS to w3schools_styles.css`. A new file with the name you chose (e.g., `w3schools_styles.css`) will appear in the same folder where `css_extractor_bot.py` is. You can open this file with any text editor (like Notepad, VS Code, Sublime Text, etc.) to see all the extracted CSS!

---

## Troubleshooting / Common Questions

*   **"Python is not recognized as an internal or external command" (Windows):** This means Python wasn't added to your system's PATH. Go back to Step 1 and make sure you checked the "Add Python X.X to PATH" box during installation. If you already installed it without checking, you might need to reinstall or manually add it to PATH (search online for instructions).
*   **"No module named 'requests'" or "No module named 'bs4'":** This means you missed Step 2. Go back and run `pip install requests beautifulsoup4`.
*   **"Invalid URL format":** Make sure your website address starts with `http://` or `https://`.
*   **"Could not fetch HTML from..." or "Connection error":** The website might be down, your internet connection might be off, or the website might be blocking the bot. Try a different website or check your internet.
*   **"No CSS content found or extracted":** This can happen if the website doesn't have much CSS, or if its CSS is heavily generated by JavaScript (which this tool can't see).
*   **The output CSS file is empty or very small:** See the "Important Things to Know (Limitations)" section above. The website might be using advanced techniques that this bot can't handle.

If you have any other issues, try searching online for the error message you see, or consult someone familiar with Python.
