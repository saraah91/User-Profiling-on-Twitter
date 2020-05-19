from app import app
import json
from collections import OrderedDict
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
from flask import render_template
import functions

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'json', 'jsonl'}

def allowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def do():
    jamalTweets = functions.parseJSONTweets('jamalrayyan.jsonl')
    resultsDict = {
        "NoOfFollowers" : functions.getFollowers(jamalTweets[0]),
        "NoOfFollowing" : functions.getFollowing(jamalTweets[0]),
        "UserName" : functions.getName(jamalTweets[0]),
        "TopLanguages" : functions.getTweetsLanguages(jamalTweets)
    }
    resultsJSON = json.dumps(resultsDict)
    print(resultsJSON)
    return render_template('index.html')
'''
def uploadFile():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowedFile(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploadedFile', filename=filename))
    return render_template('index.html')
'''

    
@app.route('/uploads/<filename>')
def uploadedFile(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)