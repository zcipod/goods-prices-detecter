from unittest import TestCase
import re
import Main


class Test(TestCase):
    def test_findOneRowRecord(self):
        data = [
            "NESCAFE DOLCE GUSTO 186GRAM",
            "8.50",
        ]
        findPrice = re.match('\\$?([0-9]+\\.[0-9]{2}$)', data[1])
        result = Main.findOneRowRecord(data, 1, findPrice)
        expectResult = {
            'name': "NESCAFE DOLCE GUSTO 186GRAM",
            'price': 8.5,
            'unit': 'PCS'
        }
        self.assertEqual(expectResult, result, "Error in find one-row record")

    def test_findPriceOfProducts(self):
        data = [
            "Coles Supermarkets Australia Pty Ltd",
            "Tax Invoice ABN: 45 004 189 708",
            "coles",
            "Store: 4813 - CS MACARTHUR SQR NSW", "Store Manager: Mala",
            "Phone:",
            "0246292100",
            "Served By: Adrian",
            "Register: 004",
            "Receipt: 9270",
            "Date:",
            "29/03/2019",
            "Time:",
            "10:08",
            "Description",
            "COLES SUPER TAMPONS 32PACK",
            "4.00",
            "NESCAFE DOLCE GUSTO 186GRAM",
            "8.50",
            "COLES REGULAR TAMPON 40PACK",
            "4.00",
            "% HASK CONDITIONER 355ML",
            "15.00",
            "% HASK SHAMPOO 355ML",
            "15.00",
            "THE JUICE LAB SMOOTH 350ML",
            "3.10",
            "* MAYVERS SPREAD 240GRAM",
            "4.25",
            "* THE JUICE LAB SMOOTH 350ML",
            "3.10",
            "* CREATIVE FROZEN ACAI 400GRAM",
            "6.00",
            "FAMILY SPINACH 280GRAM",
            "5.00",
            "NAVEL ORANGES 5PACK",
            "4.50",
            "GRN SMITH APPLES 1KG 1EACH",
            "5.00",
            "CARROTS PERKG",
            "0.59",
            "0.266 kg NET @ $2.20/kg",
            "BABY BEETROOT 250GRAM",
            "3.00",
            "TOOHEYS NEW CANS 30 PACK",
            "50.00",
            "LEMONS 5PK 1EACH",
            "3.00",
            "CELERY 1EACH",
            "5.90",
            "COLES WHITE SUGAR 1KG",
            "2.00",
            "2 @ $1.00 EACH",
            "Total for 19 items:",
            "$139.94",
            "EFT",
            "$139.94",
            "Coles",
            "NSW AU",
            "29/03/19 10:08",
            "29833035",
            "NN1304",
            "***** 3704",
            "MASTERCARD",
            "CREDIT ACCOUNT",
            "Mastercard",
            "APSN 0001 ATC 0107",
            "A0000000041010",
            "PURCHASE",
            "AUD$ 139.94",
            "RRN 000040927000",
            "(00) APPROVED",
            "AUTH R42139"
        ]
        result = Main.findPriceOfProducts(data)
        expectResult = [{'name': 'COLES SUPER TAMPONS 32PACK', 'price': 4.0, 'unit': 'PCS'}, {'name': 'NESCAFE DOLCE GUSTO 186GRAM', 'price': 8.5, 'unit': 'PCS'}, {'name': 'COLES REGULAR TAMPON 40PACK', 'price': 4.0, 'unit': 'PCS'}, {'name': 'HASK CONDITIONER 355ML', 'price': 15.0, 'unit': 'PCS'}, {'name': 'HASK SHAMPOO 355ML', 'price': 15.0, 'unit': 'PCS'}, {'name': 'THE JUICE LAB SMOOTH 350ML', 'price': 3.1, 'unit': 'PCS'}, {'name': 'MAYVERS SPREAD 240GRAM', 'price': 4.25, 'unit': 'PCS'}, {'name': 'THE JUICE LAB SMOOTH 350ML', 'price': 3.1, 'unit': 'PCS'}, {'name': 'CREATIVE FROZEN ACAI 400GRAM', 'price': 6.0, 'unit': 'PCS'}, {'name': 'FAMILY SPINACH 280GRAM', 'price': 5.0, 'unit': 'PCS'}, {'name': 'NAVEL ORANGES 5PACK', 'price': 4.5, 'unit': 'PCS'}, {'name': 'GRN SMITH APPLES 1KG 1EACH', 'price': 5.0, 'unit': 'PCS'}, {'name': 'CARROTS PERKG', 'price': 2.2, 'unit': 'kg'}, {'name': 'BABY BEETROOT 250GRAM', 'price': 3.0, 'unit': 'PCS'}, {'name': 'TOOHEYS NEW CANS 30 PACK', 'price': 50.0, 'unit': 'PCS'}, {'name': 'LEMONS 5PK 1EACH', 'price': 3.0, 'unit': 'PCS'}, {'name': 'CELERY 1EACH', 'price': 5.9, 'unit': 'PCS'}, {'name': 'COLES WHITE SUGAR 1KG', 'price': 1.0, 'unit': 'PCS'}]
        self.assertEqual(expectResult, result, "Error in find prices of products")
