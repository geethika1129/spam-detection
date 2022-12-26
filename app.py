from flask import Flask,render_template,request
import pickle
import numpy as np

model=pickle.load(open('model.pkl','rb'))
cv = pickle.load(open('vector.pkl' , 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/predict',method=['POST'])
def predict():
    message=request.form['text']
    data=[message]
    data=cv.transform(data).toarray()
    pred=model.predict(data)
    return render_template('result.html',prediction=pred)

if __name__=='__main__':
    app.run(debug=True)