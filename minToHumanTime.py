#excellent work!

import math

def min_to_human_readable(minutes):
    days = math.floor(minutes / 1440)
    hours = math.floor((minutes / 60) - days * 24)
    rem_min = minutes - ((days * 1440) + (hours * 60))

    if days > 1 or days == 0:
        days_plural = "s"
    else:
        days_plural = ""

    if hours > 1 or hours == 0:
        hours_plural = "s"
    else:
        hours_plural = ""

    if rem_min > 1 or rem_min == 0:
        rem_min_plural = "s"
    else:
        rem_min_plural = ""
        
    return [f"{str(days)} day{days_plural}", f"{str(hours).zfill(2)} hour{hours_plural}", f"{str(rem_min).zfill(2)} minute{rem_min_plural}"]
  
#now try making it shorter like this:

intervals = (
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
)

def display_time(seconds, granularity=2):
    result = []
    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])

#or this

from datetime import datetime, timedelta
def GetTime():
    sec = timedelta(seconds=int(input('Enter the number of seconds: ')))
    d = datetime(1,1,1) + sec

    print("DAYS:HOURS:MIN:SEC")
    print("%d:%d:%d:%d" % (d.day-1, d.hour, d.minute, d.second))
    
 #examples from: https://stackoverflow.com/questions/4048651/python-function-to-convert-seconds-into-minutes-hours-and-days
