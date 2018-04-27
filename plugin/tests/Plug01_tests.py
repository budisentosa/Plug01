import unittest
import Plug01 as sut


@unittest.skip("Don't forget to test!")
class Plug01Tests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.Plug01_example()
        self.assertEqual("Happy Hacking", result)
