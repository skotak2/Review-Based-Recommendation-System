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
  pipeline = load("model_pipeline.joblib")
  pickle_in = open("product_lkp.pickle1","rb")
  example_dict = pickle.load(pickle_in)
  out_pred = pipeline.predict([text])
  list_recomm = [id for id, pred in example_dict.items() if pred == out_pred][:20]
  #res = ' '.join([str(item) for item in list_recomm]) 
  return list_recomm


@app.route('/result', methods=['POST'])
def result():
    if flask.request.method == 'POST':
        user = flask.request.form["product"]
        prediction = recomm(user)
        p1=prediction[0]
        p2=prediction[1]
        p3=prediction[2]
        p4=prediction[3]
        p5=prediction[4]
        return flask.render_template("result.html",p1=p1,p2=p2,p3=p3,p4=p4,p5=p5)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
           
