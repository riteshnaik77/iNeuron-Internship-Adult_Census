from flask import Flask, render_template, request, session, redirect
# from flask_sqlalchemy import SQLAlchemy
import numpy as np
import json
import os
import math
from datetime import datetime
import markdown
import warnings
import pickle
import pandas as pd
import sklearn


warnings.filterwarnings("ignore")


app = Flask(__name__)


#For income prediction page
@app.route("/")
def income():
    return render_template("income_index.html")


# prediction function for income
def ValuePredictor_income(to_predict_list):
    print("Testing This",to_predict_list)
    to_predict = np.array(to_predict_list).reshape(1, 12)
    loaded_model = pickle.load(open("income_model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]



@app.route('/income_result', methods=['POST'])
def income_result():
    if request.method == 'POST':

        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        print(to_predict_list)
        to_predict_list = list(map(float, to_predict_list))
        print(to_predict_list)

        result = ValuePredictor_income(to_predict_list)

        if int(result) == 1:
            prediction = 'Income is more than 50K'

        else:
            prediction = 'Income is less than 50K'

        return render_template("income_result.html", prediction=prediction)



if __name__ == "__main__":
        app.run(debug=True)