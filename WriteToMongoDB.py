import pymongo


class Connect(object):
    @staticmethod
    def get_connection():
        dbUri = "mongodb+srv://zcipod:zhao7895123@cocktailinformation.8e6ap.mongodb.net/pricesOfProducts?retryWrites=true&w=majority"
        return pymongo.MongoClient(dbUri, ssl=True, ssl_cert_reqs='CERT_NONE')


def insertOneRecord(record):
    try:
        db = Connect.get_connection().pricesOfProducts
        obj = db.model.insert_one(record)
        print('Successfully saved record: ', obj.inserted_id)
        return obj.inserted_id
    except pymongo.errors.ConfigurationError as e:
        print("Error while save record to MongoDB: ", e)


def insertManyRecords(records):
    try:
        db = Connect.get_connection().pricesOfProducts
        objs = db.model.insert_many(records)
        print('\nSuccessfully saved records: ', objs.inserted_ids)
        return objs.inserted_ids
    except pymongo.errors.ConfigurationError as e:
        print("Error while save records to MongoDB: ", e)

