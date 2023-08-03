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
        

class TestCheck(unittest.TestCase):
    
    def test_check1(self):
        x = hamming.Hamming(7, 4)
        self.assertEqual(x.check_hamming('0110011'), ('0110011', 0))
        
    def test_check2(self):
        x = hamming.Hamming(7, 4)
        self.assertEqual(x.check_hamming('0100011'), ('0110011', 3))
        
    def test_check3(self):
        x = hamming.Hamming(11, 7)
        self.assertEqual(x.check_hamming('10001100101'), ('10001100101', 0))

    def test_check4(self):
        x = hamming.Hamming(11, 7)
        self.assertEqual(x.check_hamming('10000100101'), ('10001100101', 5))
        
    def test_check5(self):
        x = hamming.Hamming(7, 4)
        self.assertEqual(x.check_hamming('0000011'), ('1000011', 1))
        
    def test_check6(self):
        x = hamming.Hamming(7, 4)
        self.assertEqual(x.check_hamming('1100011'), ('1000011', 2))
