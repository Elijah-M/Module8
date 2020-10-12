import unittest
from more_fun_with_collections.set_membership import in_set


class Test_set(unittest.TestCase):
    def test_in_set_true(self):
        self.assertTrue(in_set(25))

    #  I commented out the 2nd test because it has the same function name
    #  as the 1st function, which means the definition will always change
    #  to the 2nd version (the false version).  I think you meant to call
    #  the second test - test_in_set_false - but just in case I still
    #  named it test_in_set_true


    #def test_in_set_true(self):
    #    self.assertFalse(in_set(25))


if __name__ == '__main__':
    unittest.self
