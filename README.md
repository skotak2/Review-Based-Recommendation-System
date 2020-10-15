# Review_Based_Recomm_System
We recommend grocery products based on the reviews you feed for each product purchase . The recommendation is based on unsupervised technique - KMeans, where we cluster TF-IDF scores of the reviews and analyze them
<!DOCTYPE html>
<html>
<head>
	<style> 
          nav{
          	width: 50%;
          	background:linear-gradient(#D0EF88, #B4DE53);
          	background:-moz-linear-gradient(#D0EF88, #B4DE53);
          	background:-webkit-linear-gradient(#D0EF88, #B4DE53);
          	margin-left: 420px;


          }

	</style>
</head>
<body>
  <style>
     body {
        background-image: url('https://ncphwr.org.uk/wp-content/uploads/2018/02/cs9-barriers-healthy-eat.-facebook2-1.jpg');
          }
  </style>
<nav>
<div align="center" >    
    <h1 style="color:black; font-size:30px ; font-weight:bolder; margin-top: 170px; margin-left: 1px; font-family: sans-serif; margin-right: 20px">Product Recommendation</h1>
  <form action="/result" method="POST">
    <label for="Search Product name" style="font-size: 15px; font-weight:bolder; color:black; margin-left: 50px; margin-right: 100px; font-family: sans-serif; padding: 0.5px">Post your product review</label>
    <input type="text" id="product" name="product" style="font-size:15px; margin-bottom: 10px; margin-left: 15px; width:350px; padding-left: 60px; font-family: sans-serif; font-weight: bold">
    <input type="submit" value="Post" style="font-size: 14px; font-weight:bolder; font-family: sans-serif">
  </form>
</div>
</nav>
</body>
</html>
