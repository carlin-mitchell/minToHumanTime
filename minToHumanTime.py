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
  
