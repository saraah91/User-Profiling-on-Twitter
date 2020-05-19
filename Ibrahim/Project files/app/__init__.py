from flask import Flask, flash, request, redirect, url_for
import os
UPLOAD_FOLDER = 'uploadedFiles'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

from app import routes