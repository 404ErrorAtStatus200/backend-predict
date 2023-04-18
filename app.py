from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pickle
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api = Api(app)


@app.route('/disease')
def get():

    url_params = request.args
    animalname = url_params['ani']
    symptom1 = url_params['s1']
    try:
        symptom2 = url_params['s2']
    except KeyError:
        symptom2 = ""
    try:
        symptom3 = url_params['s3']
    except KeyError:
        symptom3 = ""
    try:
        symptom4 = url_params['s4']
    except KeyError:
        symptom4 = ""
    try:
        symptom5 = url_params['d5']
    except KeyError:
        symptom5 = ""

    df = pd.DataFrame([[animalname,symptom1,symptom2,symptom3,symptom4,symptom5]],columns=['AnimalName','symptoms1','symptoms2','symptoms3','symptoms4','symptoms5'])
    pipe = pickle.load(open('animalDetech.pkl', "rb"))
    prediction = pipe.predict(df)
    print(prediction[0])
    return str(prediction[0])



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
