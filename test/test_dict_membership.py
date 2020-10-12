import unittest
from more_fun_with_collections.dict_membership import in_dict


class Test_set(unittest.TestCase):
    def test_in_dict_true(self):
        self.assertTrue(in_dict(3))

    #  The first test will always be ignored because the 2nd test has the
    #  same function name, I think you wanted us to name the 2nd test
    #  test_in_dict_false, that way we could run 2x different tests
    #  simultaneously

    def test_in_dict_true(self):
        self.assertFalse(in_dict(12))


if __name__ == '__main__':
    unittest.self
