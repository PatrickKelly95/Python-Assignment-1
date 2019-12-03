# Program Name: render_charts
# Purpose: Render specified charts (e.g. bar chart)

import pygal
import logging
import requests
from bs4 import BeautifulSoup


def render_hor_bar_chart(title, values, labels, height):
    """
    Render a horizontal bar chart image

    Parameters
    ----------
    title : str
        A title for the horizontal bar chart

    values : list
        A list of values.

    labels : list
        A list of labels

    height : int
        A height for the horizontal bar chart

    Returns
    -------
    chart
        A base 64 encoded data uri (chart image)
    """

    logging.info('Rendering horizontal bar chart')
    bar_chart = pygal.HorizontalBar(show_legend=False, height=height)
    bar_chart.title = title
    bar_chart.add("", values)
    bar_chart.x_labels = labels
    bar_chart = bar_chart.render_data_uri()

    return bar_chart


def render_bar_chart(title, message, value1, value2, value3):
    """
    Render a bar chart image

    Parameters
    ----------
    title : str
        A title for the horizontal bar chart

    message : str
        A label for the chart

    value1 : int
        A value for the chart

    value2 : int
        A value for the chart

    value3 : int
        A value for the chart

    Returns
    -------
    chart
        A base 64 encoded data uri (chart image)
    """
    logging.info('Rendering bar chart')
    line_chart = pygal.Bar()
    line_chart.title = title
    line_chart.x_labels = ("Ages",)
    line_chart.add('Avg Age', value1)
    line_chart.add('Min Age', value2)
    line_chart.add('Max Age', value3)
    line_chart = line_chart.render_data_uri()

    return line_chart


def render_world_map(title, message, values):
    """
    Render a world map chart image

    Parameters
    ----------
    title : str
        A title for the world map

    message : str
        A label beside world map

    values : list
        A list of country codes

    Returns
    -------
    chart
        A base 64 encoded data uri (chart image)
    """
    logging.info('Rendering world chart')
    wm = pygal.maps.world.World()
    wm.force_uri_protocol = 'http'
    wm.title = title
    wm.add(message, values)
    wm = wm.render_data_uri()

    return wm


def web_scrap_country_codes():
    """
    Web scrap country codes

    Returns
    -------
    dict
        A dictionary with countries and country codes
    """
    site = 'http://www.pygal.org/en/stable/documentation/types/maps/pygal_maps_world.html'

    try:
        logging.info(f'Testing connection to {site}')
        # Send GET request to site set above
        result = requests.get(site)
    except requests.ConnectionError as conn_error:
        logging.exception(f'ConnectionError: {conn_error}')
    else:
        logging.info(f'Connection to {site} is successful')
        # Store page content of website
        src = result.content
        # Parse and process the source using Beautiful Soup
        soup = BeautifulSoup(src, 'html.parser')
        # Accessing specific table content on page
        table = soup.find_all("td")

        list_of_table_values = []
        # Convert each item in the table to a string and append to a list
        for row in table:
            list_of_table_values.append(str(row))

        remove_td_tag = [s.replace('<td>', '').replace('</td>', '') for s in list_of_table_values]

        # Splice "remove_td_tag" list into two seperate lists one for country and one for country_codes
        country = remove_td_tag[1::2]
        country_code = remove_td_tag[::2]

        # Overwriting the old list content with the new content
        country = remove_extra_content(country)
        country_code = remove_extra_content(country_code)

        # Creating a dictionary of the two lists
        country_code_dict = dict(zip(country_code, country))

        return country_code_dict


def remove_extra_content(items):
    """
    Remove continents from list

    Parameters
    ----------
    items : list
        A list of countries or country codes

    Returns
    -------
    list
        A list without the continents present
    """

    logging.info("Removing content from country/country code lists")
    # Removing extra content from each list
    return items[: len(items) - 7]

