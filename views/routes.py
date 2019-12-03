# Program Name: routes
# Purpose: Separating out the routes for a large application to make app smaller and more readable

import logging
from flask import Blueprint, render_template
from stats.country_or_club_statistics import get_sum_players_team
from stats.country_specific_statistics import world_map
from dataset.render_charts import render_bar_chart
from views.database_check import check_db_age, check_db_total_players, \
    check_db_worst_players, check_db_best_players, check_db_height_weight, check_db_correlation, check_db_variance

# Define the blueprint
routes_blueprint = Blueprint('index', __name__)

# Decorator to tell Flask what URL should trigger our function.
@routes_blueprint.route("/")
def index():
    logging.info('Accessing home page')
    # Renders html content at the given URL
    return render_template("home.html")


@routes_blueprint.route("/players")
def players_statistics():
    logging.info('Accessing player statistics page')

    # Total number of players
    total_no_players = check_db_total_players()

    # Get player age statistics
    average_age, min_age, max_age = check_db_age()
    age_bar_chart = render_bar_chart("Age Statistics", "Ages", average_age, min_age, max_age)

    # Worst and Best players
    top_players = check_db_best_players()
    worst_players = check_db_worst_players()

    # Average height in ft and inches and weight in stones
    average_height, average_weight = check_db_height_weight()

    # Correlation between age and rating
    # Correlation between age and pace
    # Correlation between passing short and passing long
    age_rating_correlation, age_pace_correlation, pass_short_long_correlation = check_db_correlation()

    # Variance of shooting ability
    variance, standard_dev = check_db_variance()

    return render_template("players.html", total_no_players=total_no_players, top_five_players=top_players,
                           worst_five_players=worst_players, average_age=average_age, min_age=min_age,
                           max_age=max_age, age_bar_chart=age_bar_chart, average_height=average_height,
                           average_weight=average_weight, age_rating_correlation=age_rating_correlation,
                           age_pace_correlation=age_pace_correlation,
                           pass_short_long_correlation=pass_short_long_correlation, variance=variance,
                           standard_dev=standard_dev)


@routes_blueprint.route("/countries")
def countries_statistics():
    logging.info('Accessing country statistics page')

    # Total number of players for each country
    bar_chart, amount_of_countries = get_sum_players_team("country")

    # Render world map with list of countries Prefix* Some countries might be missing due to the naming differences
    # between pygal and csv file e.g. "Republic of Ireland" instead of "Ireland"
    worldmap = world_map()

    return render_template("countries.html", chart=bar_chart, amount_of_countries=amount_of_countries, worldmap=worldmap)


@routes_blueprint.route("/clubs")
def clubs_statistics():
    logging.info('Accessing club statistics page')

    # Total number of players for each club
    bar_chart, amount_of_clubs = get_sum_players_team("club")

    return render_template("clubs.html", chart=bar_chart, amount_of_clubs=amount_of_clubs)