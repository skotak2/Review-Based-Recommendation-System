# Review_Based_Recomm_System

## OBJECTIVE

To build web application for product recommendations to customers based on their reviews at the online grocery store. The web application is a prototype to mimic a real time application where the recommendations are rendered with product images for a given input string as a review.


![Demo](Demo/demo.gif)

Check it out live [here](https://productrecsystem.herokuapp.com/)

### TABLE OF CONTENTS
* [Data](#data)
* [Technologies](#technologies)
* [Algorithm](#algorithm)
* [Architecture](#architecture)
* [Implementation](#implementation)
* [Results](#results)
* [References](#references)

## Data

The dataset was obtained from [Amazon review dataset](https://nijianmo.github.io/amazon/index.html) released in 2014, provided by UCSD. The dataset contains 287,209 products with 5,074,160 reviews and ratings by 1,57,386 unique users

## Technologies
* Python - Scikit-learn, Pipeline
* Flask 
* Docker
* Heroku

## Algorithm

We use k-means clustering algorithm to cluster all the products based on the reviews. The features would form the unsupervised clusters based on TF-IDF scores of the text. 

How do we do that ?

Each product's reviews are collected and concatenated as a single string.Now each product has the feature set of tf-idf scores for the concatenated string of reviews. Further The tf-idf scores as a feature set is used to find the euclidean distance between selected points in space, thus allowing us to implement the k-means algorithm.

Based on the number of categories in the grocery store, we get to choose the number of centroids and bucket the products with a label. We would train the model, over iterations, allowing the clusters to move farther apart in space and save the model, i.e noting down the centroid points in the space. Further, we pickle dump the dictionary of cluster labels and its corresponding products.

The conversion of a string into a tf-idf score and then find its nearest centroid point (cluster) would done using a pipeline function and saved into a joblib file.
   

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

