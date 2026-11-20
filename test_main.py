import unittest

from main import greet


class GreetTests(unittest.TestCase):
    def test_greet_with_name(self) -> None:
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_greet_defaults_to_world(self) -> None:
        self.assertEqual(greet(""), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
