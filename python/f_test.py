import unittest
import test 

class Test(unittest.TestCase):
  def test_something(self):
    a = 0 
    self.assertEqual(test.add(a), '0')
    a = 2
    self.assertEqual(test.add(a), "Số dương")
    a = -1
    self.assertEqual(test.add(a), "Số âm")
    
if __name__ == '__main__' :
  unittest.main(verbosity=2);
