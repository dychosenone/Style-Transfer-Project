#.\env\Scripts\activate.bat

import os

from asyncio.windows_events import NULL
from flask import Flask
from flask import Flask, render_template, flash, request, redirect, url_for, json
from werkzeug.utils import secure_filename
from flask import request
from flask import send_file

from model.cnn_model import Model

import uuid

import time
import threading

UPLOAD_FOLDER = './uploads/'
RESULT_FOLDER = './results/'
ALLOWED_EXTENSIONS = {'jpg', 'png'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
app.secret_key = "secret key"
style_img = None
content_img = None

def runModel(filename, contentFileName, styleFileName):
    model = Model()
    output = model(contentFileName, styleFileName, filename)

@app.route('/')
def index():
    return render_template('p1.html')

@app.route('/inputpage/')
def inputpage():
    return render_template('p2.html')

@app.route('/loadingpage/')
def loadingpage():
    return render_template('p3.html')

@app.route('/resultpage/')
def resultpage():
    return render_template('p4.html')

@app.route('/uploadcontent', methods = ['GET', 'POST'])
def uploadContent():
    if 'file' not in request.files:
        print('No file part')
        return redirect(request.url)
    contentfile = request.files['file']
    if contentfile.filename == '':
        print('No image selected for uploading')
        return redirect(request.url)
    if contentfile and allowed_file(contentfile.filename):
        content_img = contentfile
        print(content_img)
        filename = secure_filename(contentfile.filename)
        contentfile.save(CONTENT_UPLOAD_FOLDER + filename)
        print('Image successfully uploaded and displayed below')
        return ('', 204)
    else:
        print('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)

@app.route('/uploadstyle', methods = ['GET', 'POST'])
def uploadStyle():
    if 'file' not in request.files:
        print('No file part')
        return redirect(request.url)
    stylefile = request.files['file']
    style_img = request.files.get('file', '')
    if stylefile.filename == '':
        print('No image selected for uploading')
        return redirect(request.url)
    if stylefile and allowed_file(stylefile.filename):
        print(style_img)
        filename = secure_filename(stylefile.filename)
        stylefile.save(STYLE_UPLOAD_FOLDER + filename)
        print('Image successfully uploaded and displayed below')
        return ('', 204)
    else:
        print('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)

@app.route('/processImage', methods=["POST"])
def processImage():
    
    
    if request.method == "POST":

        contentFile = request.files['content']
        styleFile = request.files['style']

        if contentFile and allowed_file(contentFile.filename):
            contentFileName = secure_filename(contentFile.filename)
            contentFile.save(os.path.join(app.config['UPLOAD_FOLDER'], contentFileName))


        if styleFile and allowed_file(styleFile.filename):
            styleFileName = secure_filename(styleFile.filename)
            styleFile.save(os.path.join(app.config['UPLOAD_FOLDER'], styleFileName))

        outputFileName = str(uuid.uuid4())

        thread = threading.Thread(target=runModel, args=(outputFileName, contentFileName, styleFileName))
        thread.daemon = True
        thread.start()

        return outputFileName

    pass

@app.route('/getImage', methods=["GET"])
def getImage():

    filename = request.form['filename']
    print(filename)
    return send_file(os.path.join(RESULT_FOLDER+ filename + '.png'))


if __name__ == "__main__":
    app.run(debug=True)
