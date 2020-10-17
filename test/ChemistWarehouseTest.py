from unittest import TestCase
from ChemistWarehouse import findRecord
import re


class Test(TestCase):
    def test_findRecord(self):
        data = [
            "1",
            "APTAMIL PRO/F JNR SUPP 900 NEW",
            "$32.49",
        ]
        findPrice = re.match('\\$?([0-9]+\\.[0-9]{2}$)', data[2])
        result = findRecord(data, 2, findPrice)
        expectResult = {
            'name': "APTAMIL PRO/F JNR SUPP 900 NEW",
            'price': 32.49,
            'unit': 'PCS'
        }
        self.assertEqual(expectResult, result, "Error in find record in ChemistWarehouse")

