from datetime import datetime

def time_conversion(time):
    list_ = []
    for x in range(0,len(time)):
        times = time[x].strftime('%Y-%m-%d %H:%M:%S.%f')
        list_.append(datetime.strptime(times, '%Y-%m-%d %H:%M:%S.%f'))
    return list_
