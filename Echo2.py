import os
import flask
from joblib import load
import pickle

#creating instance of the class
app=flask.Flask(__name__)
port = int(os.environ.get("PORT", 5000))

#to tell flask what url shoud trigger the function index()
@app.route('/')
def home():
    return flask.render_template('home.html')

#Prediction function
def recomm(text):
  pipeline = load("text_classification.joblib")
  pickle_in = open("dict.pickle","rb")
  example_dict = pickle.load(pickle_in)
  out_pred = pipeline.predict(text)
  list_recomm = [id for id, pred in example_dict.items() if pred == out_pred][:20]
  res = ' '.join([str(item) for item in list_recomm]) 
  return res


@app.route('/result', methods=['POST'])
def result():
    if flask.request.method == 'POST':
        user = flask.request.form
        prediction = recomm(user)
        return flask.render_template("result.html",prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
           
