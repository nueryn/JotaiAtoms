# test_jotaiatoms.py
"""
Tests for JotaiAtoms module.
"""

import unittest
from jotaiatoms import JotaiAtoms

class TestJotaiAtoms(unittest.TestCase):
    """Test cases for JotaiAtoms class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JotaiAtoms()
        self.assertIsInstance(instance, JotaiAtoms)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JotaiAtoms()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
