import numpy as np


def time_filtering(times, date):
    """
    Filters time stamps in database to only those since the time requested by
    the user
    """
    array_ = np.array(times)
    time_index = (array_ >= date)
    filtered_times = array_[time_index]
    return filtered_times


def rate_filtering(rates, rates_index):
    """
    Filters heart rates to only those recorded since the time inserted by the
    user
    """
    array_ = np.array(rates)
    filtered_rates = array_[rates_index]
    return filtered_rates
