from time import sleep
from datetime import datetime
from threading import Thread

time_start_1 = datetime.now()


def wite_words(word_count, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(word_count):
            file.write(f"Какое-то слово №{i + 1}" + "\n")
            sleep(0.1)
    return print(f"Завершилась запись в файл {file_name}")


wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")

time_end_1 = datetime.now()
time_res_1 = time_end_1 - time_start_1
print(f"Работа потоков {time_res_1}")

time_start_2 = datetime.now()

thr_first = Thread(target=wite_words, args=[10, "example5.txt"])
thr_second = Thread(target=wite_words, args=[30, "example6.txt"])
thr_third = Thread(target=wite_words, args=[200, "example7.txt"])
thr_fourth = Thread(target=wite_words, args=[100, "example8.txt"])

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end_2 = datetime.now()
time_res_2 = time_end_2 - time_start_2
print(f"Работа потоков {time_res_2}")
