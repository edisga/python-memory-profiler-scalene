import numpy as np
import scipy.signal
from flask import Flask
import os
from random import random

app = Flask(__name__, static_url_path='/static')

def create_data():
    ret = []
    for n in range(50):
        ret.append(np.random.randn(1, 70, 71, 72))
    return ret

def process_data(data):
    data = np.concatenate(data)
    detrended = scipy.signal.detrend(data, axis=0)
    return detrended

def generate_data(id):
    data = []
    i=0
    for _ in range(id):
	    value = random()
	    data.append(value)
    return data


@app.route("/")
def home():
    raw_data = create_data()
    processed_data = process_data(raw_data)
    return f"Length of processed data: { len(processed_data)}"

array = []
@app.route("/memory")
def memory():
    random = 200000 * 1024
    array.append(generate_data(random))
    return f"Length of processed data: { len(array)}"

if __name__ == '__main__':
    port= os.environ.get('PORT')
    app.run(host='0.0.0.0', debug=False, port=port)