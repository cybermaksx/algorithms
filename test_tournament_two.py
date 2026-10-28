import random
import unittest

from tournament_two import tournament_two


class TestTournamentTwo(unittest.TestCase):

    def test_example(self):
        # Пример из разбора: ответ посчитан вручную
        self.assertEqual(tournament_two([15, 21, 13, 8, 26, 11, 17, 9]), (26, 21))

    def test_two_elements(self):
        # Самый маленький вход: один матч
        self.assertEqual(tournament_two([1, 2]), (2, 1))
        self.assertEqual(tournament_two([2, 1]), (2, 1))

    def test_left_side_wins(self):
        # Чемпион в левой половине: проверяет ветку else
        self.assertEqual(tournament_two([8, 7, 1, 2]), (8, 7))

    def test_second_lost_early(self):
        # Второе место проиграло чемпиону в первом раунде, а не в финале
        self.assertEqual(tournament_two([9, 8, 1, 2, 3, 4, 5, 6]), (9, 8))

    def test_duplicates(self):
        # Одинаковые максимумы: второе место равно первому
        self.assertEqual(tournament_two([5, 5, 1, 2]), (5, 5))

    def test_negative(self):
        self.assertEqual(tournament_two([-3, -1, -7, -2]), (-1, -2))

    def test_random_against_sorted(self):
        # Сравниваем с заведомо правильным, но медленным решением
        for k in range(1, 11):
            N = 2 ** k
            for _ in range(100):
                A = [random.randint(-100, 100) for _ in range(N)]
                s = sorted(A)
                with self.subTest(A=A):
                    self.assertEqual(tournament_two(A), (s[-1], s[-2]))

    def test_odd_length_fails(self):
        # Нечётная длина не поддерживается: ждём ошибку
        with self.assertRaises(IndexError):
            tournament_two([1, 2, 3])


if __name__ == "__main__":
    unittest.main()
