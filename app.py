from flask import Flask, render_template, request, send_file
import os
import sys

# Add the directory containing css_extractor_bot.py to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from css_extractor_bot import extract_css

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
    url = request.form['url']
    error, css_content = extract_css(url)

    if error:
        return render_template('result.html', error=error)
    elif css_content:
        return render_template('result.html', css_content=css_content, url=url)
    else:
        return render_template('result.html', error="No CSS content found or extracted.")

if __name__ == '__main__':
    app.run(debug=True)