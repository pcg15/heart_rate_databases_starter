import requests


def main():
    """
    Program that will post user heart rate information to a server that will
    store the information in a database, retrieve the users heart rate from
    the database, retrieve the average heart rate for the user, and post a
    user specified time period for average heart rate calculations and
    tachycardic indication

    :param json: json data containing the user email, age, heart rate, and date
    selection

    :returns heart_rate: all heart rate records found for user
    :returns average_heart_rate: average heart rate over all recorded values
    :returns average_heart_rate_since: average heart rate over certain period
    :returns is_tachycardic: indication of where heart rate is tachycardic
    """
    postInfo()
    getHeartRate()
    getAverage()
    postIntervalAverage()
    getData()


def postInfo():
    """
    Sends user info to server

    :param json: json data containing the user email, age, and heart rate
    """
    data = {
        "user_email": "pcg@duke.edu",
        "user_age": 24,
        "heart_rate": 178
    }
    r = requests.post("http://0.0.0.0:5000/api/heart_rate", json=data)


def getHeartRate():
    """
    Gets heart rate data from server for user

    :returns heart_rate: all heart rate records found for user
    """
    r2 = requests.get("http://0.0.0.0:5000/api/heart_rate/pcg@duke.edu")
    print(r2.json())


def getAverage():
    """
    Gets average heart rate for user

    :returns average_heart_rate: average heart rate over all recorded values
    """
    r3 = requests.get("http://0.0.0.0:5000/api/heart_rate/average/pcg@duke.edu"
                      )
    print(r3.json())


def postIntervalAverage():
    """
    Posts average heart rate calculation for user

    :param json: json data containing the user email and date
    selection

    :returns average_heart_rate_since: average heart rate over certain period
    :returns is_tachycardic: indication of where heart rate is tachycardic
    """
    data = {
        "user_email": "pcg@duke.edu",
        "heart_rate_average_since": "2018-03-09 11:00:36.372339"
    }
    r4 = requests.post("http://0.0.0.0:5000/api/heart_rate/interval_average",
                       json=data)
    print(r4.json())


def getData():
    """
    Gets heart rate data from server for user

    :returns heart_rate: all heart rate records found for user
    """
    r5 = requests.get("http://0.0.0.0:5000/api/heart_rate/get_data/pcg@duke.edu")
    print(r5.json())

if __name__ == '__main__':
    main()
