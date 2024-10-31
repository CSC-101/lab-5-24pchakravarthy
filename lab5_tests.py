import data
import lab5
import unittest

from lab5 import is_descending


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test1add(self):
        t1 = data.Time(1, 10, 20)
        t2 = data.Time(2, 25, 30)
        return lab5.time_add(t1, t2)

    def test2add(self):
        t1 = data.Time(6, 45, 50)
        t2 = data.Time(7, 25, 40)
        return lab5.time_add(t1, t2)


    # Part 4
    def test1descent(self):
        r1 = [10.4, 8.2, 1.4, 4.5]
        return lab5.is_descending(r1)

    def test2descent(self):
        r2 = [9.3, 4.6, 2.1]
        return lab5.is_descending(r2)


    # Part 5
    def test_largest_between1(self):
        n1 = [4, 6, 1, 7, 9, 2, 5]
        return lab5.largest_between(n1, 1, 2)

    def test_largest_between2(self):
        n2 = [4, 6, 1, 7, 9, 2, 5]
        return lab5.largest_between(n2, -2, 2)




    # Part 6
    def test_originfurthest1(self):
        examples = [data.Point(2, 3), data.Point(4, 7), data.Point(8, 9)]
        return lab5.furthest_from_origin(examples)

    def test_originfurthest2(self):
        examples = []
        return lab5.furthest_from_origin(examples)


if __name__ == '__main__':
    unittest.main()
