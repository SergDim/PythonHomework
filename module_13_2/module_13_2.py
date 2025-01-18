import runner_and_tournament as battles
import unittest

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for i in range(3):
            one_result = cls.all_results.get(i)
            if one_result is None:
                continue
            next_runner = one_result.get(1)
            if next_runner is None:
                continue
            else:
                print(f"{{1:{next_runner}", end='')
            next_runner = one_result.get(2)
            if next_runner is None:
                print("}")
                continue
            else:
                print(f", 2:{next_runner}", end='')
            next_runner = one_result.get(3)
            if next_runner is None:
                print("}")
                continue
            else:
                print(f", 3:{next_runner}}}")

    def setUp(self):
        self.runner1 = battles.Runner('Усэйн', 10)
        self.runner2 = battles.Runner('Андрей', 9)
        self.runner3 = battles.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament13(self):
        self.all_results.update({0: None})
        result = battles.Tournament(90, self.runner1, self.runner3).start()
        self.all_results.update({0: result})
        self.assertTrue(result[2] == self.runner3.name)
        for i in range(1, 4):
            i_runner = result.get(i)
            if i_runner is None:
                break
            for j in range(i+1, 4):
                j_runner = result.get(j)
                if j_runner is None:
                    break
                else:
                    self.assertTrue(i_runner.speed > j_runner.speed)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament23(self):
        self.all_results.update({1 : None})
        result = battles.Tournament(90, self.runner2, self.runner3).start()
        self.all_results.update({1 : result})
        self.assertTrue(result[2] == self.runner3.name)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament123(self):
        self.all_results.update({2: None})
        result = battles.Tournament(90, self.runner1, self.runner2, self.runner3).start()
        self.all_results.update({2: result})
        self.assertTrue(result[3] == self.runner3.name)


if __name__ == '__main__':
    unittest.main()