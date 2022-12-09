from array import array

from flask import Flask, render_template, request
from flask import *
import pickle

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


if __name__ == '__main__':
    app.run()


#@app.post('/predict')
#def get_music_category():
@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        model = pickle.load(open('model.pkl', 'rb'))
        prediction = model.predict(f.filename)
        print(prediction)
        return render_template("Acknowledgement.html", name = f.filename)
