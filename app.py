import os
import sys
from util import lets_see
# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer


# Declare a flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

def to_float(lst):
    a=[]
    lst=lst.split(',')
    for i in lst:
        if(lst!=','):
            a.append(float(i))
    return a

@app.route('/', methods=['POST'])
def predict():
    print("Gsmkdfnj")
    print(request.form)
    f=request.form.get('f')
    i=request.form.get('i')
    t=request.form.get('t')
    g=request.form.get('g')
    f=to_float(f)
    t=to_float(t)
    i=to_float(i)
    g=to_float(g)
    # print(f,g,t,i)
    ans=lets_see(g,f,i,t)
    # print(ans)
    return render_template('output.html',context={ans})
if __name__ == '__main__':
     app.run(debug = True)
    