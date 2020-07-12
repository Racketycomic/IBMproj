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

    def search_feature(self, key, database_name): #key=languvage, #database_name
        c = dbservice()
        client = c.connection()
        my_database = client[database_name]
        result = Result(my_database.all_docs, include_docs=True)
        my_document = result[ResultByKey(key)]

        for key, value in my_document[0].items():
            if key == 'doc':
                doc = value
        return doc


        if len(my_document) != 0:
            for key, value in my_document[0].items():
                if key == 'doc':
                    doc = value
            return doc
        else:
            return my_document
        client.disconnect()

    def search_and_insert(self, key, database_name, data, flag):
        c = dbservice()
        client = c.connection()
        my_database = client[database_name]
        print('Inside search_and_insert')
        if flag == 'double':
            my_document = my_database[key]
            for i in data.keys():
                if i in my_document.keys():
                    my_document[i].append(data[i])
                else:
                    my_document[i] = [data[i]]
            my_document.save()
        elif flag == 'single':
            my_document = my_database[key]
            for i in data.keys():
                my_document[i] = data[i]
                my_document.save()

        elif flag == 'create':
            my_document = my_database.create_document(data)
            my_document.save()
            print('Inside Create')

        else:
            my_document = my_database[key]
            for i in data.keys():
                if i in my_document.keys():
                    my_document[i].append(data[i])
                else:
                    my_document[i] = [data[i]]
            my_document.save()
        client.disconnect()
