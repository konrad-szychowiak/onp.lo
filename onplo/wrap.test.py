import sys
import unittest
import onplo.wrap


class TestWrapers(unittest.TestCase):

    def test_general_wraper(self):
        """Check if the general `formula` wraper doesn't return `None`"""

        actual = utils.wrap.formula("TEST")
        self.assertIsNotNone(actual, self.__doc__)

    def test_wrap_predicate(self):
        """Tests the `predicate` wrapper output"""

        actual = utils.wrap.predicate("p", "X")
        expected = "p(X)"

        self.assertEqual(expected, actual, self.__doc__)

    def test_wrap_single(self):
        """Tests the `single`-argument operator wrapper output"""

        actual = utils.wrap.predicate("NOT", "p(X)")
        expected = "NOT X"

        self.assertEqual(expected, actual, self.__doc__)


if __name__ == '__main__':
    unittest.main()
