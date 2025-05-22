#!/usr/bin/env python3
"""
function filter_datum
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    filter data
    :param fields: private data fields
    :param redaction: redaction letters
    :param message: full message
    :param separator: delimiter
    :return: redacted data
    """
    field = "|".join(fields)
    pattern = r'({})=[^{}]*'.format(field, separator)
    result = re.sub(pattern, r'\1=' + redaction, message)
    return result
