import unittest
import sys
import os

from miscellanea.tdd_tests.main import nitro_salt

# sys.path.append('M:/Programs/workspace/programming/python/miscellanea/tdd_tests')
# from main import *


class TestNitroSalt(unittest.TestCase):
    def test_nitro_salt_returns_mass(self):
        self.assertEqual(nitro_salt(1000), 10)
        self.assertEqual(nitro_salt(1500), 15)
        self.assertEqual(nitro_salt(800), 8)

    def test_nitro_salt_returns_integer(self):
        self.assertIsInstance(nitro_salt(1000), int)

    def test_nitro_salt_receives_string_returns_integer(self):
        self.assertEqual(nitro_salt('1000'), 10)

    def test_nitro_salt_receives_alpha_string_returns_zero(self):
        self.assertEqual(nitro_salt('asdadad'), 0)




if __name__ == '__main__':
    unittest.main()
