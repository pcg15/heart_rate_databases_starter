from flask import Flask, jsonify, request
from pymodm import connect
import models
import datetime
app = Flask(__name__)

@app.route("/api/heart_rate", methods=["POST"])
def postInfo():
    """
    Communicates with database to store user info
    """
    r = request.get_json()
    connect("mongodb://localhost:27017/heart_rate_app")
    email = r["user_email"]
    age = r["user_age"]
    heart_rate = r["heart_rate"]
    user = models.User.objects.raw({"_id": email}).first()
    if user.exists():
        user.heart_rate.append(heart_rate)
        user.heart_rate_times.append(time)
        user.save()
    else:
        u = models.User(email, age, [], [])
        u.heart_rate.append(heart_rate)
        u.heart_rate_times.append(datetime.datetime.now())
        u.save()
    print(user.email)
    print(user.heart_rate)
    print(user.heart_rate_times)

@app.route("/api/heart_rate/<user_email>", methods=["GET"])
def getHeartRate():
    """
    Returns all heart rate measurements for user
    """
    email = "{0}"
    connect("mongodb://localhost:27017/heart_rate_app")
    user = models.User.objects.raw({"_id": email}).first()
    print(user.heart_rate())

@app.route("/api/heart_rate/average/<user_email>", methods=["GET"])
def getHeartRate():
    """
    Returns all heart rate measurements for user
    """
    email = "{0}"
    connect("mongodb://localhost:27017/heart_rate_app")
    user = models.User.objects.raw({"_id": email}).first()
    average_heart_rate = sum(user.heart_rate())/len(user.heart_rate())
    print(average_heart_rate())

@app.route("/api/heart_rate/interval_average", methods=["POST"])
def getHeartRate():
    """
    Returns all heart rate measurements for user
    """
    import numpy
    r = request.get_json()
    connect("mongodb://localhost:27017/heart_rate_app")
    email = r["user_email"]
    date = r["heart_rate_average_since"]
    user = models.User.objects.raw({"_id": email}).first()
    if user.exists():
        times = user.heart_rate_times()
        index = numpy.where(times >= date)[0]
        rates = user.heart_rate()
        filtered_rates = rates[index:]
        average_heart_rate = sum(filtered_rates)/len(filtered_rates)
        age = user.age()
        if age > 15:
            if average_heart_rate > 100:
                tachycardia = True
            else:
                tachycardia = False
        if 12 <= age && age <= 15:
            if average_heart_rate > 119:
                tachycardia = True
            else:
                tachycardia = False
        if 8 <= age && age <= 11:
            if average_heart_rate > 130:
                tachycardia = True
            else:
                tachycardia = False
        if 5 <= age && age <= 7:
            if average_heart_rate > 133:
                tachycardia = True
            else:
                tachycardia = False
        if 3 <= age && age <= 4:
            if average_heart_rate > 137:
                tachycardia = True
            else:
                tachycardia = False
        if 1 <= age && age <= 2:
            if average_heart_rate > 151:
                tachycardia = True
            else:
                tachycardia = False
        if tachycardia == True:
            print(average_heart_rate)
            print("User is tachycardic")
        else:
            print(average_heart_rate)
            print("User is not tachycardic")
    else:
        print("User not found")
