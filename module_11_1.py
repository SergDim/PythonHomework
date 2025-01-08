

import multiprocessing
import time

def read_info(name):
    all_data = []
    with open(name, mode="r", encoding="utf-8") as file:
        for line in  file:
            all_data.append(line)

if __name__ == '__main__':
    file_names = ("file 1.txt", "file 2.txt", "file 3.txt", "file 4.txt")
    time_start = time.time()
    for n in file_names:
        read_info(n)
    print("Время выполнения линейным методом", time.time() - time_start)
    time_start = time.time()
    with multiprocessing.Pool(len(file_names)) as p:
        p.map(read_info, file_names)
    print("Время выполнения мультипроцессорным методом", time.time() - time_start)
