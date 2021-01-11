
import numpy as np
from flask import Flask,render_template,request
import pickle


app = Flask(__name__)
model = pickle.load(open("C:\\Users\\risto\\Documents\\GitHub\\Deploying-ML-on-Cloud\\lr_model.pkl", "rb"
))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict_expenses',methods=['POST'])
def predict_expenses():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Predicted monthly grocery expenses $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)

