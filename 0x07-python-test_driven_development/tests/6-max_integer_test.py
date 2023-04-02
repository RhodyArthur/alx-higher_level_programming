#!/usr/bin/python3
"""Unittest module for max integer in a list"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """max_integer unittest class"""
    def test_module_docstring(self):
        """Tests for module docsting"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Test for function docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)
    
    def test_empty_list(self):
        """Test for empty list"""
        a = []
        self.assertIsNone(max_integer(a))
    
    def test_no_args(self):
        """Test for no arguments"""
        self.assertIsNone(max_integer())
    
    def test_one_item(self):
        """Test for one item in list"""
        b = [2]
        self.assertEqual(max_integer(b), 2)
        
    def test_max_at_beginning(self):
        """Test for max_integer at first index"""
        c = [50, 40, 30, 20, 10]
        self.assertEqual(max_integer(c), 50)
        
    def test_max_inbetween(self):
        """Test for max_integer in the middle"""
        d = [10, 20, 40, 30, 8]
        self.assertEqual(max_integer(d), 40)
        
    def test_max_at_end(self):
        """Test for max_integer at last index"""
        e = [1, 3, 5, 7, 9]
        self.assertEqual(max_integer(e), 9)
        
    def test_for_negative(self):
        """Test for negative value in list"""
        g = [2, 8, -4, 1, 3]
        self.assertEqual(max_integer(g), 8)
        
    def test_all_negative(self):
        """Test for max_integer in all negative list"""
        n = [-1, -2, -5, -4, -7]
        self.assertEqual(max_integer(n), -1)
        
    def test_none(self):
        """Test for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Test for non-int type in list"""
        t = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(t)

if __name__ == "__main__":
    unittest.main()
