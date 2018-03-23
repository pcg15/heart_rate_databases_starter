from pymodm import connect
import models
import datetime


def add_heart_rate(email, heart_rate, time):
    """
    Adds heart rate data for user

    :param email: the users email
    :param heart_rate: the users heart rate
    :param time: timestamp for when the data is being recorded

    :returns heart_rate: appended list of user heart rate data
    :raises heart_rate_times: appended list timestamps
    """
    user = models.User.objects.raw({"_id": email}).first()
    user.heart_rate.append(heart_rate)
    user.heart_rate_times.append(time)
    user.save()


def create_user(email, age, heart_rate, time):
    """
    Creates new user

    :param email: the users email
    :param age: the users age
    :param heart_rate: the users heart rate
    :param time: timestamp for when the data is being recorded

    :returns heart_rate: appended list of user heart rate data
    :raises heart_rate_times: appended list timestamps
    """
    u = models.User(email, age, [], [])
    u.heart_rate.append(heart_rate)
    u.heart_rate_times.append(time)
    u.save()


def print_user(email):
    """
    Prints user information

    :param email: the users email

    :returns email: users email
    :returns heart_rate: appended list of user heart rate data
    :raises heart_rate_times: appended list timestamps
    """
    user = models.User.objects.raw({"_id": email}).first()
    print(user.email)
    print(user.heart_rate)
    print(user.heart_rate_times)

if __name__ == "__main__":
    connect("mongodb://localhost:27017/heart_rate_app")
    create_user(email="suyash@suyashkumar.com", age=24, heart_rate=60)
    add_heart_rate("suyash@suyashkumar.com", 60, datetime.datetime.now())
    print_user("suyash@suyashkumar.com")
