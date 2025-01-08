

class  IncorrectVinNumber(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)

class IncorrectCarNumbers(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__()

class Car:

    def __init__(self, model, vin, numbers):
        if self.__is_valid_vin(vin):
            self.vin = vin
        if self.__is_valid_numbers(numbers):
            self.numbers = numbers
        self.model = model
        super().__init__()

    def __is_valid_vin(self, vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        elif vin < 1000000 or vin > 9999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        else:
            return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        elif len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        else: return True


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')