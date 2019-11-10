import unittest
import onpl.read as read


class TestOnp(unittest.TestCase):
    """
    Unit tests for provided input/output examples.
    """

    def test_1(self):
        actual = read.raw("a p/1".split())
        expected = "p(a)"

        self.assertEqual(expected, actual)

    def test_2(self):
        # actual = utils.test.init("a p/1".split())
        # expected = "p(a)"
        #
        # self.assertEqual(expected, actual)
        pass


if __name__ == '__main__':
    unittest.main()
