"""
Author: Elijah Morishita
elmorishita@dmacc.edu
10/12/2020
This programs tests if a number entered in the parameters of in_set matches the
pre-determined set within the in_set function
"""


def in_set(my_set):
    """
    This function returns True if the parameter (my_set) is in your_set,
    or it returns false if the parameter (my_set) is not in your_set
    :param my_set:
    :return: True or False depending on if the parameter is in your_set
    """
    
    your_set = {19, 20, 21, 23, 23, 24}

    if my_set in your_set:
        return True
    else:
        return False


if __name__ == '__main__':
    print(in_set(25))
