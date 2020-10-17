from unittest import TestCase
from Coles import findTwoRowRecord


class Test(TestCase):
    def test_findTwoRowRecordWithQuantity(self):
        dataWithQuantity = [
            "COLES WHITE SUGAR 1KG",
            "2.00",
            "2 @ $1.00 EACH",
        ]
        result = findTwoRowRecord(dataWithQuantity, 1)
        expectResult = {
            'name': "COLES WHITE SUGAR 1KG",
            'price': 1.0,
            'unit': 'PCS'
        }
        self.assertEqual(expectResult, result, "Error in find record with quantity in Coles")

    def test_findTwoRowRecordWithWeight(self):
        dataWithWeight = [
            "CARROTS PERKG",
            "0.59",
            "0.266 kg NET @ $2.20/kg",
        ]
        result = findTwoRowRecord(dataWithWeight, 1)
        expectResult = {
            'name': "CARROTS PERKG",
            'price': 2.2,
            'unit': 'kg'
        }
        self.assertEqual(expectResult, result, "Error in find record with weight in Coles")

