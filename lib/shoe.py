import unittest
import io
import sys

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size  # This will use the setter

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            raise ValueError("size must be an integer")
        self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

class TestShoe(unittest.TestCase):
    def test_requires_int_size(self):
        '''prints "size must be an integer" if size is not an integer.'''
        stan_smith = Shoe("Adidas", 9)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            stan_smith.size = "not an integer"
        except ValueError:
            pass
        finally:
            sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "size must be an integer\n")

    def test_can_cobble(self):
        '''says that the shoe has been repaired.'''
        stan_smith = Shoe("Adidas", 9)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.cobble()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "Your shoe is as good as new!\n")

    def test_cobble_makes_new(self):
        '''creates an attribute on the instance called 'condition' and set equal to 'New' after repair.'''
        stan_smith = Shoe("Adidas", 9)
        stan_smith.cobble()
        self.assertEqual(stan_smith.condition, "New")

if __name__ == '__main__':
    unittest.main()
