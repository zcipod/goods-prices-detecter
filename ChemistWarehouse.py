def findRecord(data, currentIndex, price):
    res = {}
    name = data[currentIndex - 1]
    quantity = data[currentIndex - 2]
    price = float(price.group(1)) / int(quantity)
    res['name'] = name
    res['price'] = float(price)
    res['unit'] = 'PCS'
    return res
