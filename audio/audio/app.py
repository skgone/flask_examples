from flask import Flask, render_template, \
    request, redirect, url_for,send_from_directory, flash,session
from flask_dropzone import Dropzone
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    DROPZONE_ALLOWED_FILE_TYPE='audio',
    DROPZONE_MAX_FILE_SIZE=10,
    DROPZONE_MAX_FILES=30,
    DROPZONE_REDIRECT_VIEW='display',
    DROPZONE_UPLOAD_ON_CLICK=True
)


dropzone = Dropzone(app)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    filenames = []
    if request.method == 'POST':
        for key, f in request.files.items():
            if key.startswith('file'):
                f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
                filenames.append(f.filename)
        flash('Uplload success.')
        session['filenames'] = filenames
    return render_template('upload.html')


@app.route('/')
def hello():
    return redirect(url_for("upload"))


@app.route('/upload/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOADED_PATH'], filename=filename)


@app.route('/display')
def display():
    # audio_names=[]
    # for file in os.listdir('./uploads'):
    #     if file.endswith('.wav'):
    #         audio_names.append(file)
    # print("{} files was uploaded".format(len(audio_names)))
    return render_template("display.html")


if __name__ == '__main__':
    app.run(port=7000, debug=True)



