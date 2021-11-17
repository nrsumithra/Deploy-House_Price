from flask import Flask,render_template, request, jsonify
import pickle
import json
import numpy as np
import pandas as pd

app=Flask(__name__)

filename= 'house price.sav'
with open(filename,'rb') as f:
    model=pickle.load(f)
with open('columns.json','r') as cols:
    column=json.load(cols) 
  

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    BHK = request.form.get('BHK')   
    Bath = request.form.get('Bath') 
    final_sqft = request.form.get('Sqft') 
    location = request.form.get('Location') 

    locate=list(column.values())[0].index(location.lower())  #get the index value of the location in search  
    x=np.zeros(len(list(column.values())[0])) #To replicate'X',fill row values with '0'.Later it can b changed
    x[0]=BHK
    x[1]=Bath
    x[2]=final_sqft
    x[locate]=1
    x_log=np.log10(x+1)
    pred=model.predict([x_log])
    price=round(10**pred[0], 2)

    #print(BHK, Bath, final_sqft, location)
    return render_template('form.html', prediction_text='Price of the house is $ {}'.format(price))

if __name__ == "__main__":
    app.run(debug=True)