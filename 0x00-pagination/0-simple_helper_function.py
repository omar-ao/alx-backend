#!/usr/bin/env python3
"""
This is module contains one function
"""


def index_range(page, page_size):
    """Returns a tuple containing a start index and end index"""
    total = page * page_size
    return ((total - page_size), total)
