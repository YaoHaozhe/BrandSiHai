#!flask/bin/python
from flask import Flask, jsonify  ,request , render_template
from werkzeug import secure_filename
import sys
sys.path.append('algorithm/yolo3/')
import infer as prediction

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
        f_dir_out = 'images/' + 'output.jpg'
        f.save(f_dir)
        res = []
        names,scores = prediction.main(f_dir,f_dir_out )
        for i in range(0, len(names)):
            res.append({
                'name': names[i],
                'score': str(scores[i])
            })
        print(res)
        return jsonify({'item' : res}) , 201
    return jsonify({'info': 'not a post request'}), 201


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0',port=7001)
