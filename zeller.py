
import datetime
import random
import calendar
import math


def showdatesanddays():

    """
    Creates a selection of random dates and runs the Zeller Algorithm on them,
    printing out the date, and then the day according to Python and Zeller.
    """

    # Zeller gives a value 0 to 6 representing Saturday to Friday
    zellerdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    for i in range(0, 19):

        d = datetime.date.fromtimestamp(random.randint(1, 1000000000))

        print("Date:   " + str(d))
        print("Python: " + calendar.day_name[d.weekday()])
        print("Zeller: " + zellerdays[zellergregorian(d)])
        print("------------------")


def zellergregorian(d):

    """
    Runs the Zeller algorithm on the given date
    and returns the day index 0 to 6 for Saturday to Friday.
    """

    q = d.day
    m = d.month
    Y = d.year

    # adjust month to run from 3 to 14 from March to February
    if m <= 2:
        m+= 12

    # and also adjust year if January or February
    if d.month <= 2:
        Y -= 1

    h = (q + math.floor((13 * (m + 1)) / 5) + Y + math.floor(Y / 4) - math.floor(Y / 100) + math.floor(Y / 400)) % 7

    return h
