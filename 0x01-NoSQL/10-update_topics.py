#!/usr/bin/env python3
""" 10-update_topics """


def update_topics(mongo_collection, name, topics):
    """ changes all topics of a school document based on the name """
    docs = mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return docs
