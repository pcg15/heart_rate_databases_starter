import requests

def main():
    postInfo()
    getHeartRate()
    getAverage()
    #postIntervalAverage()

def postInfo():
    """
    Sends user info to server
    """
    data = {
        "user_email": "pcg15@duke.edu",
        "user_age": 24, #// in years
        "heart_rate": 78
    }
    r = requests.post("http://0.0.0.0:5000/api/heart_rate", json=data)
    #r_response = r.json()
    print(r.json())

def getHeartRate():
    """
    Gets heart rate data from server for user
    """
    r2 = requests.get("http://0.0.0.0:5000/api/heart_rate/pcg15@duke.edu")
    print(r2.json())

def getAverage():
    """
    Gets average heart rate for user
    """
    r3 = requests.get("http://0.0.0.0:5000/api/heart_rate/average/pcg15@duke.edu")
    print(r3.json())

if __name__ == '__main__':
    main()
