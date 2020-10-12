"""
Author: Elijah Morishita
elmorishita@dmacc.edu
10/12/2020
This programs tests if a number entered in the parameters of in_dict matches the
pre-determined set within the in_dict function
"""


def in_dict(my_dictionary):
    """
    This function compares my_dicitonary to the key in your_dictionary
    :param my_dictionary:
    :return: True or False depending on the parameter
    """
    your_dictionary = {1: "First", 2: "Second", 3: "Third", 4: "Fourth"}
    if my_dictionary in your_dictionary:
        return True
    else:
        return False


if __name__ == '__main__':
    print(in_dict(4))
