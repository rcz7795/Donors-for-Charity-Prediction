from flask import Flask, request, render_template, jsonify
from flask_cors import cross_origin
import datetime as dt

import DonorPrediction as tm

app = Flask(__name__)

@app.route('/get_workclass_names', methods=['GET'])
def get_workclass_names():
    response = jsonify({
        'workclass': tm.get_workclass_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_education_names', methods=['GET'])
def get_education_names():
    response = jsonify({
        'education': tm.get_education_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_occupation_names', methods=['GET'])
def get_occupation_names():
    response = jsonify({
        'occupation': tm.get_occupation_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_marital_status_names', methods=['GET'])
def get_marital_status_names():
    response = jsonify({
        'marital_status': tm.get_marital_status_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_relationship_names', methods=['GET'])
def get_relationship_names():
    response = jsonify({
        'relationship': tm.get_relationship_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_race_names', methods=['GET'])
def get_race_names():
    response = jsonify({
        'race': tm.get_race_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_gender_names', methods=['GET'])
def get_gender_names():
    response = jsonify({
        'gender': tm.get_gender_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_native_country_names', methods=['GET'])
def get_native_country_names():
    response = jsonify({
        'native_country': tm.get_native_country_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_boolean_names', methods=['GET'])
def get_boolean_names():
    response = jsonify({
        'boolean': ["Yes", "No"]
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
# @cross_origin()
def predict():
    if request.method == "POST":
        age = request.form.get('age')
        gain = request.form.get('capital_gain')
        hours_per_week = request.form.get('hours_per_week')
        workclass = request.form.get('workclass')
        education = request.form.get('education')
        occupation = request.form.get('occupation')
        marital_status = request.form.get('marital_status')
        relationship = request.form.get('relationship')
        race = request.form.get('race')
        gender = request.form.get('gender')
        native_country = request.form.get('native_country')

        if gain == "Yes":
            capital_gain = 1
            capital_loss = 0
        else:
            capital_gain = 0
            capital_loss = 1

        prediction = tm.predict_donor(age, capital_gain, capital_loss, hours_per_week, workclass, education, occupation, marital_status, relationship, race, gender, native_country)

        if prediction == 1:
            return render_template("index.html", prediction_text="The person seems to be a potential donor")
        else:
            return render_template("index.html", prediction_text="The person doesn't seem to be a donor")

    return render_template("index.html")

if __name__ == "__main__":
    tm.load_saved_attributes()
    app.run(debug=True)