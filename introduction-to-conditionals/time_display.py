# Display time in 12-hour format
def time(hours, minutes, amOrPm):
    if hours>12:
        hours = str(hours-12)
    else:
        hours = str(hours)
    minutes = str(minutes)
    return hours + ":" + minutes + amOrPm

# Get user input for hours and minutes
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
if hours > 12:
    amOrPm = "pm"
else:
    amOrPm = "am"
print(time(hours, minutes, amOrPm))