#!/usr/bin/env python3
"""func that changes all topics of a school document based on the name"""
import pymongo
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """func that changes all topics of a school document based on the name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
