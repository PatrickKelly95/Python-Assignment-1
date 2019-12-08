# Program Name: request_data_from_kaggle
# Purpose: Check if csv file exists otherwise download it from kaggle

import kaggle
import requests
import logging
from pathlib import Path

site = 'https://www.kaggle.com/'


def request_csv_file():
    """
    Check connection to site where dataset is present

    """

    try:
        logging.info(f'Testing connection to {site}')
        # Send GET request to site set above
        requests.get(site)
    except requests.ConnectionError as conn_error:
        logging.exception(f'ConnectionError: {conn_error}')
    else:
        logging.info(f'Connection to {site} is successful')
        check_if_csv_file_exists()


def check_if_csv_file_exists():
    """
    Check if the csv file exists otherwise authorize and download it

    """

    path_to_csv_file = Path("FIFA19 - Ultimate Team player prices.csv")

    if path_to_csv_file.exists():
        logging.info('File already exists')
    else:
        logging.info('Authenticating and downloading csv file')

        # Verifying authentication to kaggle using an API token.
        kaggle.api.authenticate()

        # Downloading dataset from kaggle
        kaggle.api.dataset_download_files('stefanoleone992/fifa-19-fifa-ultimate-team', path=None, unzip=True)
