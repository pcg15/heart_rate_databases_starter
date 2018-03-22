from flask import Flask, jsonify, request
from pymodm import connect
import models
import datetime
import pandas
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
    print(time)
    try:
        user = models.User.objects.raw({"_id": email}).first()
        user.heart_rate.append(heart_rate)
        user.heart_rate_times.append(time)
        user.save()
    except:
        user = models.User(email, age, [], [])
        user.heart_rate.append(heart_rate)
        user.heart_rate_times.append(time)
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

@app.route("/api/heart_rate/interval_average", methods=["POST"])
def postIntervalAverage():
    """
    Returns all heart rate measurements for user
    """
    import numpy
    r = request.get_json()
    email = r["user_email"]
    date = datetime.datetime(r["heart_rate_average_since"])
    try:
        user = models.User.objects.raw({"_id": email}).first()
        times = user.heart_rate_times
        df = DataFrame({'times': times})
        index = df.iloc[df.index.get_loc(date,method='nearest')]
        #nearest = min(times, key=lambda x: abs(x - date))
        rates = user.heart_rate
        filtered_rates = rates[index:]
        average_heart_rate = sum(filtered_rates)/len(filtered_rates)
        from tachycardia import tachycardia
        t = tachycardia(user.age, average_heart_rate)
        if t == True:
            is_tachycardic = print("User is tachycardic")
        else:
            print(average_heart_rate)
            is_tachycardic = print("User is not tachycardic")
    except:
        raise IOError("User not in database")
    response = {
        "average_heart_rate": average_heart_rate,
        "is_tachycardic": is_tachycardic
    }
    return jsonify(response)
