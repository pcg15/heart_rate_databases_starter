from flask import Flask, jsonify, request
from pymodm import connect
import models
import datetime
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
    try:
        user = models.User.objects.raw({"_id": email}).first()
        user.heart_rate.append(heart_rate)
        user.heart_rate_times.append(datetime.datetime.now())
        user.save()
    except:
        user = models.User(email, age, [], [])
        user.heart_rate.append(heart_rate)
        user.heart_rate_times.append(datetime.datetime.now())
        user.save()
    response = {
        "user_email": user.email,
        "user_heart_rate": user.heart_rate,
        "heart_rate_times": user.heart_rate_times
    }
    return jsonify(response)

@app.route("/api/heart_rate/<user_email>", methods=["GET"])
def getHeartRate(user_email):
    """
    Returns all heart rate measurements for user
    """
    try:
        user = models.User.objects.raw({"_id": user_email}).first()
    except:
        raise IOError("User not in database")
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
        raise IOError("User not in database")
    response = {
        "average_heart_rate": average_heart_rate
    }
    return jsonify(response)
