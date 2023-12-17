#!/usr/bin/env python3
"""Python function that lists all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    """Python function that lists all documents in a collection"""
    alldocuments = mongo_collection.find()
    if not alldocuments:
        return []
    else:
        return alldocuments
