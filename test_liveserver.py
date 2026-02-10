# test_liveserver.py
"""
Tests for LiveServer module.
"""

import unittest
from liveserver import LiveServer

class TestLiveServer(unittest.TestCase):
    """Test cases for LiveServer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LiveServer()
        self.assertIsInstance(instance, LiveServer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LiveServer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
