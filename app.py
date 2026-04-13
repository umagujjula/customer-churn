import flask
from flask import Flask,render_template,request
import pickle
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import sklearn

with open('customer-churn.pkl','rb') as f:
    model = pickle.load(f)

# Load scaler
with open('standard_scalar.pkl','rb') as f:
    scaler = pickle.load(f)

app = Flask(__name__)

@app.route('/')

def fun():
    return render_template("index.html")

@app.route("/predict",methods=['GET','POST'])
def fun3():
    a = [pd.to_numeric(i) for i in request.form.values()]
    b = [np.array(a)]
    outcome = model.predict(b)[0]
    return render_template('index.html',Customer_Churn_Prediction_value=outcome)


if __name__ == '__main__':
    app.run(debug = True)

