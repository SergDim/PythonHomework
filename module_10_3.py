

from random import randint
import threading
from time import sleep

class Bank:

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = threading.Lock()
        self.lock.acquire()

    def deposit(self):
        for i in range(100):
            put = randint(50, 500)
            self.balance += put
            print(f"Пополнение: {put}. Баланс: {self.balance}")
            if self.balance > 500 and self.lock.locked():
                self.lock.release()
            sleep(0.01)

    def take(self):
        for i in range(100):
            get = randint(50, 500)
            print(f"Запрос на {get}")
            if get >= self.balance:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            else:
                self.balance -= get
                print(f"Снятие: {get}. Баланс: {self.balance}")

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()


print(f"Итоговый баланс: {bk.balance}")