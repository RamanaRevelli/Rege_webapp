from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form.get('test_string', '')
    regex_pattern = request.form.get('regex_pattern', '')

    # Perform regex matching
    matches = re.findall(regex_pattern, test_string)

    return render_template('results.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)

@app.route('/validate_email', methods=['GET', 'POST'])
def validate_email():
    if request.method == 'POST':
        email = request.form.get('email', '')
        is_valid_email = re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None

        return render_template('validate_email.html', email=email, is_valid_email=is_valid_email)

    return render_template('validate_email.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
