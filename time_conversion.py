from datetime import datetime


def time_conversion(time):
    """
    Converting all database timestamps to the same format because for some
    reason no matter what I do my computer refuses to put things into
    the database in a workable format

    :param time: datetime list of time heart rate data points are recorded

    :returns list_: datetime list in specific usable format
    """
    list_ = []
    for x in range(0, len(time)):
        times = time[x].strftime('%Y-%m-%d %H:%M:%S.%f')
        list_.append(datetime.strptime(times, '%Y-%m-%d %H:%M:%S.%f'))
    return list_
