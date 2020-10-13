"""
Author: Elijah Morishita
elmorishita@dmacc.edu
10/12/2020
This program emulates a switch/case function
"""


def switch_average(case):
    """
    This function returns a value based on if its parameter is a valid key, if
    the key doesn't exist then the string "Invalid Key!" is returned.
    :param case:
    :return: The value of a key based on the parameter, if the key doesn't
    exist then the string "Invalid Key!" is returned
    """
    switch = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5
    }
    return switch.get(case, "Invalid Key!")


if __name__ == '__main__':
    print(switch_average('A'))
