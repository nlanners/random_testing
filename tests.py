import unittest
import string
import random
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):

    def test1(self):
        # for test in range(1000):
        #     num = [4]
        #     for i in range(0, 15):
        #         num.append(random.randint(0, 9))
        #     #num.append(gen_check_bit(num))
        #
        #     string_num = ''.join(str(n) for n in num)
        #     credit_card_validator(string_num)

        for test in range(1000000):
            credit_card_validator(random.randint(1000000000000000, 9999999999999999))


def gen_check_bit(num):
    modified_num = []

    # double odd indexes
    for index in range(len(num)):
        if len(num) % 2 == 0:
            if index % 2 != 0:
                new_digit = num[index] * 2

                # sum digits of new values
                if new_digit >= 10:
                    new_digit = 1 + (new_digit - 10)
                modified_num.append(new_digit)
            else:
                modified_num.append(num[index])
        else:
            if index % 2 == 0:
                new_digit = num[index] * 2

                # sum digits of new values
                if new_digit >= 10:
                    new_digit = 1 + (new_digit - 10)
                modified_num.append(new_digit)
            else:
                modified_num.append(num[index])

    # sum all digits
    digit_sum = sum(modified_num)

    # calculate check digit
    check_bit = ((10 - (digit_sum % 10)) % 10)

    return check_bit


if __name__ == '__main__':
    unittest.main()
