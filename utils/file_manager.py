import os #library of operating system 
from werkzeug.utils import secure_filename

UPLOAD_FOLDERS = 'uploads'


def save_files(folder,file):#save the files and give the secure names like removing the gap with_
    filename = secure_filename(file.filename)
    path = os.path.join(folder,filename)
    file.save(path)
    return filename


def upload_files(folder):#for uploading the files and giving the range of 20mb to save the file
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


def delete_files(filename,folder):#for deleting the files which are already saved
    path = os.path.join(folder,filename)
    if os.path.exists(path):#if the file exist then it can be deleted and if not it will also not show because it does not exist
        os.remove(path)
    
