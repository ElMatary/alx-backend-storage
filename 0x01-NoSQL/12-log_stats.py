#!/usr/bin/env python3
"""
Module contains main fun
"""

from pymongo import MongoClient


def main():
    """
    script that provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient("mongodb://localhost:27017")
    db = client.logs
    collection = db.nginx
    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
    print("\tmethod GET: {}".format(collection.
                                    count_documents({"method": "GET"})))
    print("\tmethod POST: {}".format(collection.
                                     count_documents({"method": "POST"})))
    print("\tmethod PUT: {}".format(collection.
                                    count_documents({"method": "PUT"})))
    print("\tmethod PATCH: {}".format(collection.
                                      count_documents({"method": "PATCH"})))
    print("\tmethod DELETE: {}".format(collection.
                                       count_documents({"method": "DELETE"})))
    print("{} status check".format(collection.
                                   count_documents({
                                                    "method": "GET",
                                                    "path": "/status"
                                                    })))


if __name__ == "__main__":
    main()
