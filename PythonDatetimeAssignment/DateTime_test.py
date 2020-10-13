import unittest
from PythonDatetimeAssignment.DateTime import half_birthday
from datetime import timedelta
import datetime


class TestDateTime(unittest.TestCase):
    def test_half_birthday(self):
        self.assertEqual(half_birthday(2020, 4, 29), datetime.date(2020, 10, 28))


if __name__ == '__main__':
    unittest.self
