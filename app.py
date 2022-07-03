#.\env\Scripts\activate.bat

from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

CONTENT_UPLOAD_FOLDER = 'content/'
STYLE_UPLOAD_FOLDER = 'style/'

app.secret_key = "secret key"

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('p1.html')

@app.route('/inputpage/')
def inputpage():
    return render_template('p2.html')

@app.route('/uploadcontent', methods = ['GET', 'POST'])
def uploadFile():
    if 'file' not in request.files:
        print('No file part')
        return redirect(request.url)
    contentfile = request.files['file']
    if contentfile.filename == '':
        print('No image selected for uploading')
        return redirect(request.url)
    if contentfile and allowed_file(contentfile.filename):
        filename = secure_filename(contentfile.filename)
        contentfile.save(CONTENT_UPLOAD_FOLDER + filename)
        print('Image successfully uploaded and displayed below')
        return render_template('p2.html')
    else:
        print('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)

if __name__ == "__main__":
    app.run(debug = True)


