import unittest

from prime import is_prime

class Test(unittest.TestCase):

  def test_1(self):
    """Check that 1 is not prime"""
    self.assertFalse(is_prime(1))

  def test_2(self):
    """Check that 2 is prime"""
    self.assertTrue(is_prime(2))

  def test_8(self):
    """Check that 8 is not prime"""
    self.assertFalse(is_prime(8))

  def test_9(self):
    """Check that 9 is not prime"""
    self.assertFalse(is_prime(9))

  def test_15(self):
    """Check that 15 is not prime"""
    self.assertFalse(is_prime(15))

  def test_25(self):
    """Check that 25 is not prime"""
    self.assertFalse(is_prime(25))

  def test_97(self):
    """Check that 97 is prime"""
    self.assertTrue(is_prime(97))

if __name__ == "__main__":
  unittest.main()