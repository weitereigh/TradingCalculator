# test_tradingcalculator.py
"""
Tests for TradingCalculator module.
"""

import unittest
from tradingcalculator import TradingCalculator

class TestTradingCalculator(unittest.TestCase):
    """Test cases for TradingCalculator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TradingCalculator()
        self.assertIsInstance(instance, TradingCalculator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TradingCalculator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
