# Program Name: country_or_club_statistics
# Purpose: Calculate statistics which can be done for either country or club

import csv
import logging

from dataset.reading_from_csv import read_csv_file
from dataset.render_charts import render_hor_bar_chart


def amount_players(name_column, team_column):
    """
    Get the countries/clubs and amount of players

    Parameters
    ----------
    name_column : int
        Number of the column in the csv file which contains player names

    team_column : int
        Number of the column in the csv file which contains nationalities/clubs

    Returns
    -------
    dict
        The dictionary containing key: country/club and values: amount of players for each country/club
    """

    logging.info(f'Get list of players')

    players_dict = {}

    # Get csv file content
    file_content = read_csv_file()
    # Reads each line as a csv file
    csv_data_file = csv.reader(file_content)

    # Read each line of the csv file
    for line in csv_data_file:
        try:
            # If the key isnt in the dictionary
            if not line[team_column] in players_dict:
                # Add the key and current value to the dictionary
                players_dict[line[team_column]] = [line[name_column]]
            else:
                # Otherwise the key is present append the next value to it
                players_dict[line[team_column]].append(line[name_column])
        except ValueError:
            logging.exception(f'Line {line} of the csv file has an invalid value: {line[team_column]}')

    # Sorting the items in alphabetical order ignoring case
    sorted_players_dict = dict(sorted(players_dict.items(), key=lambda x: x[0].lower()))

    # Clearing values in dictionary to reuse
    players_dict.clear()
    # Append the key and len of each value to the previously declared dictionary
    for k, v in sorted_players_dict.items():
        players_dict[k] = len(v)

    return players_dict


def get_sum_players_team(team):
    """
    Calculate amount of players for each country/club and amount of countries/clubs

    Parameters
    ----------
    team : str
        A country or club value passed depending on which route is used

    Returns
    -------
    chart
        The dictionary containing key: country/club and values: amount of players for each country/club

    int
        The amount of countries/clubs in the list
    """

    logging.info(f'Amount of players for each {team}')

    # Check if value passed is for team or country
    if team.lower() == "country":
        team_column = 9
        height = 1500
        title = "Amount of Players in Each Country"
    else:
        team_column = 7
        height = 5000
        title = "Amount of Players in Each Club"

    # Get the amount of players for each country or club
    sum_players_team = amount_players(2, team_column)

    # Split the dictionary keys and values into two separate lists
    bar_labels = list(sum_players_team.keys())
    bar_values = list(sum_players_team.values())

    # Render chart passed on above values
    bar_chart = render_hor_bar_chart(title, bar_values, bar_labels, height)

    # Amount of different clubs or countries
    amount_of_teams = len(bar_labels)

    return bar_chart, amount_of_teams
