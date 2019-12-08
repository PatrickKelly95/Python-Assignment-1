# Program Name: player_specific_statistics
# Purpose: Calculate player specific statistics

import csv

from stats.calculate_statistics import calc_variance, calc_correlation
from dataset.reading_from_csv import read_csv_file
import logging


def get_player_data(column_number):
    """
    Get requested player data from one of the columns in the csv file

    Parameters
    ----------
    column_number : int
        Number of the column in the csv file which a function is interested in

    Returns
    -------
    list
        The contents of a column dependent on number passed
    """

    logging.info(f'Getting player data from column {column_number}')

    player_data = []
    file_content = read_csv_file()
    csv_data_file = csv.reader(file_content)

    for line in csv_data_file:
        try:
            # Append each value from a column into a list
            player_data.append(line[column_number])
        except ValueError:
            logging.exception(f'Line {line} of the csv file has an invalid value: {line[column_number]}')

    return player_data


def get_age_statistics():
    """
    Calculate the average age of the players, the oldest and youngest players in the csv file

    Returns
    -------
    int
        The average age of the players

    int
        The minimum age of the players

    int
        The maximum age of the players
    """
    logging.info('Getting age statistics')

    # Get list of ages from player data
    ages = [int(i) for i in get_player_data(11)]

    # Calculate average age of players
    average_age = sum(ages) / len(ages)

    # Get min age
    min_age = min(ages)

    # Get max age
    max_age = max(ages)

    # Round to the nearest integer
    return round(average_age), min_age, max_age


def get_height_weight():
    """
    Calculate the average height and weight of the players in the csv file

    Returns
    -------
    float
        The average height of the players in feet and inches

    float
        The average weight of the players in stone
    """

    logging.info('Average height and weight')

    # Get the list of height and weight
    height_list = [int(i) for i in get_player_data(13)]
    weight_list = [int(i) for i in get_player_data(14)]

    # Calculate average height in cms and weight in kg
    average_height_cm = sum(height_list) / len(height_list)
    average_weight_kg = sum(weight_list) / len(weight_list)

    # Convert the height to feet and inches and weight to stone
    average_height_ft, average_height_in = calculate_height_feet(average_height_cm)
    average_height_ft_in = f"{average_height_ft:.0f}ft {average_height_in:.2f}inches"

    average_weight_st = f"{calculate_weight_stone(average_weight_kg):.1f}stone"

    return average_height_ft_in, average_weight_st


def calculate_height_feet(centi):
    """
    Convert a height from centimetres to feet and inches

    Parameters
    ----------
    centi : int
        The distance in centimetes.

    Returns
    -------
    whole_feet : int
        The feet part of the distance.
    inches : float
        The inches part of the distance.
    """

    logging.info('Calculate height in feet')

    # Calculate cms to metres
    metres = centi / 100.0

    # Calculate metres to feet
    feet = metres * 3.28084

    # Calculate whole_feet as integer part of feet
    whole_feet = int(feet)

    # Calculate the remaining inches
    inches = (feet - whole_feet) * 12

    return whole_feet, inches


def calculate_weight_stone(kg):
    """
    Convert a weight from kilograms to stone

    Parameters
    ----------
    kg : int
        The weight in kg.

    Returns
    -------
    stone : float
        The weight in stone

    """

    logging.info('Calculate weight in stone')

    # Convert kg to stone
    stone: float = kg * 0.1574

    return stone


def get_total_amount_players():
    """
    Get the total number of players in the csv file

    Returns
    -------
    int
        The number of players

    """

    logging.info('Total amount of players in file')
    total_no_players = get_player_data(2)

    return len(total_no_players)


def get_player_ratings(name_column, team_column):
    """
    Get the overall rating for each player

    Parameters
    ----------
    name_column : int
        Number of the column in the csv file which contains player names

    team_column : int
        Number of the column in the csv file which contains player ratings

    Returns
    -------
    dict
        The dictionary containing players name and rating
    """

    logging.info('Each players top overall rating')
    players_dict = {}

    file_content = read_csv_file()
    csv_data_file = csv.reader(file_content)
    for line in csv_data_file:
        try:
            # If key value isnt there already
            if not line[team_column] in players_dict:
                # Add the key and current value to the dictionary
                players_dict[line[team_column]] = [line[name_column]]
            else:
                # Otherwise check if the current rating is lower than the next value
                if str(players_dict.get(line[team_column])) < str([line[name_column]]):
                    # Update the player with the new rating
                    players_dict[line[team_column]] = [line[name_column]]
        except ValueError:
            logging.exception(f'Line {line} of the csv file has an invalid value: {line[name_column]}')

    return players_dict


def get_worst_top_players():
    """
    Calculate the best and worst players in the csv file

    Returns
    -------
    list
        The values containing the best 5 players

    list
        The values containing the worst 5 players
    """

    logging.info('Best and worst overall player ratings')

    player_ratings = get_player_ratings(6, 1)

    # Top 5 best and worst players in the list
    top_5_players = sorted(player_ratings, key=player_ratings.get, reverse=True)[:5]
    worst_5_players = sorted(player_ratings, key=player_ratings.get, reverse=False)[:5]

    return top_5_players, worst_5_players


def get_correlation_age_pace():
    """
    Get the correlation between age and pace of the players in the csv file

    Returns
    -------
    float
        The correlation between age and pace
    """

    logging.info('Correlation between age and pace')

    pace = []
    # If any value is empty convert it to a zero
    for i in get_player_data(17):
        if i == '':
            i = '0'
        pace.append(int(i))

    ages = [int(i) for i in get_player_data(11)]

    # Calculating correlation
    age_pace_correlation = f"{calc_correlation(ages, pace):.1f}"

    return float(age_pace_correlation)


def get_correlation_age_rating():
    """
    Get the correlation between age and rating of the players in the csv file

    Returns
    -------
    float
        The correlation between age and rating
    """

    logging.info('Correlation between age and rating')

    ages = [int(i) for i in get_player_data(11)]
    ratings = [int(i) for i in get_player_data(6)]

    # Calculating correlation
    age_rating_correlation = f"{calc_correlation(ages, ratings):.1f}"

    return float(age_rating_correlation)


def get_correlation_passing():
    """
    Get the correlation between passing short and long in the csv file

    Returns
    -------
    float
        The correlation between passing short and long
    """

    logging.info('Correlation between passing short and long')

    pass_short = []
    # If any value is empty convert it to a zero
    for i in get_player_data(38):
        if i == '':
            i = '0'
        pass_short.append(int(i))

    pass_long = []
    # If any value is empty convert it to a zero
    for i in get_player_data(39):
        if i == '':
            i = '0'
        pass_long.append(int(i))

    # Calculating correlation
    pass_short_long_correlation = f"{calc_correlation(pass_short, pass_long):.1f}"

    return float(pass_short_long_correlation)


def get_variance_shooting():
    """
    Get the variance of the shooting ability of the players

    Returns
    -------
    str
        The variance of the shooting ability
    str
        The standard deviation of the shooting ability
    """

    logging.info("Variance of data over shooting")

    shooting = []
    for i in get_player_data(27):
        if i == '':
            i = '0'
        shooting.append(int(i))

    variance, standard_dev = calc_variance(shooting)

    return f"{variance:.1f}", f"{standard_dev:.1f}"
