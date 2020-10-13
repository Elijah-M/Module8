"""
Author: Elijah Morishita
elmorishita@dmacc.edu
10/12/2020
This program computes a half-birthday using the datetime import
"""
from datetime import timedelta
import datetime


def half_birthday(year, month, day):
    """
    This function converts a birthday into a future half birthday by
    adding 182.5 days to whatever date is included in the parameters
    :param year:
    :param month:
    :param day:
    :return: Your birthday + half a year (182.5 days)
    """
    b_day = datetime.date(year, month, day)
    return b_day + timedelta(days=182.5)


if __name__ == '__main__':
    print(('=' * 40), "\nYour Half Birthday is... ", half_birthday(2020, 4, 29))
