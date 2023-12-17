#!/usr/bin/env python3
"""that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection based on kwargs"""
    new = mongo_collection.insert_one(kwargs)
    result = new.inserted_id
    return result
