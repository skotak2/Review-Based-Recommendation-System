# Review_Based_Recomm_System
We recommend grocery products based on the reviews you feed for each product purchase . The recommendation is based on unsupervised technique - KMeans, where we cluster TF-IDF scores of the reviews and analyze them

![Demo](Demo/demo.gif)

Check the Application @ https://productrecsystem.herokuapp.com/

#PROJECT GOAL#

The aim of the project is to simulate the real-world process of deploying a product recommendation system, where different technologies are used to assist in the deployment. This report mainly highlights the overall experience and cost benefit analysis of working with these technologies, along with the code artifacts. 

In the product recommendation model used, the purchase history of customers was retrieved to capture the customer’s inclination for a set of products available in the store. The recommendation system recommends products based on customer reviews posted by the customer. 
 
This recommendation system is intended to help e-commerce websites to service customers with appropriate recommendations at the right time with an attractive price tag and could address the problem of being inundated with choices, by helping the customer filter their choices based on a variety of attributes.
     	 
HANDLING OF TECHNOLOGY & DEMONSTRATION IN A DEV ENVIRONMENT

1.	Creating the prediction model
The dataset was obtained from the website: https://nijianmo.github.io/amazon/index.html and is a part of Amazon review dataset released in 2014, provided by UCSD. The dataset contains 287,209 products with 5,074,160 reviews and ratings by 1,57,386 unique users. We created a data pipeline using the pipeline function and then dumped the pipeline object in a joblib file to avoid recomputing the same function recursively saving time and computational cost. We have clustered the products using k-means context-based filtering technique. Whenever a new input keyword is searched, it would pass through the pipeline for cluster assignment. Products under the respective clusters are up for recommendation.  
2.	HTML forms creation in templates folder
In order to recommend the product based on the user input, we created a HTML form which will allow the user to enter a text input. We added the form tag to collect the data in the search container, where we will pass the method post and name as ‘product’. By providing the method, our backend code would be able to know that we have received some data with the name ‘product’ and at the backend, we need to process that data, predict the recommendations and render it on a new html form called ‘results.html’. Both the html files are rendered through the ‘templates’ folder.
 

3.	Connected webpage with the model through flask framework
For this, we created a ‘Echo2.py’ flask script, defined a function ‘recomm’ and loaded the saved pipeline model. When a user submits the form, the webpage should display the recommended products. To accomplish this, we require the pickle file ‘dict_pickle1’ created earlier. The form values after submitting are stored in the variable ‘example_dict’ in the form of a dictionary. Further, we convert the values into a list and pass it as an argument in the predict function to return the recommended products. The flask application will route to the default URL path and call the home function and it will render the home.html. Whenever someone sends a text query, flask will detect a POST method and will get the form data with the name product and redirect to the result function. Finally, the result function will use the ‘recomm’ function to get the data and send it back to the webpage. 

 
4.	Create a Docker Container
a)	Firstly, we created a docker folder ‘docker-echo-final’ and copied the flask app ‘Echo2.py’
b)	We wrote a Dockerfile to configure the contents and start-actions of our container and built the custom docker image 
   
c)	To check if the application is running as intended, we deployed the ML model locally using the ‘run’ container command, binding the containers port 5000 to the host port 5000 using -p option. 
 
5.	Deploying flask app using Heroku
Heroku is a platform as a service which allows to deploy either an existing docker image or can build docker image itself. In order to use it, we have to register an account and 

