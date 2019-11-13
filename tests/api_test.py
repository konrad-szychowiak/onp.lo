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
        actual, expected = onplo.read.get("Z Z p/1 EXISTS"), "(EXISTS Z p(Z))"
        self.assertEqual(expected, actual)

    def test_3(self):
        actual, expected = onplo.read.get(
            "Z X X a f/2 p/1 ∃ Y Y Z f/1 p/2 FORALL → FORALL"), "(FORALL Z ((∃ X p(f(X, a))) → (FORALL Y p(Y, f(Z)))))"
        self.assertEqual(expected, actual)

    def test_4(self):
        actual, expected = onplo.read.get(
            "Z Y X X b c q/3 Z Y f/1 p/2 ~ & EXISTS FORALL EXISTS"), "(EXISTS Z (FORALL Y (EXISTS X (q(X, b, c) & (~ p(Z, f(Y)))))))"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    print(TestExampleOutput.__doc__)
    unittest.main()
