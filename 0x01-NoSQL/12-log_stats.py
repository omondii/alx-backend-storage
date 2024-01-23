#!/usr/bin/env python3
from pymongo import MongoClient

def nginx_log_stats():
    # Connect to the MongoDB server and access the 'logs' database and 'nginx' collection
    client = MongoClient('localhost', 27017)
    db = client['logs']
    collection = db['nginx']

    # Get the total number of logs
    total_logs = collection.count_documents({})

    # Get the number of logs for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}

    # Get the number of logs with method=GET and path=/status
    get_status_count = collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{get_status_count} status check")

# Call the function to print the statistics
nginx_log_stats()
