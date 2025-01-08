

from random import randint
from queue import Queue
import time, threading

guest_free_table = threading.Lock()

class Table:

    def __init__(self, number):
        super().__init__()
        self.number = number
        self.guest = None


class Guest(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(float(randint(1, 10)))
        try:
            if guest_free_table.locked():
                guest_free_table.release()
        except RuntimeError:
            pass

class Cafe:

    def __init__(self, *args):
        super().__init__()
        self.tables = args
        self.guest_queue = Queue()

    def guest_arrival(self, *guests):
        number_guest = 0
        for table in self.tables:
            if number_guest == len(guests):
                return
            if table is not None:
                table.guest = guests[number_guest]
                table.guest.start()
                print(f"{table.guest.name} сел(-а) за стол номер {table.number}")
                number_guest += 1
        while number_guest < len(guests):
            self.guest_queue.put(guests[number_guest])
            print(f"{guests[number_guest].name} в очереди")
            number_guest += 1
        return

    def discuss_guests(self):
        any_table_buzy = True
        while any_table_buzy:
            guest_free_table.acquire()
            free_table = 0
            for table in self.tables:
                if table.guest is None:
                    free_table += 1
                elif not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    if self.guest_queue.empty():
                        free_table += 1
                        table.guest = None
                    else:
                        table.guest = self.guest_queue.get()
                        print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        table.guest.start()
            if free_table == len(self.tables):
                any_table_buzy = False
        print("В кафе все столы свободны")

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()


