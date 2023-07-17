#!/usr/bin/env python3
"""
Task 8: a Python function
"""


def list_all(mongo_collection):
    """
    lists all documents in a collection

    """
    return mongo_collection.find()
