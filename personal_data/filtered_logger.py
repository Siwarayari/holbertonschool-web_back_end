#!/usr/bin/env python3
"""function called filter_datum that returns the log message obfuscated
The function should use a regex to replace occurrences of certain field values.
filter_datum should be less than 5 lines long and use re.sub
toperform the substitution with a single regex"""


from typing import List
import re
import logging
import mysql.connector
import os

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """function called filter_datum that returns the log message obfuscated
The function should use a regex to replace occurrences of certain field values.
filter_datum should be less than 5 lines long and use re.sub
toperform the substitution with a single regex"""
    for i in fields:
        message = re.sub(f'{i}=.*?{separator}',
                         f'{i}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """init"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Implement the format method to filter
        values in incoming log records using
        filter_datum. Values for fields in fields should be """
        msg = super().format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """The logger should be named "user_data" and only
    log up to logging.INFO level. It should not propagate
    messages to other loggers. It should have a StreamHandler
    with RedactingFormatter as formatter"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter)
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Implement a get_db function that
    returns a connector to the database
    (mysq.lconnector.connection.MySQLConnection object"""
    cnx = mysql.connector.connect(host=os.getenv("PERSONAL_DATA_DB_HOST"),
                                  user=os.getenv("PERSONAL_DATA_DB_USERNAME"),
                                  password=os.getenv
                                  ("PERSONAL_DATA_DB_PASSWORD"),
                                  database=os.getenv("PERSONAL_DATA_DB_NAME"))
    return cnx
