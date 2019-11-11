import unittest
import onplo.read


class TestExampleOutput(unittest.TestCase):
    """
    Unit tests for provided input/output examples.
    """

    def test_1(self):
        actual, expected = onplo.read.get("a p/1"), "p(a)"
        self.assertEqual(expected, actual)

    def test_2(self):
        # actual, expected = onplo.read.get("<input>"), "<output>"
        # self.assertEqual(expected, actual)
        pass


if __name__ == '__main__':
    unittest.main()
