import pickle
import json
import numpy as np
from os import path

workclass_values = None
education_values = None
occupation_values = None
marital_status_values = None
relationship_values = None
race_values = None
gender_values = None
native_country_values = None
model = None

def load_saved_attributes():

    global workclass_values
    global education_values
    global education_dict
    global occupation_values
    global marital_status_values
    global relationship_values
    global race_values
    global gender_values
    global native_country_values
    global model

    with open("columns.json", "r") as f:
        resp = json.load(f)
        workclass_values = resp["workclass"]
        education_dict = resp["education"]
        education_values = list(education_dict.keys())
        occupation_values = resp["occupation"]
        marital_status_values = resp["marital_status"]
        relationship_values = resp["relationship"]
        race_values = resp["race"]
        gender_values = resp["gender"]
        native_country_values = resp["native_country"]

    model = pickle.load(open("donors.pickle", "rb"))

def get_workclass_names():
    return workclass_values

def get_education_names():
    return education_values

def get_occupation_names():
    return occupation_values

def get_marital_status_names():
    return marital_status_values

def get_relationship_names():
    return relationship_values

def get_race_names():
    return race_values

def get_native_country_names():
    return native_country_values

def get_gender_names():
    return gender_values

def predict_donor(age, capital_gain, capital_loss, hours_per_week, workclass, education, occupation, marital_status, relationship, race, gender, native_country ):
    try:
        workclass_index = workclass_values.index(workclass)
        occupation_index = occupation_values.index(occupation)
        marital_status_index = marital_status_values.index(marital_status)
        relationship_index = relationship_values.index(relationship)
        race_index = race_values.index(race)
        gender_index = gender_values.index(gender)
        native_country_index = native_country_values.index(native_country)

    except:
        workclass_index = -1
        occupation_index = -1
        marital_status_index = -1
        relationship_index = -1
        race_index = -1
        gender_index = -1
        native_country_index = -1

    workclass_array = np.zeros(len(workclass_values))
    if workclass_index >= 0:
        workclass_array[workclass_index] = 1

    education_label = education_dict[education]

    occupation_array = np.zeros(len(occupation_values))
    if occupation_index >= 0:
        occupation_array[occupation_index] = 1

    marital_status_array = np.zeros(len(marital_status_values))
    if marital_status_index >= 0:
        marital_status_array[marital_status_index] = 1

    relationship_array = np.zeros(len(relationship_values))
    if relationship_index >= 0:
        relationship_array[relationship_index] = 1

    race_array = np.zeros(len(race_values))
    if race_index >= 0:
        race_array[race_index] = 1

    gender_array = np.zeros(len(gender_values))
    if gender_index >= 0:
        gender_array[gender_index] = 1

    native_country_array = np.zeros(len(native_country_values))
    if native_country_index >= 0:
        native_country_array[native_country_index] = 1

    race_array = race_array[:-1]
    gender_array = gender_array[:-1]
    native_country_array = native_country_array[:-1]


    sample = np.concatenate((np.array([age, capital_gain, capital_loss, hours_per_week]), workclass_array, np.array([education_label]), occupation_array, marital_status_array, relationship_array, race_array, gender_array, native_country_array))
    sample = np.asarray(sample, dtype='float64')
    return model.predict(sample.reshape(1,-1))[0]


if __name__ == '__main__':
    load_saved_attributes()
else:
    load_saved_attributes()
