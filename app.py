#.\env\Scripts\activate.bat

from asyncio.windows_events import NULL
from flask import Flask, render_template, flash, request, redirect, url_for, json
from werkzeug.utils import secure_filename
import os
import time

app = Flask(__name__)

CONTENT_UPLOAD_FOLDER = 'content/'
STYLE_UPLOAD_FOLDER = 'style/'

app.secret_key = "secret key"

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

style_img = None
content_img = None

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

@app.route('/processimage')
def processimage():
    print('test')
    #time.sleep(10) #simulate loading time for image
    return {'status':'ok'}

if __name__ == "__main__":
    app.run(debug = True)


