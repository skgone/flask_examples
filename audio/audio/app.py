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
def display_file(filename):
    return send_from_directory(app.config['UPLOADED_PATH'], filename=filename)


if __name__ == '__main__':
    app.run(debug=True)



