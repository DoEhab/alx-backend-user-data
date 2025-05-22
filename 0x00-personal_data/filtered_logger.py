#!/usr/bin/env python3
"""
function filter_datum
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    filter data
    :return: message with redacted data
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
