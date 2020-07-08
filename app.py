from flask import Flask,render_template,request
import pickle

app=Flask(__name__)

f=pickle.load(open('Titanic Survival Prediction.pickle','rb'))
#pre=f.predict([[1,23,1,45]])[0]
#print(pre)

@app.route('/')
def home():
    return render_template('tsp.html')


@app.route('/predict', methods=['POST'])
def predict():
    pclass=int(request.form['pclass'])
    age=int(request.form['age'])
    sex=int(request.form['sex'])
    fare=int(request.form['fare'])
    pre = f.predict([[pclass,age,sex,fare]])[0]
    return render_template('tsp.html',predict=f'prdiction= {pre}')



if __name__ == "__main__":
    app.run(debug=True)