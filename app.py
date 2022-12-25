from flask import Flask,render_template,request
import pickle
import numpy as np

model=pickle.load(open('model.pkl','rb'))
cv = pickle.load(open('vector.pkl' , 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')