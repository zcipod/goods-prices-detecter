import re
import Woolies
import Coles
import Kmart
import ChemistWarehouse
from data import DATA


def findOneRowRecord(data, currentIndex, price):
    res = {}
    name = re.match('[^a-zA-Z0-9]*(.*)', data[currentIndex - 1])
    res['name'] = name.group(1)
    res['price'] = float(price.group(1))
    res['unit'] = 'PCS'
    return res


def findPriceOfProducts(data):
    index = 0
    results = []
    while not re.search('total', data[index], re.I):
        findPrice = re.match('\\$?([0-9]+\\.[0-9]{2}$)', data[index])
        if findPrice:
            record = {}
            # Kmart has 13 numbers between products' names and prices
            if re.match('^[0-9]{13}$', data[index - 1]):
                record = Kmart.findRecord(data, index, findPrice)

            elif '$' in data[index + 1]:
                record = Coles.findTwoRowRecord(data, index)

            elif '$' in data[index - 1]:
                record = Woolies.findTwoRowRecord(data, index)

            elif data[index - 2].isdigit():
                record = ChemistWarehouse.findRecord(data, index, findPrice)

            else:
                record = findOneRowRecord(data, index, findPrice)

            results.append(record)
        index += 1
    return results


print(findPriceOfProducts(DATA['Coles']))
