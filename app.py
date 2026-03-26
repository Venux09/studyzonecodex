#skeleton of the app
from flask import Flask ,render_template,url_for,request,jsonify,redirect
from utils.pdf_parser import extract_text
from utils.ai_helper import get_summary, get_quiz, get_chat_response
from utils.file_manager import save_files, upload_files, delete_files
import os 
from dotenv import load_dotenv


app = Flask(__name__)
app.config["UPLOADS_FOALDERS"] = 'uploads'
@app.route("/")
def landing():
    return render_template('landing.html')#front or home page

@app.route('/upload',methods = ['GET','POST'])#upload section
def upload():#section for posting and saving that file
    if request.method == 'POST':
        file = request.files.get('pdf')
        if file and file.filename.endswith('.pdf'):
            filename = save_files(file, app.config['UPLOAD_FOLDER'])
            return redirect(url_for('summary', filename=filename))
    
    files = upload_files(app.config['UPLOAD_FOLDER'])
    return render_template('upload.html', files=files)
  


@app.route('/summary/<filename>')#summary section
def summary(filename):
    path =  os.path.join(app.config['UPLOAD_FOLDER'], filename)
    text = extract_text(path)
    summary_data = get_summary(text) 
    

    return render_template('summary.html', filename=filename, summary=summary_data)

@app.route('/quiz/<filename>')#quiz section
def quiz(filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    text = extract_text(path)

    return render_template('quiz.html',filename = filename, text = text)


@app.route('/generate_quiz',methods = ['POST'])
def generate_quiz():
        data = request.json#Requesting the data from the dictionary
        questions = get_quiz(data['text'], data['type'])
        return jsonify({'questions': questions})
    

def chat(filename):
    files = upload_files(app.config['UPLOAD_FOLDER'])
    return render_template('chat.html', filename=filename, files=files)

@app.route('/chat-message', methods=['POST'])#for reply from the ai 
def chat_message():
    data = request.json
    path = os.path.join(app.config['UPLOAD_FOLDER'], data['filename'])
    text = extract_text(path)
    reply = get_chat_response(text, data['message'], data.get('history', []))
    return jsonify({'reply': reply})

@app.route('/delete/<filename>', methods=['POST'])#for deleting the files in saved section
def delete(filename):
    delete_files(filename, app.config['UPLOAD_FOLDER'])
    return redirect(url_for('upload'))

if __name__== '__main__':
    app.run(debug=True)#for debugging or file changing -crashout