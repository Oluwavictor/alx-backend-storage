#!/usr/bin/env python3
"""
Task 9: a Python function
"""


def insert_school(mongo_collection, **kwargs):
    """
     inserts a new document in a
      collection based on kwargs
    """
    new_docs = mongo_collection.insert_one(kwargs)
    return new_docs.inserted_id
