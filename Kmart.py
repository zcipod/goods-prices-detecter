import re


def findRecord(data, currentIndex, price):
    res = {}
    name = re.match('[^a-zA-Z0-9]*(.*)', data[currentIndex - 2])
    res['name'] = name.group(1)
    res['price'] = float(price.group(1))
    res['unit'] = 'PCS'
    return res
