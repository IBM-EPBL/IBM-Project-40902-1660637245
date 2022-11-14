# IBM-Project-40902-1660637245

# Trip Based Modeling of Fuel Consumption in Modern Fleet Vehicles Using Machine Learning

This project enables the user to know the fuel consumption level by various factors such as distance,internal temperature and outside temperature 

## Project Structure

### This project has three major parts :

1.model.ipynb - This contains code for our Machine Learning model to predict the fuel consumption level for modern fleet vehicles based on training data in 'measurement.csv' file.

2.app.py - This contains Flask APIs that receives vehicles paramet  through GUI or API calls, computes the precited value based on our model and returns it.

3.template - This folder contains the HTML template (index.html) to allow user to enter employee detail and displays the predicted employee salary.
static - This folder contains the css folder with style.css file which has the styling required for out index.html file.

### Running the project
1. Ensure that you are in the project home directory, Create the machine learning model by running below command from command prompt -
```
python CarFuelConsumption.py
```
This would create a serialized version of our model into a file model.pkl

2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://127.0.0.1:5000/ (or) http://localhost:5000

You should be able to view the homepage.

Enter valid numerical values in all 8 input boxes and hit Predict.

If everything goes well, you should  be able to see the predcited fuel consumption vaule on the HTML page!
check the output here: http://127.0.0.1:5000/predict
