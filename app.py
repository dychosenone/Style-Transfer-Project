#.\env\Scripts\activate.bat

from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('p1.html')

@app.route('/inputpage')
def inputpage():
    return render_template('p2.html')

if __name__ == "__main__":
    app.run(debug = True)


