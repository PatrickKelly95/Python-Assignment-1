# Program Name: reading_from_csv
# Purpose: Open and read the contents of the csv file

import logging

filename = "FIFA19 - Ultimate Team players.csv"


def read_csv_file():
    """
    Open and read contents of a csv file

    Returns
    -------
    list
        The content of a csv file
    """

    try:
        # Open csv file
        with open(filename, newline="", encoding="utf8") as csv_file:
            # Ignore headers
            csv_file.readline()
            # Pass each line of the csv file as a list object
            file_content = csv_file.readlines()

    except FileNotFoundError as fnf_error:
        logging.exception(f'FileNotFound Exception occurred: {fnf_error}')
    except IsADirectoryError as dir_error:
        logging.exception(f'IsADirectoryError Exception occurred: {dir_error}')
    except PermissionError as permission_error:
        logging.exception(f'PermissionError Exception occurred: {permission_error}')

    else:
        return file_content
    finally:
        logging.info(f'Finished reading from: {filename}')
