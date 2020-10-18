from unittest import TestCase
import WriteToMongoDB


class Test(TestCase):
    def test_insertOneRecord(self):
        data = {"name": "NESCAFE DOLCE GUSTO 186GRAM", "price": "8.50"}
        id = WriteToMongoDB.insertOneRecord(data)
        try:
            db = WriteToMongoDB.Connect.get_connection().pricesOfProducts
            results = db.model.find({"_id": id}, {"_id": 0})
            self.assertEqual(data["name"], results[0]["name"])
            self.assertEqual(data["price"], results[0]["price"])
        except:
            self.fail()

    def test_insertManyRecords(self):
        data = [
            {"name": "NESCAFE DOLCE GUSTO 186GRAM", "price": "8.50"},
            {"name": "THE JUICE LAB SMOOTH 350ML", "price": "3.10"}
        ]
        WriteToMongoDB.insertManyRecords(data)
        try:
            db = WriteToMongoDB.Connect.get_connection().pricesOfProducts
            for record in data:
                results = db.model.find({"_id": record["_id"]}, {"_id": 0})
                self.assertEqual(record["name"], results[0]["name"])
                self.assertEqual(record["price"], results[0]["price"])
        except:
            self.fail()
