import numpy as np
import datetime


def test_average():
    from average import average_hr
    list_ = [3, -5, 6, 3.4]
    function = average_hr(list_)
    assert function == 1.85


def test_time_filtering():
    from filtering import time_filtering
    times = ["2018-03-09 11:00:36.372339", "2018-03-09 11:00:36.372339",
             "2018-03-09 11:00:36.372339"]
    date = "2018-03-09 11:00:36.372339"
    array_ = (['2018-03-09 11:00:36.372339',
               '2018-03-09 11:00:36.372339',
               '2018-03-09 11:00:36.372339'])
    a = np.array(times)
    function = time_filtering(times, date)
    assert type(function) == type(a)


def test_rate_filtering():
    from filtering import rate_filtering
    rates = [78, 45, 23, 5]
    rates_index = [0, 3]
    a = np.array(rates)
    function = rate_filtering(rates, rates_index)
    assert type(function) == type(a)


def test_time_conversion():
    from time_conversion import time_conversion
    time = [datetime.datetime.now(), datetime.datetime.now(),
            datetime.datetime.now()]
    t = time[2]
    function = time_conversion(time)
    assert function[2] == t


def test_tachycardia():
    from tachycardia import tachycardia
    age = 24
    average_heart_rate = 78
    function = tachycardia(age, average_heart_rate)
    assert function == "User is NOT tachycardic"
    age2 = 24
    average_heart_rate2 = 180
    function2 = tachycardia(age2, average_heart_rate2)
    assert function2 == "User is tachycardic"


def test_tachycardic():
    from tachycardia import tachycardic
    x = 3 > 2
    y = 3 < 2
    function = tachycardic(x)
    assert function == "User is tachycardic"
    function2 = tachycardic(y)
    assert function2 == "User is NOT tachycardic"
