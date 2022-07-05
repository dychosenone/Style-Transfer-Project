#.\env\Scripts\activate.bat

import os

from flask import Flask, render_template, flash, request, redirect, send_from_directory, url_for, json, jsonify
from werkzeug.utils import secure_filename
from flask import request
from flask import send_file

from model.cnn_model import Model

from waitress import serve

import uuid

import time
import threading

STYLE_FOLDER = './style/'
CONTENT_FOLDER = './content/'

RESULT_FOLDER = './results/'
ALLOWED_EXTENSIONS = {'jpg', 'png'}

app = Flask(__name__)
app.config['STYLE_FOLDER'] = STYLE_FOLDER
app.config['CONTENT_FOLDER'] = CONTENT_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
app.secret_key = "secret key"


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

@app.route('/resultpage/<result>', methods=["GET"])
def resultpage(result):

    # filename = request.args.get('result')
    print(result)

    check = checkImage(result + '.png')
    if check == True:
        return render_template('p4.html', result=os.path.join(result + '.png'))
    else:
        return render_template('p4.html', result=False)

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
        filename = str(uuid.uuid4())
        contentfile.save(os.path.join(CONTENT_FOLDER + filename + '.png'))
        print('Image successfully uploaded and displayed below')
        return jsonify(uuid=filename)
    else:
        print('Allowed image types are - png, jpg')
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

    
        filename = str(uuid.uuid4())
        stylefile.save(os.path.join(STYLE_FOLDER + filename + '.png'))
        print('Image successfully uploaded and displayed below')
        return jsonify(uuid=filename)

    else:
        print('Allowed image types are - png, jpg')
        return redirect(request.url)

@app.route('/processImage', methods=["POST"])
def processImage():
    
    if request.method == "POST":
        
        style = request.json['style']
        content = request.json['content']

        contentFile = os.path.join(CONTENT_FOLDER + content + '.png')
        styleFile = os.path.join(STYLE_FOLDER + style + '.png')

        outputFileName = str(uuid.uuid4())

        thread = threading.Thread(target=runModel, args=(outputFileName, contentFile, styleFile))
        thread.daemon = True
        thread.start()

        return outputFileName

    pass

def checkImage(filename):
    if(os.path.exists(RESULT_FOLDER + filename)):
        return True
    else: 
        return False

@app.route('/results/<path:filename>', methods=["GET"])
def getImage(filename):

    return send_from_directory("results", filename)



if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
