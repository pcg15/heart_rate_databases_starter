# heart_rate_databases_introduction [![Build Status](https://travis-ci.org/pcg15/heart_rate_databases_introduction.svg?branch=master)](https://travis-ci.org/pcg15/heart_rate_databases_introduction)
## ONLINE README: http://heart-rate-databases-introduction.readthedocs.io/en/latest/
Databases Assignment ([here](https://github.com/mlp6/Medical-Software-Design/blob/master/Lectures/databases/main.md#mini-projectassignment)).

### ABOUT

Server code can be found in `flaskhandler.py`. The accompanying client program is found in `client.py`.

This server handles `GET` and `POST` requests for the following instances:
* `POST /api/heart_rate` : finds and adds user information or creates a new user given json input from `client.py`
* `GET /api/heart_rate/<user_email>` : finds heart rate information associated with the specified user email and outputs all of the user's heart rates
* `GET /api/heart_rate/average/<user_email>` : finds user information associated with the specified user email and outputs the average user heart rate over all heart rates within the database
* `POST /api/heart_rate/interval_average` : finds user information and returns the average user heart rate over a user specified time interval that was sent to the server as json input data found within `client.py` ; also returns whether the average is considered tachycardic given the user's age
* `GET /api/heart_rate/get_data/<user_email>` : finds user information associated with the specified user email and returns heart rate and accompanying time stamp information for the given user

The `client.py` file can be altered to reflect changing user input. Given the server and client files, the program should be able to handle all instances stated above.

### GETTING STARTED

To get started with this program, you first need to clone this repository onto your local machine. Make sure that all python dependencies are installed onto your machine using 
```
pip install -r requirements.txt
```
To start running the server, first you need to make sure the database is up and running using docker.
```
docker run -v $PWD/db:/data/db -p 27017:27017 mongo
```
Next, you can run `flaskhandler.py` with gunicorn to run the server using
```
gunicorn --bind 0.0.0.0:5000 flaskhandler:app
```
or substitute with the address of your virtual machine if you wish to run the server there instead of on your local machine. The `client.py` code will also need to be edited (lines 38, 48, 59-60, 79, and 90-91) based on where you choose to run your server and/or database.
All other python files in this repo contain functions called by `flaskhandler.py` and are needed in order for the server to function properly. This includes:
* `average.py` : calculates average heart rate
* `filtering.py` : helps retrieve user-specified heart rate data
* `main.py` : template for finding and creating a new user in mongo
* `models.py` : model file for a user in the mongo database
* `tachycardia.py` : determines whether a given heart rate is considered tachycardic given the patient's age

Once the database and server are running, you can run `client.py` using 
```
python client.py
```
The client file contains a template json data setup for user POST requests that can be altered to reflect varied user input.
