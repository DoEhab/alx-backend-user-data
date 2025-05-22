#!/usr/bin/env python3
"""
function filter_datum
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    filter data
    :return: redacted data
    """
    field = "|".join(fields)
    pattern = r'({})=[^{}]*'.format(field, separator)
    result = re.sub(pattern, r'\1=' + redaction, message)
    return result
