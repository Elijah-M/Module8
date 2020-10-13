import unittest
from PythonDatetimeAssignment.DateTime import half_birthday
from datetime import timedelta
import datetime


class TestDateTime(unittest.TestCase):
    def test_half_birthday(self):
        b_day = datetime.date(2020, 4, 29)
        half_b_day = b_day + timedelta(days=182.5)
        self.assertEqual(half_birthday(b_day), half_b_day)


if __name__ == '__main__':
    unittest.self
