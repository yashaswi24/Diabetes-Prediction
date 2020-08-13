from flask import Flask, request, render_template
import pickle

ip = open("mod", 'rb')
m = pickle.load(ip)
h = 0
w = 0
ge = ""
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def fun():
    if request.method == 'POST':
        global h
        h = float(request.form['height'])
        global w
        w = float(request.form['weight'])
        global ge
        ge = request.form['gender']
        if ge == 'male':
            return render_template('home2.html')
        else:
            return render_template('home.html')


@app.route('/Submit', methods=['POST'])
def Submit():
    if request.method == 'POST':
        print("hello")
        data = request.form
        print(data)
        if ge == 'male':
            preg = 0
        else:
            preg = int(request.form['Pregnancies'])
        print(preg)
        gluc = float(request.form['Glucose'])
        bp = float(request.form['BloodPressure'])
        st = float(request.form['SkinThickness'])
        iss = float(request.form['Insulin'])
        hi = 0.3048 * h
        bmi = w / (hi * hi)
        print(bmi)
        dpf = float(request.form['DiabetesPredigreeFunction'])
        age = int(request.form['Age'])
        k = [[preg, gluc, bp, st, iss, bmi, dpf, age]]
        pred = m.predict(k)
        print(pred)
        if pred == [0.]:
            p = "NEGATIVE"
        else:
            p = "POSITIVE"
        if iss > 150:
            per = 0.8
        elif iss > 120:
            per = 0.7
        elif iss > 100:
            per = 0.6
        elif iss > 80:
            per = 0.4
        else:
            per = 0.2
        if p == "POSITIVE":
            return render_template('res1.html')
        else:
            return render_template('result.html', percentage=per)


if __name__ == '__main__':
    app.run(debug=True)
