# Display time in 12-hour format
def time(hours, minutes, amOrPm):
    if hours>12:
        hours = str(hours-12)
    else:
        hours = str(hours)
    minutes = str(minutes)
    return hours + ":" + minutes + amOrPm