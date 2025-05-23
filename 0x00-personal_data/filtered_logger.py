#!/usr/bin/env python3
"""
function filter_datum
"""
import re
from typing import List

import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        format and redact
        :return: redacted message
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def get_logger(self) -> logging.Logger:
    """
    :return: logger
    """
    logs = logging.getLogger("user_data")
    logs.setLevel(logging.INFO)
    logs.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logs.addHandler(handler)
    return logs


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    filter data
    :return: message with redacted data
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
