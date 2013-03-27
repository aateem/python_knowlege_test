import pytest
#import key as pytest
import unittest
from itertools import permutations


class TestMedian(unittest.TestCase):

    def test_all_different_ascending(self):
        res = pytest.median(1, 2, 3)
        self.assertEqual(res, 2)

    def test_median_last(self):
        res = pytest.median(9, 3, 6)
        self.assertEqual(res, 6)

    def test_2_same(self):
        res = pytest.median(7, 8, 7)
        self.assertEqual(res, 7)

    def test_permute(self):
        for p in permutations((9, 4, 2)):
            self.assertEqual(pytest.median(*p), 4)


class TestCountWords(unittest.TestCase):

    def test_count(self):
        passage =("The number of orderings of the 52 cards in a deck of cards "
                  "is so great that if every one of the almost 7 billion people alive "
                  "today dealt one ordering of the cards per second, it would take "
                  "2.5 * 10**40 times the age of the universe to order the cards in every "
                  "possible way.")
        res = pytest.count_words(passage)
        self.assertEqual(res, 56)


class TestDownloadTime(unittest.TestCase):

    def test_kB_MB(self):
        res = pytest.download_time(1024,'kB', 1, 'MB')
        self.assertEqual(res[0], 0)
        self.assertEqual(res[1], 0)
        self.assertEqual(res[2], 1)

    def test_kb_Mb(self):
        res = pytest.download_time(1024,'kB', 1, 'Mb')
        self.assertEqual(res[0], 0)
        self.assertEqual(res[1], 0)
        self.assertEqual(res[2], 8)

    def test_GB_MB(self):
        res = pytest.download_time(13,'GB', 5.6, 'MB')
        self.assertEqual(res[0], 0)
        self.assertEqual(res[1], 39)
        self.assertAlmostEquals(res[2], 37.1428571429, 5)

    def test_GB_Mb(self):
        res = pytest.download_time(13,'GB', 5.6, 'Mb')
        self.assertEqual(res[0], 5)
        self.assertEqual(res[1], 16)
        self.assertAlmostEquals(res[2], 57.1428571429, 5)

    def test_MB_kB(self):
        res = pytest.download_time(10,'MB', 2, 'kB')
        self.assertEqual(res[0], 1)
        self.assertEqual(res[1], 25)
        self.assertEqual(res[2], 20)

    def test_MB_kb(self):
        res = pytest.download_time(10,'MB', 2, 'kb')
        self.assertEqual(res[0], 11)
        self.assertEqual(res[1], 22)
        self.assertEqual(res[2], 40)


class TestRotate(unittest.TestCase):

    def test_single_circular(self):
        res = pytest.rotate('sarah', 13)
        self.assertEqual(res, 'fnenu')
        res = pytest.rotate(res, 13)
        self.assertEqual(res, 'sarah')

    def test_single_back_and_forth(self):
        res = pytest.rotate('dave', 5)
        self.assertEqual(res, 'ifaj')
        res = pytest.rotate(res, -5)
        self.assertEqual(res, 'dave')

    def test_single_a_z(self):
        res = pytest.rotate('z', 1)
        self.assertEqual(res, 'a')
        res = pytest.rotate(res, -1)
        self.assertEqual(res, 'z')

    def test_long_with_spaces(self):
        str_ = ("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj")
        res = pytest.rotate(str_, -17)
        res = pytest.rotate(res, 17)
        self.assertEqual(res, str_)


class TestDeepCount(unittest.TestCase):
    def test_single_list(self):
        l = [1, 2, 3]
        self.assertEqual(pytest.deep_count(l), 3)

    def test_nested_with_empty(self):
        l = [1, [] ,3]
        self.assertEqual(pytest.deep_count(l), 3)

    def test_nested(self):
        l = [1, [1, 2, [3, 4]]]
        self.assertEqual(pytest.deep_count(l), 7)

    def test_deep_nested(self):
        l = [[[[[[[[1, 2, 3]]]]]]]]
        self.assertEqual(pytest.deep_count(l), 10)


if __name__ == '__main__':
    unittest.main()
