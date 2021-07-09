# import basics
import os

# import stuff for our web server
from flask import Flask, flash, request, redirect, url_for, render_template
from flask import send_from_directory
from flask import jsonify
from utils import get_base_url, allowed_file, and_syntax

# setup the webservver
port = 12345
base_url = get_base_url(port)
# if dev locally
# base_url = '/00817c4c-2234-4da4-8978-4e3c95b77bdd/port/12345/'
app = Flask(__name__)


@app.route(base_url)
def index():
    return 'Index Page'

@app.route(base_url+'/hello')
def hello():
    return 'Hello, World'


if __name__ == "__main__":
    # change the code.ai-camp.org to the site where you are editing this file.
    print("Try to open\n\n    https://cocalc1.ai-camp.org" + base_url + '\n\n')
#     with app.test_request_context():
#         print(url_for('hello'))
    # Try to open: https://cocalc1.ai-camp.org/00817c4c-2234-4da4-8978-4e3c95b77bdd/port/12345/
    # remove debug=True when deploying it
    app.run(host = '0.0.0.0', port=port, debug=True)
    import sys; sys.exit(0)