import unittest
from answer import Main as answer

class TestProblemMultiples(unittest.TestCase):
    def test_multiple1(self):
        self.assertFalse(answer().isMultiple(1))
    
    def test_multiple2(self):
        self.assertFalse(answer().isMultiple(2))
        
    def test_multiple3(self):
        self.assertTrue(answer().isMultiple(3))
        
    def test_multiple4(self):
        self.assertFalse(answer().isMultiple(4))
        
    def test_multiple5(self):
        self.assertTrue(answer().isMultiple(5))
        
    def test_multiple9(self):
        self.assertTrue(answer().isMultiple(9))
        
    def test_multiple10(self):
        self.assertTrue(answer().isMultiple(10))
        
    def test_multiple15(self):
        self.assertTrue(answer().isMultiple(15))
        
        
class TestProblemSequences(unittest.TestCase):
    def test_sequence1(self):
        self.assertListEqual(answer().inRange(10), [3,5,6,9,10])
        
    def test_sequence2(self):
        self.assertListEqual(answer().inRange(15), [3,5,6,9,10,12,15])
        
    def test_sequence3(self):
        self.assertListEqual(answer().inRange(5, 10), [5,6,9,10])
    
    def test_sequence4(self):
        self.assertListEqual(answer().inRange(10, 20), [10,12,15,18,20])
        
    def test_sequence5(self):
        self.assertListEqual(answer().inRange(10, 9), [])
        
class TestProblemAnswer(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(answer().solve(), 233168)
		
if __name__ == '__main__':
    unittest.main()