import unittest
from more_fun_with_collections.set_membership import in_set


class Test_set(unittest.TestCase):
    def test_in_set_true(self):
        self.assertTrue(in_set(25))

    #  Now I've un-commented out the 2nd test

    def test_in_set_true(self):
        self.assertFalse(in_set(25))


if __name__ == '__main__':
    unittest.self
