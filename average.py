def average_hr(heart_rate):
    """
    Calculation to get the average heart rate for the user

    :param heart_rate: user heart rate

    :returns average_heart_rate: the average user heart rate
    """
    average_heart_rate = sum(heart_rate)/len(heart_rate)
    return average_heart_rate
