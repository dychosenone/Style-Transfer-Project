#.\env\Scripts\activate.bat

from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

CONTENT_UPLOAD_FOLDER = 'content'
STYLE_UPLOAD_FOLDER = 'style'

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

@app.route('/upload', methods = ['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
      f = request.files['file']
      f.save(CONTENT_UPLOAD_FOLDER + '/' + secure_filename(f.filename))
      return 'file uploaded successfully'

if __name__ == "__main__":
    app.run(debug = True)


