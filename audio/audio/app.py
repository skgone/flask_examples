from flask import Flask, render_template, request, redirect, url_for,send_from_directory
from flask_dropzone import Dropzone
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    DROPZONE_ALLOWED_FILE_TYPE='audio',
    DROPZONE_MAX_FILE_SIZE=10,
    DROPZONE_MAX_FILES=30,
)


dropzone = Dropzone(app)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('upload.html')


@app.route('/')
def hello():
    return redirect(url_for("upload"))


@app.route('/upload/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOADED_PATH'], filename=filename)


@app.route('/display')
def get_file():
    audio_names=[]
    for file in os.listdir('./uploads'):
        if file.endswith('.wav'):
            audio_names.append(file)
    print("{} files was uploaded".format(len(audio_names)))
    return render_template("display.html", audio_names=audio_names)


if __name__ == '__main__':
    app.run(port=7000, debug=True)



