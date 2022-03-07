"""
is_valid_phone_number
"""

import re
def is_valid_phone_number(txt):
    return bool(re.match('^\(\d{3}\) \d{3}-\d{4}$', txt))

print(is_valid_phone_number("(123) 456-7890"))
is_valid_phone_number("1111)555 2345")
is_valid_phone_number("098) 123 4567")