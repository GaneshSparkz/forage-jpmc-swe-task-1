import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            actual_result = getDataPoint(quote)
            required_result = quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
            self.assertEqual(actual_result, required_result)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            actual_result = getDataPoint(quote)
            required_result = quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
            self.assertEqual(actual_result, required_result)


    """ ------------ Add more unit tests ------------ """
    def test_getRatio_calculateRatio(self):
        price_a = 121.2
        price_b = 121.68
        actual_ratio = getRatio(price_a, price_b)
        required_ratio = price_a / price_b
        self.assertEqual(actual_ratio, required_ratio)

    def test_getRatio_calculateRatioPriceBIsZero(self):
        price_a = 121.2
        price_b = 0
        actual_ratio = getRatio(price_a, price_b)
        required_ratio = None
        self.assertEqual(actual_ratio, required_ratio)


if __name__ == '__main__':
    unittest.main()
