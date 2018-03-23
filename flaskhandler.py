from flask import Flask, jsonify, request
from pymodm import connect
import datetime
from main import add_heart_rate, create_user
from time_conversion import time_conversion, string_conversion
from average import average_hr
from filtering import time_filtering, rate_filtering
from tachycardia import tachycardia
import models
import numpy as np
import logging
logging.basicConfig(filename="flaskhandler.txt", format='%(levelname)s\
%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
connect("mongodb://localhost:27017/heart_rate_app")
app = Flask(__name__)
"""
Flask server file logging and creating user information in a database,
retrieving hear rate information for the user, retrieving the average heart
rate over all records, finding average heart rate over a user specified period,
and determining if average heart rate is tachycardic

:param json: json data containing the user email, age, heart rate, and date
selection

:returns heart_rate: all heart rate records found for user
:returns average_heart_rate: average heart rate over all recorded values
:returns average_heart_rate_since: average heart rate over certain period
:returns is_tachycardic: indication of where heart rate is tachycardic
"""


@app.route("/api/heart_rate", methods=["POST"])
def postInfo():
    """
    Communicates with database to store user info

    :param json: json data containing the user email, age, heart rate, and date
    selection

    :raises ValueError: Error raised if data is not in the correct format
    """
    time = datetime.datetime.now()
    logging.debug("/heart_rate: time = " + str(time))
    try:
        r = request.get_json()
        email = r["user_email"]
        age = r["user_age"]
        heart_rate = r["heart_rate"]
        logging.info("/heart_rate: data received and extracted from json")
        logging.debug("/heart_rate: email = " + str(email))
        logging.debug("/heart_rate: age = " + str(age))
        logging.debug("/heart_rate: heart rate = " + str(heart_rate))
    except:
        raise ValueError("Submit json data for email, age, and heart_rate")
        logging.warning("/heart_rate: not all data points found or not json")
        return 400
    try:
        user = add_heart_rate(email, heart_rate, time)
        logging.info("/heart_rate: user located in database and info appended")
        print("New heart rate information was added")
    except:
        user = create_user(email, age, heart_rate, time)
        logging.info("/heart_rate: user was not found and was created")
        print("A new user was created")
    return 200


@app.route("/api/heart_rate/<user_email>", methods=["GET"])
def getHeartRate(user_email):
    """
    Returns all heart rate measurements for user

    :param user_email: the users email

    :returns user_heart_rate: all heart rate measurements in database for user
    :raises KeyError: Error raised if data is not in the database
    """
    try:
        user = models.User.objects.raw({"_id": user_email}).first()
        logging.info("/heart_rate/<user_email>: user found and info extracted")
        logging.debug("/heart_rate/<user_email>: user = " + str(user.email))
    except:
        raise KeyError("User not in database")
        logging.warning("/heart_rate/<user_email>: user not found in database")
        return 400
    response = {
        "user_heart_rate": user.heart_rate
    }
    logging.debug("/heart_rate/<user_email>: heart_rate = " +
                  str(user.heart_rate))
    return jsonify(response), 200


@app.route("/api/heart_rate/average/<user_email>", methods=["GET"])
def getAverage(user_email):
    """
    Returns all heart rate measurements for user

    :param user_email: the users email

    :returns average_heart_rate: average heart rate over all measurements
    :raises KeyError: Error raised if data is not in the database
    """
    try:
        user = models.User.objects.raw({"_id": user_email}).first()
        logging.info("/heart_rate/average/<user_email>: user found in database\
                     and info extracted")
        logging.debug("/heart_rate/average/<user_email>: user = " +
                      str(user.email))
        average_heart_rate = average_hr(user.heart_rate)
        logging.debug("/heart_rate/avaerae/<user_email>: average = " +
                      str(average_heart_rate))
    except:
        raise KeyError("User not in database")
        logging.warning("/heart_rate/<user_email>: user not found in database")
        return 400
    response = {
        "average_heart_rate": average_heart_rate
    }
    return jsonify(response), 200


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def postIntervalAverage():
    """
    Returns all heart rate measurements for user

    :param json: user email and date selection in json format

    :returns average_heart_rate: heart rate average over specified period
    :returns is_tachycardic: indication if average heart rate is tachycardic
    :raises ValueError: Error raised if data is not in the correct format
    :raises KeyError: Error raised if data is not in the database
    """
    try:
        r = request.get_json()
        email = r["user_email"]
        since = r["heart_rate_average_since"]
        date = string_conversion(since)
        logging.info("/heart_rate/interval_average: data received and\
                     extracted from json")
        logging.debug("heart_rate/interval_average: email = " + str(email))
        logging.debug("heart_rate/interval_average: date = " + str(date))
    except:
        raise ValueError("Submit json data for email, age, and heart_rate")
        logging.warning("heart_rate/interval_average: not all data points\
                        found or not json")
        return 400
    try:
        user = models.User.objects.raw({"_id": email}).first()
        logging.info("/heart_rate/interval_average: user found")
    except:
        raise KeyError("User not in database")
        logging.warning("heart_rate/interval_average: user not found")
        return 400
    try:
        times = time_conversion(user.heart_rate_times)
        filtered_times = time_filtering(times, date)
        rates_index = np.where(times == filtered_times)[0]
        logging.info("/heart_rate/interval_average: times found and filtered")
        logging.debug("heart_rate/interval_average: times = " + str(times))
        logging.debug("heart_rate/interval_average: filtered_times = " +
                      str(filtered_times))
        logging.debug("heart_rate/interval_average: rates_index = " +
                      str(rates_index))
    except:
        raise KeyError("No time data found for user")
        logging.warning("heart_rate/interval_average: time data not found")
        return 400
    try:
        rates = user.heart_rate
        filtered_rates = rate_filtering(rates, rates_index)
        average_heart_rate = average_hr(filtered_rates)
        logging.info("/heart_rate/interval_average: average heart rate\
                     calculated")
        logging.debug("heart_rate/interval_average: rates = " + str(rates))
        logging.debug("heart_rate/interval_average: filtered_rates = " +
                      str(filtered_rates))
        logging.debug("heart_rate/interval_average: average_heart_rate = " +
                      str(average_heart_rate))
    except:
        raise KeyError("No heart rate data found for user")
        logging.warning("heart_rate/interval_average: hr data not found")
        return 400
    try:
        is_tachycardic = tachycardia(user.age, average_heart_rate)
        logging.info("/heart_rate/interval_average: tachycardia risk\
                     calculated")
        logging.debug("heart_rate/interval_average: is_tachycardic = " +
                      str(is_tachycardic))
    except:
        raise KeyError("User age not found in database")
        logging.warning("heart_rate/interval_average: age not in database")
        return 400
    response = {
        "average_heart_rate": average_heart_rate,
        "is_tachycardic": is_tachycardic
    }
    return jsonify(response), 200
