

import unittest, runner

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        test_runner_obj = runner.Runner('')
        for i in range(10):
            test_runner_obj.walk()
        self.assertEqual(test_runner_obj.distance, 50, "method walk fail")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        test_runner_obj = runner.Runner('')
        for i in range(10):
            test_runner_obj.run()
        self.assertEqual(test_runner_obj.distance, 100, "method run fail")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        walk_test_runner_obj = runner.Runner('walk')
        run_test_runner_obj = runner.Runner('run')
        for i in range(10):
            run_test_runner_obj.run()
            walk_test_runner_obj.walk()
        self.assertNotEqual(run_test_runner_obj.distance, walk_test_runner_obj.distance, "comparison walk and run fail")


if __name__ == '__main__':
    unittest.main()