import unittest
import random
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):

    def test1(self):
        # Visa prefix
        # 16 digit
        for test in range(10000):
            credit_card_validator(random.randint(4000000000000000, 4999999999999999))

    def test2(self):
        # AmEx prefixes
        # 15 digit
        # 34
        for test in range(10000):
            credit_card_validator(random.randint(340000000000000, 349999999999999))

        # 37
        for test in range(10000):
            credit_card_validator(random.randint(370000000000000, 379999999999999))

    def test3(self):
        # MasterCard prefixes
        # 16 digit
        # 51-55
        for test in range(10000):
            credit_card_validator(random.randint(5100000000000000, 5599999999999999))

        # 2221-2720
        for test in range(10000):
            credit_card_validator(random.randint(2221000000000000, 2720999999999999))


if __name__ == '__main__':
    unittest.main()
