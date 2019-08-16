from flask import Flask, request
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    the_file = request.files['file']
    the_file.save("./" + the_file.filename)
    print (request.form['other_data'])    # 999
    return ""


if __name__ == '__main__':
    app.run(port=5001)