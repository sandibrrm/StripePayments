# test_stripepayments.py
"""
Tests for StripePayments module.
"""

import unittest
from stripepayments import StripePayments

class TestStripePayments(unittest.TestCase):
    """Test cases for StripePayments class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StripePayments()
        self.assertIsInstance(instance, StripePayments)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StripePayments()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
