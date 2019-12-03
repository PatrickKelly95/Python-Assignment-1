# Program Name: models
# Purpose: Creates individual tables in database for each statistic

from database.database import db


# Create table based on age statistics
class Age(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    average_age = db.Column(db.Integer, unique=False)
    min_age = db.Column(db.Integer, unique=False)
    max_age = db.Column(db.Integer, unique=False)


# Create table based on total number of players
class TotalPlayers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_players = db.Column(db.Integer, unique=False)


# Create table based on top 5 best players
class BestPlayers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    best_players = db.Column(db.String, unique=False)


# Create table based on top 5 worst players
class WorstPlayers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    worst_players = db.Column(db.String, unique=False)


# Create table based on average height and weight
class AvgHeightWeight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    average_height = db.Column(db.String, unique=False)
    average_weight = db.Column(db.String, unique=False)


# Create table based on correlation between different statistics in the csv file
class Correlation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age_rating_correlation = db.Column(db.Float, unique=False)
    age_pace_correlation = db.Column(db.Float, unique=False)
    pass_short_long_correlation = db.Column(db.Float, unique=False)


# Create table based on variance of shooting ability
class Variance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    variance = db.Column(db.String, unique=False)
    standard_dev = db.Column(db.String, unique=False)
