# Program Name: country_specific_statistics
# Purpose: Calculate country specific statistics

from stats.player_specific_statistics import get_player_data
from dataset.render_charts import web_scrap_country_codes, render_world_map
import logging


def world_map():
    """
    Processing so only the right country codes are used and renders the world map

    Returns
    -------
    chart
        A base 64 encoded data uri (chart image)
    """
    logging.info("Processing the world map data")
    # Get country data to be processed
    country_code_dict = web_scrap_country_codes()
    list_of_countries = []
    country_codes = []

    # Removing duplciates from the data
    [list_of_countries.append(country) if country not in list_of_countries else '' for country in get_player_data(9)]

    # Sorting list of countries in alphabetical order
    sorted_list_of_countries = sorted(list_of_countries, key=str.lower)

    # Going through the list of sorted countries
    for sorted_country in sorted_list_of_countries:
        # Going through each key and value in the dictionary
        for code, country in country_code_dict.items():
            # If the sorted country is equal to the country in dictionary
            if sorted_country == country:
                # If the country isnt in the new list of country codes
                if code not in country_codes:
                    # Append the country code from the dictionary into the list
                    country_codes.append(code)

    title = "Countries in Fifa 19 Ultimate Team"
    message = "Countries"
    # Render the world map
    world_map_chart = render_world_map(title, message, country_codes)

    return world_map_chart
