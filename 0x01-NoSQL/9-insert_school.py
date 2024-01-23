#!/usr/bin/env python3
""" 9-insert_school """


def insert_school(mongo_collection, **kwargs):
    """ function that inserts a new document in a collection based on kwargs """
    docs = mongo_collection.insert_one(kwargs)
    return docs.inserted_id
