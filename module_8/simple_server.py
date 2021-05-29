# in cmd write
# pip install flask

from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
import numpy as np
import pickle
from flask import Flask, request


app = Flask(__name__) # create a Flask object


# load dataset and fit
X, y = load_diabetes(return_X_y=True)
X = X[:, 0].reshape(-1, 1) # Берём только один признак
regressor = LinearRegression()
regressor.fit(X,y)


with open('my_model.pkl', 'wb') as output:
   	pickle.dump(regressor, output) # save model

with open('my_model.pkl', 'rb') as pkl_file:
    	regressor_from_file = pickle.load(pkl_file) # load model

    
def model_predict(value):
        value_to_predict = np.array([value]).reshape(-1, 1)
        return regressor_from_file.predict(value_to_predict)
    

@app.route('/predict') # Attach functions to url ../predict
def predict_func():
    try:
    	value = request.args.get('value') 
    	prediction = model_predict(float(value)) # convert to int
    	return f'The predicted value is {prediction}'
    except (ValueError): 
        return f'Please set a numeric parameter'


if __name__ == '__main__':
    	app.run('localhost', 5000) # link and port


# http://localhost:5000/predict?value=0.04
# http://localhost:5000/predict?value=abc