'''Lab 4 Test Cases - Michael Jolley and Dilpreet Gill - 4/17/2024'''

import unittest
from lab_4_main import construct_set_zm, compute_gcd, test_primality, euclidean_algorithm

class TestZmConstruction(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(construct_set_zm(7), ({0, 1, 2, 3, 4, 5, 6}, {0, 6, 5, 4, 3, 2, 1}, {None, 1, 4, 5, 2, 3, 6}))

    def test_case_2(self):
        self.assertEqual(construct_set_zm(18), (set(range(18)), set(range(17, -1, -1)), {None, 1, None, None, None, 11, None, 13, None, None, None, 5, None, 7, None, None, None, 17}))

    def test_case_3(self):
        self.assertEqual(construct_set_zm(1), ({0}, {0}, {None}))

    def test_case_4(self):
        with self.assertRaises(ValueError):
            construct_set_zm(-5)

if __name__ == '__main__':
    unittest.main()

class TestGCDComputation(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(compute_gcd(60, 48), 12)

    def test_case_2(self):
        self.assertEqual(compute_gcd(0, 10), 10)

    def test_case_3(self):
        self.assertEqual(compute_gcd(-75, 100), 25)

    def test_case_4(self):
        self.assertEqual(compute_gcd(0, 0), "Inputs must be integers.")

    def test_case_5(self):
       self.assertEqual(compute_gcd("five", 17), "Inputs must be integers.")

if __name__ == '__main__':
    unittest.main()

class TestPrimality(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(test_primality(125), "Composite")

    def test_case_2(self):
        self.assertEqual(test_primality(9227), "Prime")

    def test_case_3(self):
        self.assertEqual(test_primality(226756349067901), "Prime")

    def test_case_4(self):
        self.assertEqual(test_primality(10645339258651698560366005671960349577271099695795778776116027191844748763697162810489806211517453319790712671486610384338352861386371682337778726583068523), "Prime")

    def test_case_5(self):
        self.assertEqual(test_primality(2), "2 is the only even prime number, no test needed.")

    def test_case_6(self):
        self.assertEqual(test_primality(1), "1 is composite, no test needed.")

    def test_case_7(self):
        self.assertEqual(test_primality(-7), "Input must be a positive integer")

if __name__ == '__main__':
    unittest.main()

class TestEuclideanAlgorithm(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(euclidean_algorithm(15, 125), 5)

    def test_case_2(self):
        self.assertEqual(euclidean_algorithm(112, 57), 1)

    def test_case_3(self):
        self.assertEqual(euclidean_algorithm(101, 462), 1)

    def test_case_4(self):
        self.assertEqual(euclidean_algorithm(1, 462), 1)

    def test_case_5(self):
        self.assertEqual(euclidean_algorithm(27, 1), 1)

    def test_case_6(self):
        self.assertEqual(euclidean_algorithm("a", 462), "Inputs must be integers.")

if __name__ == '__main__':
    unittest.main()
