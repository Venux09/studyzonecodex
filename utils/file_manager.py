import os #library of operating system 
from werkzeug.utils import secure_filename

UPLOAD_FOLDERS = 'uploads'


def save_files(file,folder):
    filename = secure_filename(file.filename)
    path = os.path.join(folder,filename)
    file.save(path)
    return filename


def upload_files(folder):
    if not os.path.exists(folder):

        return[]
    files = []
    for f in os.listdir(folder):
        if f.endswith(".pdf"):
            path = os.path.join(folder, f)
            size = os.path.getsize(path)  # size in bytes
            files.append({
                "name": f,
                "size": f"{round(size / 1024 / 1024, 1)} MB"
            })
    return files


def delete_files(filename,folder):
    path = os.path.join(folder,filename)
    if os.path.exists(path):
        os.remove(path)
    
