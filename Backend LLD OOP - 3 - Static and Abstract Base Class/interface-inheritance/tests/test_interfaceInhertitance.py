import unittest
from config.interface_inheritance import C,I,I1,I2

class TestInterfaces(unittest.TestCase):
    def test_interface_inheritance(self):
        obj = C()
        self.assertTrue(isinstance(obj, I1))
        self.assertTrue(isinstance(obj, I2))
        self.assertTrue(isinstance(obj, I))

        self.assertTrue(hasattr(obj, 'fun1'))
        self.assertTrue(hasattr(obj, 'fun2'))
        self.assertTrue(hasattr(obj, 'fun'))

        obj.fun1()
        obj.fun2()
        obj.fun()

if __name__ == '__main__':
    unittest.main()