import unittest
import string
import random


class TestCase(unittest.TestCase):

    def test1(self):
        num = [4]
        for i in range(0,13):
            num.append(random.randint(0, 9))
        num.append(gen_check_bit(num))

        string_num = ''.join(str(n) for n in num)
        credit_card_validator(string_num)


def gen_check_bit(num):
    modified_num = []

    # double odd indexes
    for digit in num:
        if digit % 2 != 0:
            new_digit = digit * 2

            # sum digits of new values
            if new_digit >= 10:
                new_digit = 1 + (new_digit - 10)
            modified_num.append(new_digit)
        else:
            modified_num.append(digit)

    # sum all digits
    digit_sum = sum(modified_num)

    # calculate check digit
    check_bit = ((10 - digit_sum % 10) % 10)

    return check_bit
