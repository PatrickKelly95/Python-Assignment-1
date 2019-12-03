# Program Name: database_check
# Purpose: Check if database is empty, if it is run statistic calculations then populate the db

from database.database import db
from database.models import Age, TotalPlayers, BestPlayers, WorstPlayers, AvgHeightWeight, Correlation, \
    Variance
from stats.player_specific_statistics import get_age_statistics, get_total_amount_players, get_worst_top_players, \
    get_height_weight, get_correlation_age_rating, get_correlation_age_pace, get_correlation_passing, \
    get_variance_shooting
import logging


def check_db_total_players():
    """
    Populate table with total players if empty otherwise read data from table

    Returns
    -------
    int
        The number of players
    """
    # Query to check if database is empty
    is_db_empty = TotalPlayers.query.first()

    if is_db_empty is None:
        logging.info("Total Players table is empty")
        # Get total amount of players
        total_players = get_total_amount_players()
        # Added the value to the database table
        total = TotalPlayers(total_players=total_players)
        # Table variable needs to be added to the session
        db.session.add(total)
        # Committed changes to database table
        db.session.commit()
        return total_players
    else:
        logging.info("Total Players table has data")
        # Query to return all values from the database table
        total_no_players = db.session.query(TotalPlayers).all()
        for number in total_no_players:
            # Returns value from that particular column
            return number.total_players


def check_db_age():
    """
    Populate table with avg, min and max age if empty otherwise read data from table

    Returns
    -------
    int
        The average age
    int
        The minimum age
    int
        The maximum age
    """
    is_db_empty = Age.query.first()

    if is_db_empty is None:
        logging.info("Age table is empty")
        average_age, min_age, max_age = get_age_statistics()
        age = Age(average_age=average_age, min_age=min_age, max_age=max_age)
        db.session.add(age)
        db.session.commit()
        return average_age, min_age, max_age
    else:
        logging.info("Age table has data")
        age = db.session.query(Age).all()
        for stats in age:
            return stats.average_age, stats.min_age, stats.max_age


def check_db_best_players():
    """
    Populate table with best 5 players if empty otherwise read data from table

    Returns
    -------
    list
        The top 5 players in the csv file
    """
    is_db_empty = BestPlayers.query.first()

    if is_db_empty is None:
        logging.info("Best Players table is empty")

        best_players = get_worst_top_players()[0]

        for player in best_players:
            best = BestPlayers(best_players=player)
            db.session.add(best)
        db.session.commit()

        return best_players
    else:
        players_list = []
        logging.info("Best Players table has data")
        best_players = db.session.query(BestPlayers).all()
        for player in best_players:
            players_list.append(player.best_players)

        return players_list


def check_db_worst_players():
    """
    Populate table with worst 5 players if empty otherwise read data from table

    Returns
    -------
    list
        The worst 5 players in the csv file
    """
    is_db_empty = WorstPlayers.query.first()

    if is_db_empty is None:
        logging.info("Worst Players table is empty")

        worst_players = get_worst_top_players()[1]

        for player in worst_players:
            worst = WorstPlayers(worst_players=player)
            db.session.add(worst)
        db.session.commit()

        return worst_players
    else:
        players_list = []
        logging.info("Worst Players table has data")
        worst_players = db.session.query(WorstPlayers).all()
        for player in worst_players:
            players_list.append(player.worst_players)

        return players_list


def check_db_height_weight():
    """
    Populate table with avg height and weight if empty otherwise read data from table

    Returns
    -------
    str
        The average height
    str
        The average weight
    """
    is_db_empty = AvgHeightWeight.query.first()

    if is_db_empty is None:
        logging.info("Height and Weight table is empty")
        average_height, average_weight = get_height_weight()
        age_height_weight = AvgHeightWeight(average_height=average_height, average_weight=average_weight)
        db.session.add(age_height_weight)
        db.session.commit()
        return average_height, average_weight
    else:
        logging.info("Height and Weight table has data")
        age_height_weight = db.session.query(AvgHeightWeight).all()
        for stats in age_height_weight:
            return stats.average_height, stats.average_weight


def check_db_correlation():
    """
    Populate table with correlation results if empty otherwise read data from table

    Returns
    -------
    float
        The correlation between age and rating
    float
        The correlation between age and pace
    float
        The correlation between passing short and long
    """
    is_db_empty = Correlation.query.first()

    if is_db_empty is None:
        logging.info("Correlation table is empty")

        age_rating_correlation = get_correlation_age_rating()
        age_pace_correlation = get_correlation_age_pace()
        pass_short_long_correlation = get_correlation_passing()

        correlation = Correlation(age_rating_correlation=age_rating_correlation,
                                  age_pace_correlation=age_pace_correlation,
                                  pass_short_long_correlation=pass_short_long_correlation)
        db.session.add(correlation)
        db.session.commit()
        return age_rating_correlation, age_pace_correlation, pass_short_long_correlation
    else:
        logging.info("Correlation table has data")
        correlation = db.session.query(Correlation).all()
        for stats in correlation:
            return stats.age_rating_correlation, stats.age_pace_correlation, stats.pass_short_long_correlation


def check_db_variance():
    """
    Populate table with variance results if empty otherwise read data from table

    Returns
    -------
    str
        The variance of shooting ability
    str
        The standard deviation of variance of shooting ability
    """
    is_db_empty = Variance.query.first()

    if is_db_empty is None:
        logging.info("Variance table is empty")
        variance_st, standard_dev = get_variance_shooting()
        variance = Variance(variance=variance_st, standard_dev=standard_dev)
        db.session.add(variance)
        db.session.commit()
        return variance_st, standard_dev
    else:
        logging.info("Variance table has data")
        variance_st = db.session.query(Variance).all()
        for stats in variance_st:
            return stats.variance, stats.standard_dev
