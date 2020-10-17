import re


def findTwoRowRecord(data, currentIndex):
    res = {}
    # coles gives the quantity after prices when buy the same product for more than 1 time
    if 'EACH' in data[currentIndex + 1]:
        price = re.search('\\$([0-9]+\\.[0-9]{2})', data[currentIndex + 1])
        name = re.match('[^a-zA-Z0-9]*(.*)', data[currentIndex - 1])
        res['name'] = name.group(1)
        res['price'] = float(price.group(1))
        res['unit'] = 'PCS'

    # coles gives the weight after prices when the product is sold by weight
    else:
        price = re.search('\\$([0-9]+\\.[0-9]{2})\\/(.*)$', data[currentIndex + 1])
        name = re.match('[^a-zA-Z0-9]*(.*)', data[currentIndex - 1])
        res['name'] = name.group(1)
        res['price'] = float(price.group(1))
        res['unit'] = price.group(2)
    return res
