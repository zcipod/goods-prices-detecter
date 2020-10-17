import re


def findTwoRowRecord(data, currentIndex):
    res = {}
    # Woolworths gives the quantity between names and prices when buy the same product for more than 1 time
    if 'each' in data[currentIndex - 1]:
        price = re.search('\\$([0-9]+\\.[0-9]{2})', data[currentIndex - 1])
        name = re.match('[^a-zA-Z0-9]*(.*)', data[currentIndex - 2])
        res['name'] = name.group(1)
        res['price'] = float(price.group(1))
        res['unit'] = 'PCS'

    # Woolworths gives the weight between names and prices when the product is sold by weight
    else:
        price = re.match('\\$([0-9]+\\.[0-9]{2})/(.*)]', data[currentIndex - 1])
        name = re.match('[^a-zA-Z0-9]*(.*)', data[currentIndex - 2])
        res['name'] = name.group(1)
        res['price'] = float(price.group(1))
        res['unit'] = price.group(2)
    return res
