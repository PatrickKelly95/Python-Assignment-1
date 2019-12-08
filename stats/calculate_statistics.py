# Program Name: calculate_statistics
# Purpose: Calculate generic statistical information

import logging
from math import sqrt


def calc_correlation(x_values, y_values):
    """
    Calculate the correlation of two lists of numbers

    Parameters
    ----------
    x_values : list
        A list of values.

    y_values : list
        A list of related values

    Returns
    -------
    float
        The correlation between the lists, or None if it cannot be calculated.
    """

    # Check if correlation can be calculated
    if not check_list_all_numbers(x_values) or not check_list_all_numbers(x_values) or len(x_values) != len(y_values):
        return None
    else:
        logging.info('Calculate correlation')

        # Calculate the means
        x_mean = calc_mean(x_values)
        y_mean = calc_mean(y_values)

        # create a list of the deviations
        x_deviations = [x - x_mean for x in x_values]
        y_deviations = [y - y_mean for y in y_values]

        # Create a list of the deviations multiplied
        xy_deviations = [x * y for (x, y) in zip(x_deviations, y_deviations)]

        # Create a list of the deviations squared
        x_sqd_deviations = [(x - x_mean) ** 2 for x in x_values]
        y_sqd_deviations = [(y - y_mean) ** 2 for y in y_values]

        # Calculate and return the standard deviation
        return sum(xy_deviations) / (sqrt(sum(x_sqd_deviations)) * sqrt(sum(y_sqd_deviations)))


def check_list_all_numbers(values):
    """
    To check if the values in a list are all numbers

    Parameters
    ----------
    values : list
        A list of values.

    Returns
    -------
    bool
        True if the values in the list are all numbers.
        False if the list is empty, or if there is at least 1 non-numeric value.
    """

    # Empty list returns False
    if len(values) == 0:
        return False
    else:
        logging.info('Check if list of values are numbers')

        # Check for non-numeric value
        for value in values:
            if not isinstance(value, (int, float)):
                return False
        # Otherwise all values are numbers
        else:
            return True


def calc_mean(values):
    """
    Calculate the mean (average) of a list of numbers

    Parameters
    ----------
    values : list
        A list of numbers.

    Returns
    -------
    float
        The mean value.

    """

    try:
        logging.info('Calculate Mean Values')

        # Mean is the sum of the values divided by the number of values
        return sum(values) / len(values)

    # ZeroDivisionError - if the list is empty
    # TypeError - is the list is not all
    except (ZeroDivisionError, TypeError):
        logging.exception(f'ZeroDivisionError or TypeError')
        return None


def calc_variance(x_values):
    """
    Calculate the variance(how are spread out from their average value)

    Parameters
    ----------
    x_values : list
        A list of numbers.

    Returns
    -------
    float
        The variance of the data

    float
        The standard deviation of the data

    """

    # Check if the values passed are numeric
    if not check_list_all_numbers(x_values):
        return None
    else:
        logging.info("Calculating variance")

        # Getting the average of the data passed
        average = sum(x_values) / len(x_values)

        squared_values = []
        for i in x_values:
            # Subtracting the average against each value in the data
            x = i - average
            #Squaring resulting value of x
            square = x ** 2
            squared_values.append(square)

        # Getting the sum of all squared values
        sum_of_squares = sum(squared_values)

        variance = sum_of_squares / len(x_values)
        standard_deviation = sqrt(variance)

        return variance, standard_deviation
