#!flask/bin/python
from flask import Flask, jsonify  ,request , render_template
from werkzeug import secure_filename

from PIL import Image
from algorithm import  test_xception as prediction

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def test_task():
    return jsonify({'res': 'ok'}), 201

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['upload']
        f_name = secure_filename(f.filename)
        f_dir  = 'images/' + f_name
        f.save(f_dir)
        img = Image.open(f_dir)
        res = prediction.predict(img)
        return jsonify({'item' : res}) , 201
    return jsonify({'info': 'not a post request'}), 201


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0',port=7001)
