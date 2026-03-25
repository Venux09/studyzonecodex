#skeleton of the app
from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template('landing.html')#front or home page

@app.route('/upload')#upload section
def upload():
    return render_template('upload.html')


@app.route('/summary')#summary section
def summary():
    return render_template('summary.html')

@app.route('/quiz')#quiz section
def quiz():
    return render_template('quiz.html')


@app.route('/chat')#ai or problem solving section
def chat():
    return render_template('chat.html')

if __name__== '__main__':
    app.run(debug=True)#for debugging or file changing -crashout