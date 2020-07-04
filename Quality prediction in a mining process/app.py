# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:52:57 2020

@author: sarath
"""


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from joblib import load
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
# model = load('rfg.save')
# load the model
model = load(open('qualityPrediction.pkl', 'rb'))
# load the scaler
scaler = load(open('scaler.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('login.html')

database={'Test':'sb@123','Sarath':'sb@123','Mohan':'sb@123','Jithendra':'sb@123','Srinivas':'sb@123','Jayanth':'sb@123'}


@app.route('/login',methods=['POST','GET'])
def login():
    un=request.form['username']
    pwd=request.form['password']
    if un not in database:
        return render_template('login.html',info="Invalid user")
    else:
        if database[un]!=pwd:
            return render_template('login.html',info="Invalid password")
        else:
            return render_template('index.html',name=un)
        
            
    

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[float(x) for x in request.form.values()]]
    print(x_test)
    x_test=scaler.transform(x_test)
    print(x_test)
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]

    return render_template('index.html', prediction_text='Silica % {0:.3f}'.format(output))

'''@app.route('/predict_api',methods=['POST'])
def predict_api():
    #For direct API calls trought request

    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)'''

if __name__ == "__main__":
    app.run(debug=True)
