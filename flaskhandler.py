from flask import Flask, jsonify, request
from pymodm import connect
from datetime import datetime
from main import add_heart_rate, create_user
from time_conversion import time_conversion
import models
import pandas as pd
import numpy as np
connect("mongodb://localhost:27017/heart_rate_app")
app = Flask(__name__)

@app.route("/api/heart_rate", methods=["POST"])
def postInfo():
    """
    Communicates with database to store user info
    """
    r = request.get_json()
    email = r["user_email"]
    age = r["user_age"]
    heart_rate = r["heart_rate"]
    time = datetime.datetime.now()
    try:
        user = add_heart_rate(email, heart_rate, time)
        print("New heart rate information was added")
    except:
        user = create_user(email, age, heart_rate, time)
        print("A new user was created")

@app.route("/api/heart_rate/<user_email>", methods=["GET"])
def getHeartRate(user_email):
    """
    Returns all heart rate measurements for user
    """
    try:
        user = models.User.objects.raw({"_id": user_email}).first()
    except:
        raise KeyError("User not in database")
    response = {
        "user_heart_rate": user.heart_rate
    }
    return jsonify(response)

@app.route("/api/heart_rate/average/<user_email>", methods=["GET"])
def getAverage(user_email):
    """
    Returns all heart rate measurements for user
    """
    try:
        user = models.User.objects.raw({"_id": user_email}).first()
        average_heart_rate = sum(user.heart_rate)/len(user.heart_rate)
    except:
        raise KeyError("User not in database")
    response = {
        "average_heart_rate": average_heart_rate,
    }
    return jsonify(response)

@app.route("/api/heart_rate/interval_average", methods=["POST"])
def postIntervalAverage():
    """
    Returns all heart rate measurements for user
    """
    r = request.get_json()
    email = r["user_email"]
    date = r["heart_rate_average_since"]
    format_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    try:
        user = models.User.objects.raw({"_id": email}).first()
        times = time_conversion(user.heart_rate_times)
        d = np.array(times)
        date_index = (d >= format_date)
        values = d[date_index]
        rates_index = np.where(times == values)[0]
        rates = user.heart_rate
        a = np.array(rates)
        filtered_rates = a[rates_index]
        average_heart_rate = sum(filtered_rates)/len(filtered_rates)
        from tachycardia import tachycardia
        t = tachycardia(user.age, average_heart_rate)
        if t == True:
            is_tachycardic = "User is tachycardic"
        else:
            print(average_heart_rate)
            is_tachycardic = "User is NOT tachycardic"
    except:
        raise IOError("User not in database")
    response = {
        "average_heart_rate": average_heart_rate,
        "is_tachycardic": is_tachycardic
    }
    return jsonify(response)
