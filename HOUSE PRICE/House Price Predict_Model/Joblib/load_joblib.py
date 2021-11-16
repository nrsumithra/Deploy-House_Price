import joblib
import json
import numpy as np
import pandas as pd
filename= 'house price.joblib'
with open(filename,'rb') as f:
    model=joblib.load(f)
with open('columns.json','r') as cols:
    column=json.load(cols)       
def predict_price(BHK, Bath, final_sqft,location):
    locate=list(column.values())[0].index(location.lower())  #get the index value of the location in search  
    x=np.zeros(len(list(column.values())[0])) #To replicate'X',fill row values with '0'.Later it can b changed
    x[0]=BHK
    x[1]=Bath
    x[2]=final_sqft
    x[locate]=1
    x_log=np.log10(x+1)
    pred=model.predict([x_log])
    price=10**pred[0]
    return price   
print(predict_price(2,2,1400,'Indira Nagar'))