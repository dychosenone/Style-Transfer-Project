import os

from flask import Flask
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

def runModel(filename, contentFileName, styleFileName):
    model = Model()
    output = model(contentFileName, styleFileName, filename)


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