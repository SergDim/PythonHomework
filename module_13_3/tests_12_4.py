

import unittest, logging
import rt_with_exceptions as exc_runner

logging.basicConfig(filename="runner_tests.log", filemode="w", level=logging.INFO,
                    encoding="UTF-8", format="%(asctime)s | %(levelname)s | %(message)s")

class ExcRunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            test_runner_obj = exc_runner.Runner('', -2)
            logging.info("test_walk выполнен успешно")
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            test_runner_obj = exc_runner.Runner(1, 1)
            logging.info("test_run выполнен успешно")
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)


if __name__ == '__main__':
    unittest.main()