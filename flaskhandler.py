from flask import Flask, jsonify, request
from pymodm import connect
from datetime import datetime
from main import add_heart_rate, create_user
from time_conversion import time_conversion
from average import average_hr
from filtering import time_filtering, rate_filtering
from tachycardia import tachycardia
import models
import numpy as np
connect("mongodb://localhost:27017/heart_rate_app")
app = Flask(__name__)


@app.route("/api/heart_rate", methods=["POST"])
def postInfo():
    """
    Communicates with database to store user info
    """
    try:
        r = request.get_json()
        email = r["user_email"]
        age = r["user_age"]
        heart_rate = r["heart_rate"]
        time = datetime.datetime.now()
    except:
        raise ValueError("Submit json data for email, age, and heart_rate")
        return 400
    try:
        user = add_heart_rate(email, heart_rate, time)
        print("New heart rate information was added")
    except:
        user = create_user(email, age, heart_rate, time)
        print("A new user was created")
    return 200


@app.route("/api/heart_rate/<user_email>", methods=["GET"])
def getHeartRate(user_email):
    """
    Returns all heart rate measurements for user
    """
    try:
        user = models.User.objects.raw({"_id": user_email}).first()
    except:
        raise KeyError("User not in database")
        return 400
    response = {
        "user_heart_rate": user.heart_rate
    }
    return jsonify(response), 200


@app.route("/api/heart_rate/average/<user_email>", methods=["GET"])
def getAverage(user_email):
    """
    Returns all heart rate measurements for user
    """
    try:
        user = models.User.objects.raw({"_id": user_email}).first()
        average_heart_rate = average_hr(user.heart_rate)
    except:
        raise KeyError("User not in database")
        return 400
    response = {
        "average_heart_rate": average_heart_rate,
    }
    return jsonify(response), 200


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def postIntervalAverage():
    """
    Returns all heart rate measurements for user
    """
    try:
        r = request.get_json()
        email = r["user_email"]
        date = datetime.strptime(r["heart_rate_average_since"],
                                 '%Y-%m-%d %H:%M:%S.%f')
    except:
        raise ValueError("Submit json data for email, age, and heart_rate")
        return 400
    try:
        user = models.User.objects.raw({"_id": email}).first()
    except:
        raise KeyError("User not in database")
        return 400
    try:
        times = time_conversion(user.heart_rate_times)
        filtered_times = time_filtering(times, date)
        rates_index = np.where(times == filtered_times)[0]
    except:
        raise KeyError("No time data found for user")
        return 400
    try:
        rates = user.heart_rate
        filtered_rates = rate_filtering(rates, rates_index)
        average_heart_rate = average_hr(filtered_rates)
    except:
        raise KeyError("No heart rate data found for user")
        return 400
    try:
        is_tachycardic = tachycardia(user.age, average_heart_rate)
    except:
        raise KeyError("User age not found in database")
        return 400
    response = {
        "average_heart_rate": average_heart_rate,
        "is_tachycardic": is_tachycardic
    }
    return jsonify(response), 200
