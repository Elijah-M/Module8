import unittest
from more_fun_with_collections.assign_average import switch_average


class TestSwitch(unittest.TestCase):
    def test_switch_average_return_value_A(self):
        self.assertEqual(switch_average('A'), 1)

    def test_switch_average_return_value_BCDE(self):
        self.assertEqual(switch_average('B'), 2)
        self.assertEqual(switch_average('C'), 3)
        self.assertEqual(switch_average('D'), 4)
        self.assertEqual(switch_average('E'), 5)

    def test_switch_average_non_key(self):
        self.assertRaises(switch_average())


if __name__ == '__main__':
    unittest.self
