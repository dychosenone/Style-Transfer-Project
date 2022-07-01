from fileinput import filename
import os
from click import style

from flask import Flask
from flask import render_template
from werkzeug.utils import secure_filename
from flask import request

from model.cnn_model import Model

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = {'jpg', 'png'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/processImage', methods=["POST"])
def processImage():
    
    '''
    Todo: 
    - Get Image
    - Send Image to Backend for Processing
    - Return Image
    '''
    if request.method == "POST":

        contentFile = request.files['content']
        styleFile = request.files['style']

        if contentFile and allowed_file(contentFile.filename):
            contentFileName = secure_filename(contentFile.filename)
            contentFile.save(os.path.join(app.config['UPLOAD_FOLDER'], contentFileName))


        if styleFile and allowed_file(styleFile.filename):
            styleFileName = secure_filename(styleFile.filename)
            styleFile.save(os.path.join(app.config['UPLOAD_FOLDER'], styleFileName))

        model = Model()
        output = model(contentFileName, styleFileName)

        return output

    pass

if __name__ == "__main__":
    app.run(debug=True)