import unittest
from math import pi
from test_my_prog import one_prog

class Test_circle_area(unittest.TestCase):
    def test_area(self):
        self.assertEqual(one_prog.circle_area(3),pi*3**2)
        self.assertEqual(one_prog.circle_area(1), pi * 1 ** 2)
        self.assertEqual(one_prog.circle_area(0), pi * 0 ** 2)
        self.assertEqual(one_prog.circle_area(2.5), pi * 2.5 ** 2)

    def test_value(self):
        self.assertRaises(ValueError,one_prog.circle_area,-1)

    def test_of_type(self):
        self.assertRaises(TypeError,one_prog.circle_area,True)
        self.assertRaises(TypeError, one_prog.circle_area, [1,2,3])
        self.assertRaises(TypeError, one_prog.circle_area, 'True')


