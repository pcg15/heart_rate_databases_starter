# heart_rate_databases_introduction [![Build Status](https://travis-ci.org/pcg15/heart_rate_databases_introduction.svg?branch=master)](https://travis-ci.org/pcg15/heart_rate_databases_introduction)
### ONLINE README: http://heart-rate-databases-introduction.readthedocs.io/en/latest/
Databases Assignment ([here](https://github.com/mlp6/Medical-Software-Design/blob/master/Lectures/databases/main.md#mini-projectassignment)). 

Server code can be found in `flaskhandler.py`. The accompanying client program is found in `client.py`.

To get started with this program, you first need to get the server program running. After installing all python dependencies using 
```
pip install -r requirements.txt
```
you can begin to run the server. To do that, you can run `flaskhandler.py` with gunicorn. All other python files in this repo contain functions called by `flaskhandler.py` and are needed in order for the server to function properly. This includes 
*`average.py` : calculates average heart rate 
*`filtering.py` : helps retrieve user-specified heart rate data
*`main.py` : template for finding and creating a new user in mongo
*`models.py` : model file for a user in the mongo database
*`tachycardia.py` : determines whether a given heart rate is considered tachycardic given the patient's age
The database also needs to be running via docker.
```
docker run -v $PWD/db:/data/db -p 27017:27017 mongo
```
Once the database and server are running, you can run `client.py`. The client file contains a template json data setup that can be altered to reflect varied user input. 
