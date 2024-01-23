#!/usr/bin/env python3
""" 11-schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    """ function that returns the list of school having a specific topic """
    docs = mongo_collection.find({"topics": topic})
    docs_list = [school for school in docs]
    return docs_list
