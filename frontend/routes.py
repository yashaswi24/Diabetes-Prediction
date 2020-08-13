from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/Submit', methods=['POST', 'GET'])
def Submit():
    if request.method == 'POST':
        result = request.form
    pkl_file = open('cat', 'rb')
    index_dict = pickle.load(pkl_file)
    new_vector = np.zeros(len(index_dict))
    # print(new_vector)

    try:
        new_vector[index_dict['Pregnancies_' + str(result['Pregnancies'])]] = 1
    except:
        pass
    try:
        new_vector[index_dict['Glucose_' + str(result['Glucose'])]] = 1
    except:
        pass
    try:
        new_vector[index_dict['BloodPressure_' + str(result['BloodPressure'])]] = 1
    except:
        pass
    try:
        new_vector[index_dict['SkinThickness_' + str(result['SkinThickness'])]] = 1
    except:
        pass
    try:
        new_vector[index_dict['Insulin_' + str(result['Insulin'])]] = 1
    except:
        pass
    try:
        new_vector[index_dict['BMI_' + str(result['BMI'])]] = 1
    except:
        pass
    try:
        new_vector[index_dict['DiabetesPedigreeFunction_' + str(result['DiabetesPredigreeFunction'])]] = 1
    except:
        pass
    try:
        new_vector[index_dict['Age_' + str(result['Age'])]] = 1
    except:
        pass

    # print(result['Glucose'])

    pkl_file = open('finalmodel.pkl', 'rb')
    finalmodel = pickle.load(pkl_file)
    # new_vector=new_vector.reshape(-1,1)
    prediction = finalmodel.predict(result)
    # result=request.form['Glucose']
    # return render_template('result.html')
    return render_template('result.html', prediction=prediction)


if __name__ == '__main__':
    app.run()
