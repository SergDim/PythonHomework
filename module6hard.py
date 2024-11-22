from math import pi, sqrt


class _Figure:
    sides_count = 0

    def __init__(self, color, sides):
        self.__color = color
        self.__sides = sides
        self.filled = False

    def __len__(self):
        return sum(self.__sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r < 0 or r > 255 or g <0 or g > 255 or b < 0 or b > 255:
            return False
        else:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, new_sides):
        if self.sides_count != len(new_sides) or len(new_sides) == 0 or min(new_sides) < 0:
            return False
        else:
            return True

    def get_sides(self):
        return self.__sides

    def  set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides.clear()
            self.__sides.extend(list(new_sides))

class Circle(_Figure):
    sides_count = 1

    def __init__(self, color, *args):
        if Circle.sides_count != len(args) or min(args) < 0:
            super().__init__(color, [1])
            self.__radius = 1 / (2 * pi)
        else:
            super().__init__(color, list(args))
            self.__radius = args[0] / (2 * pi)

    def get_square(self):
        return pi * self.__radius * self.__radius

class Triangle(_Figure):
    sides_count = 3

    def __init__(self, color, *args):
        if Triangle.sides_count != len(args) or min(args) < 0:
            super().__init__(color, [1,1,1])
        else:
            super().__init__(color, list(args))

    def get_square(self):
        l = self.get_sides()
        p = sum(l) / 2
        return sqrt(p * (p - l[0]) * (p - l[1]) * (p - l[2])) / 4

class Cube(_Figure):
    sides_count = 12

    def __init__(self, color, *args):
        if len(args) != 1 or args[0] < 0:
            self.__sides = [1] * 12
        else:
            self.__sides = list(args) * 12
        super().__init__(color, self.__sides)

    def get_volume(self):
        return self.__sides[0]**3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())