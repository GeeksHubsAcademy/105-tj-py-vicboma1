import pytest
import unittest   # The test framework

from kata import apply

class Test_kata(unittest.TestCase):
    
    def test_apply_01(self):
        expected = []
        result = apply([])
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_02(self):
        expected = [1]
        result = apply([1])
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 
    
    def test_apply_03(self):
        expected = [1, 2]
        result = apply([1, 2])
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 
    

    def test_apply_04(self):
        expected = [1, 2]
        result = apply([1, 2, 2])
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_05(self):
        expected = [1, 2]
        result = apply([1, 2, 2, 1])
        for i in range(0,len(result)):
                    assert(expected[i] == result[i])     


    def test_apply_06(self):
        expected = [1, 2]
        result = apply([1, 2, 2, 1])
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 
    

    def test_apply_07(self):
        expected = ["a"]
        result = apply(["a", "a"])
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 
    

    def test_apply_08(self):
        expected = ["a", "b"]
        result = apply([ "a", "a", "b"])
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 
    
    def test_apply_09(self):
        expected = ["a", "b", "c"]
        result = apply(["a", "a", "b", "b", "c", "c"])
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_10(self):
        expected = ["a", "b", "hola"]
        result = apply(["a", "a", "b", "b", "hola"])
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 
    

    def test_apply_11(self):
        expected = ["a", "b", "hola", "ola"]
        result = apply(["a", "a", "b", "b", "hola", "ola"])
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 
    

    def test_apply_12(self):
        expected = ["a", "b", "hola", "ola"]
        result = apply(["a", "a", "b", "b", "hola", "ola", "hola"])
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 
    

    def test_apply_13Null(self):
        expected = None;
        result = apply(None)
        assert(result == expected) 
 

if __name__ == '__main__':
	unittest.main()