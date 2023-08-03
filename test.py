import unittest
import hamming

class TestEncode(unittest.TestCase):
    def test_encode1(self):
        x = hamming.Hamming(7, 4)
        self.assertEqual(x.encode('1011'), '0110011')
        
    def test_encode2(self):
        x = hamming.Hamming(7, 4)
        self.assertEqual(x.encode('1101'), '1010101')
        
    def test_encode3(self):
        x = hamming.Hamming(11, 7)
        self.assertEqual(x.encode('0110101'), '10001100101')
        
    

