#!/usr/bin/env python3
""" Imported module
pymongo
"""


def list_all(mongo_collection):
    """ function that lists all documents in a collection """
    docs = mongo_collection.find()
    return [doc for doc in docs] if docs else []
