
import time, threading

def wite_words(word_count, file_name):
    with open(file_name, mode="w", encoding="utf-8") as file:
        for word in range(1, word_count+1):
            file.write(f"Какое-то слово № {word}\n")
            time.sleep(0.1)
    print("Завершилась запись в файл", file_name)

time_spend = time.time()
wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")
print("Работа потоков ", time.time() - time_spend)

time_spend = time.time()
thread1 = threading.Thread(target=wite_words, args=(10, "example5.txt"))
thread2 = threading.Thread(target=wite_words, args=(30, "example6.txt"))
thread3 = threading.Thread(target=wite_words, args=(200, "example7.txt"))
thread4 = threading.Thread(target=wite_words, args=(100, "example8.txt"))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
print("Работа потоков ", time.time() - time_spend)