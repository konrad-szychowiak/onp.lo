import sys
import unittest

from onplo import type
from onplo import conf


class TestTermChecks(unittest.TestCase):

    def test_type_predicate(self):
        actual = type.rematch("predicate", "p/1")
        self.assertTrue(actual)

    def test_type_function(self):
        actual = type.rematch("function", "f/1")
        self.assertTrue(actual)

    def test_type_variable(self):
        actual = type.rematch("variable", "X")
        self.assertTrue(actual)

    def test_type_constant(self):
        actual = type.rematch("constant", "c")
        self.assertTrue(actual)


class TestOperandChecks(unittest.TestCase):

    def test_type_quantifier(self):
        actual = type.match("quantifier", "FORALL")
        self.assertTrue(actual)

    def test_type_single(self):
        actual = type.match("single", "NOT")
        self.assertTrue(actual)

    def test_type_double(self):
        actual = type.match("double", "XOR")
        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
