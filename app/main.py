#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Run by typing
#      python3 flask_app.py
# in a terminal (or just ./main.py).

## **IMPORTANT:** only collaborators on the project where you run
## this can access this web server!

"""
    Bonus points if you want to have internship at AI Camp
    1. How can we save what user built? And if we can save them, like allow them to publish, can we load the saved results back on the home page? 
    2. Can you add a button for each generated item at the frontend to just allow that item to be added to the story that the user is building? 
    3. What other features you'd like to develop to help AI write better with a user?
    4. How to speed up the model run? Quantize the model? Using a GPU to run the model?
"""


# import basics
import os

# import stuff for our web server
from flask import Flask, flash, request, redirect, url_for, render_template
from flask import send_from_directory
from flask import jsonify
from utils import get_base_url, allowed_file, and_syntax

# import stuff for our models
import torch
from aitextgen import aitextgen
# load up the model into memory
# you will need to have all your trained model into the folder trained_mode.
ai = aitextgen(model_folder="trained_model_1", to_gpu=False)



# setup the webservver
#port = 12345
#base_url = get_base_url(port)
# if dev locally
# base_url = '/00817c4c-2234-4da4-8978-4e3c95b77bdd/port/12345/'
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('writer_home.html', generated=None)

@app.route('/how_it_works')
def how_it_works():
    return render_template('How-It-Works.html', generated=None)

@app.route('/about_us')
def About_us():
    return render_template('About-Us.html', generated=None)

@app.route('/', methods=['POST'])
def home_post():
    return redirect(url_for('results'))

@app.route('/results')
def results():
    return render_template('Write-your-story-with-AI.html', generated=None)

'''
@app.route(base_url + '/generate_text', methods=["POST"])
def generate_text():
    """view function that will return json response for generated text. 
    """

    prompt = request.form['prompt']
    if prompt is not None:
        generated = ai.generate(
            n=3,
            batch_size=3,
            prompt='QUERY: ' + str(prompt),
            max_length=50,
            temperature=0.5,
            return_as_list=True
        )
    print('ai generated this:\n')
    new_generated=[]
    for string in generated:
        temp =string.split("\n#")[0].split("HUMAN:")[1]
        new_generated.append(temp)
    print(new_generated)
    data = {'generated_ls': new_generated}

    return jsonify(data)
'''
def remove_toks(s):
    s = s.split("[start]")[1]
    s = s.split("[end]")[0]
    return s

import json
import requests
@app.route('/generate_text', methods=["POST"])
def generate_text():
    prompt = str(request.form["prompt"]).lower()
    ngrok_url = "http://54e389e7f6e3.ngrok.io"
    url = ngrok_url + "/generate"
    x = requests.post(url, data={"prompt":prompt})
    res = json.loads(x.text)["generated_ls"]
    r = [remove_toks(resp) for resp in res]
    return jsonify({'generated_ls':r})




#if __name__ == "__main__":
    # change the code.ai-camp.org to the site where you are editing this file.
#    print("Try to open\n\n    https://cocalc1.ai-camp.org" + base_url + '\n\n')
    # Try to open: https://cocalc1.ai-camp.org/00817c4c-2234-4da4-8978-4e3c95b77bdd/port/12345/
    # remove debug=True when deploying it
#    app.run(host = '0.0.0.0', port=port, debug=True)
#    import sys; sys.exit(0)
