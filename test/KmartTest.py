from unittest import TestCase
from Kmart import findRecord
import re


class Test(TestCase):
    def test_findRecord(self):
        data = [
            "%BRAID BUCKET HAT",
            "9341107487754",
            "5.00",
        ]
        findPrice = re.match('\\$?([0-9]+\\.[0-9]{2}$)', data[2])
        result = findRecord(data, 2, findPrice)
        expectResult = {
            'name': "BRAID BUCKET HAT",
            'price': 5.0,
            'unit': 'PCS'
        }
        self.assertEqual(expectResult, result, "Error in find record in Kmart")

