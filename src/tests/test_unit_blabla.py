import unittest
from oxrse_unit_conv.units import bla, blabla


class TestBlaBla(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(blabla.si_unit.matches(bla))

    def test_basic_conversion(self):
        self.assertEqual(blabla.to_si(1), 2)
        self.assertEqual(blabla.to_unit(10, blabla), 10)


if __name__ == '__main__':
    unittest.main()
