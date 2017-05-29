from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        from random import randint

        num1 = randint(0, 10)
        num2 = randint(11, 20)
        num3 = randint(21, 30)
        num4 = randint(31, 40)

        x = [num1, num2, num3, num4]

        result = solution(x)

        self.assertNotEqual(None, result)

        self.assertTrue(result[0], x[3])
        self.assertTrue(result[1], x[2])
        self.assertTrue(result[2], x[1])
        self.assertTrue(result[3], x[0])