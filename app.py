import numpy as np
import scipy.signal
from flask import Flask

app = Flask(__name__)

def create_data():
    ret = []
    for n in range(50):
        ret.append(np.random.randn(1, 70, 71, 72))
    return ret

def process_data(data):
    data = np.concatenate(data)
    detrended = scipy.signal.detrend(data, axis=0)
    return detrended

@app.route("/")
def home():
    raw_data = create_data()
    processed_data = process_data(raw_data)
    return f"Length of processed data: { len(processed_data)}"

if __name__ == '__main__':
    app.run()

