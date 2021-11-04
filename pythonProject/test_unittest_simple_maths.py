import unittest


def add(a, b=3):
    if b == -0:
        raise ValueError("Number Not Acceptable")
    return a + b


def multiply(a=6, b=4):
    return a * b


class AddTest(unittest.TestCase):
    a = 7
    b = 64

    # ARRANGE
    def setUp(self):
        print("Setting-Up Test")
        self.a = 7
        self.b = 64

    def tearDown(self):
        self.a = 0
        self.b = 0
        print("Tearing-Down After Each Test")

    # ACT
    def test_add(self):
        print("Test Is Called")
        result = add(self.a, self.b)

        # ASSERT
        self.assertRaises(ValueError, add, 5, -0)
        with self.assertRaises(ValueError):
            add(5, -0)
        self.assertEqual(71, result, msg="Assertion Failure")

    def test_multiply(self):
        next_result = multiply()

        # ASSERT
        self.assertEqual(24, next_result)


if __name__ == "__main__":
    unittest.main()
