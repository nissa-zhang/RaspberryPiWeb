from flask import Flask
import subprocess
import os
from flask import send_from_directory
from flask import render_template



app = Flask(__name__)


@app.route("/")
def hello():

    p = subprocess.Popen(["/usr/bin/python", "/Users/nissa/Downloads/photo.py"], stdout=subprocess.PIPE)
    out, err = p.communicate()
    path = "photo/" + out.decode('utf-8').replace('\n', '')

    print(path)

    # return '<html><body><img src="file://{0}" /></body></html>'.format(path)
    # return '<img src="static/photo/'  + path  + '" />'
    return render_template('index.html', photo=path)


@app.route('/photo/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static', 'photo'), filename)