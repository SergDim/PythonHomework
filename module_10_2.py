

import time, threading

class Knight(threading.Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name} , на нас напали!")
        enemies = 100
        day = 0
        while enemies > 0:
            day += 1
            time.sleep(1)
            if enemies > self.power:
                enemies -= self.power
            else:
                enemies = 0
            print(f"{self.name} сражается {day}..., осталось {enemies} воинов.")
        print(f"{self.name} одержал победу спустя {day} дней(дня)")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")