

import unittest
import module_13_1, module_13_2

test_runner = unittest.TestSuite()
test_runner.addTest(unittest.TestLoader().loadTestsFromTestCase(module_13_1.RunnerTest))
test_runner.addTest(unittest.TestLoader().loadTestsFromTestCase(module_13_2.TournamentTest))

tests_runner = unittest.TextTestRunner(verbosity=2)
tests_runner.run(test_runner)