import numpy as np


def time_filtering(times, date):
    """
    Filters time stamps in database to only those since the time requested by
    the user

    :param times: datetime list of times data was recorded
    :param date: datetime user selected date and time

    :returns filtered_times: the times within user specification
    """
    array_ = np.array(times)
    time_index = (array_ >= date)
    filtered_times = array_[time_index]
    return filtered_times


def rate_filtering(rates, rates_index):
    """
    Filters heart rates to only those recorded since the time inserted by the
    user

    :param rates: list of user heart rates
    :param rates_index: the index corresponding to data points within range

    :returns is_tachycardic: the rates corresponding to the selected time range
    """
    array_ = np.array(rates)
    filtered_rates = array_[rates_index]
    return filtered_rates
