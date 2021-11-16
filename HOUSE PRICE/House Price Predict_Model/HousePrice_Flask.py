from flask import Flask,render_template, request

app=Flask(__name__)

@app.route('/')
def houseprice():
    return render_template('form.html')
@app.route('/predict',methods=['POST'])
def predict():
    BHK = request.form.get('BHK')   
    Bath = request.form.get('Bath') 
    final_sqft = request.form.get('Sqft') 
    location = request.form.get('Location') 

    print(BHK, Bath, final_sqft, location)
    return 'Form is submitted'

app.run(debug=True)