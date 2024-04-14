import logging


class ResponseUtils:

    def check_status_code(expected, actual):
        if expected == actual:
            logging.info(f"Status code {actual} is as expected {expected}")
        else:
            logging.error(f"Status code {actual} is NOT as expected {expected} !")
