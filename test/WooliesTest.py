from unittest import TestCase
from Woolies import findTwoRowRecord


class Test(TestCase):
    def test_findTwoRowRecordWithQuantity(self):
        dataWithQuantity = [
            "^#Locacker Quadratini Wafer Nplitnr 125g",
            "Qty 8 @  $1.25 each",
            "10.00",
        ]
        result = findTwoRowRecord(dataWithQuantity, 2)
        expectResult = {
            'name': "Locacker Quadratini Wafer Nplitnr 125g",
            'price': 1.25,
            'unit': 'PCS'
        }
        self.assertEqual(expectResult, result, "Error in find record with quantity in Woolies")

    def test_findTwoRowRecordWithWeight(self):
        dataWithWeight = [
            "Carrots",
            "0.266 kg NET @ $2.20/kg",
            "0.59",
        ]
        result = findTwoRowRecord(dataWithWeight, 2)
        expectResult = {
            'name': "Carrots",
            'price': 2.2,
            'unit': 'kg'
        }
        self.assertEqual(expectResult, result, "Error in find record with weight in Woolies")

