from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result,ResultByKey
from flask import config,current_app


class dbservice():
    def connection(self):
        client = Cloudant(current_app.config['DB_USERNAME'], current_app.config["DB_PASSWORD"], url=current_app.config["DB_URL"])
        try:
            client.connect()
            print("Connection succesfull")
        except:
            print("Connection failed")
        return client


c = dbservice()


class crud():

    def insert_feature(self, candict, database_name):
        c = dbservice()
        client = c.connection()
        my_database = client[database_name]
        try:
            my_document = my_database.create_document(candict)
            my_document.save()
            print("User inserted")
        except:
            print("Insertion failed")
        client.disconnect()

    def search_feature(self, key, database_name):
        c = dbservice()
        client = c.connection()
        my_database = client[database_name]
        result = Result(my_database.all_docs, include_docs=True)
        my_document = result[ResultByKey(key)]
        if len(my_document)!=0:
            for key, value in my_document[0].items():
                if key == 'doc':
                    doc = value
            return doc
        else:
            return my_document
        client.disconnect()
