from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result,ResultByKey
from flask import config,current_app


class dbservice():
    def connection(self):
        client = Cloudant(current_app.config['USERNAME'], current_app.config["PASSWORD"], url=current_app.config["URL"])
        try:
            client.connect()
            print("Connection succesfull")
        except:
            print("Connection failed")
        return client


c = dbservice()


class crud():

    def insert_feature(self, args):
        client = c.connection()
        database_name = "candidate_features"
        my_database = client[database_name]

        try:
            my_document = my_database.create_document(args)
            print("User inserted")
        except:
            print("Insertion failed")

    def search_feature(self,args):

        client=c.connection()
        database_name = "candidate_features"
        my_database = client[database_name]
        my_document = my_database[args]
