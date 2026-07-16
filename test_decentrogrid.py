# test_decentrogrid.py
"""
Tests for DecentroGrid module.
"""

import unittest
from decentrogrid import DecentroGrid

class TestDecentroGrid(unittest.TestCase):
    """Test cases for DecentroGrid class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DecentroGrid()
        self.assertIsInstance(instance, DecentroGrid)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DecentroGrid()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
