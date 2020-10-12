"""
Author: Elijah Morishita
elmorishita@dmacc.edu
10/12/2020
This program prompts the user to input the amount of test scores along with the actual
scores, combines the data into a dictionary, and prints the average of the scores
"""


def average_scores(scores_dict):
    """
    This function calculates the average of a dictionary, then returns the value
    :param scores_dict:
    :return: The average of the scores_dict dictionary
    """
    sums = 0
    for x in range(len(scores_dict)):
        sums = sums + scores_dict[x+1]

    return sums / len(scores_dict)


def get_test_scores():
    """
    This function combines the number of test scores and the actual test
    scores into a dictionary called scores_dict
    :return:
    """

    scores_dict = dict()
    while True:  # checking the input
        try:
            num_scores = int(input("Please enter the number of Test Scores: "))
            break  # This will end the while loop if the correct input has been received
        except:
            print("Invalid input, please try again.")

    for x in range(num_scores):
        scores_dict = ({x+1: ""})  # adds the amount of num_scores, one by one, into scores_dict as the keys

    for x in range(num_scores):
        while True:
            try:
                score = float(input("Enter a test score: "))
                break  # This will end the while loop if the correct input has been received
            except:
                print("Invalid input, please try again.")
        scores_dict.update({x+1: score})  # adds the test scores to scores_dict as the values

    print(("=" * 30), "\nOverall Average: ", average_scores(scores_dict))


if __name__ == '__main__':
    get_test_scores()
