import unittest
from dodaj import dodaj
class TestDodaj(unittest.TestCase):

	def test_dodaj_liczby_dodatnie(self):
		self.assertEqual(dodaj(2, 3), 5)
		self.assertEqual(dodaj(6, 2), 8)

	def test_dodaj_liczby_ujemne(self):
		self.assertEqual(dodaj(-2, -2), -4)
		self.assertEqual(dodaj(-3, -4), -7)

	def test_dodaj_liczby_zmiennoprzecinkowe(self):
		self.assertEqual(dodaj(1.1, 1.2), 2.3)
		self.assertEqual(dodaj(-3.3, 3,3), (0,0)

	def test_dodaj_zera(self):
		self.assertEqual(dodaj(0, 0), 0)
		self.assertEqual(dodaj(0.0, 0.0), 0.0)

if __name__ == '__main__':
	unittest.main()
