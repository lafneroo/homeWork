import os
import time
import multiprocessing


def func1():
    print("Функция 1: запущена, ID процесса =", os.getpid())
    time.sleep(1)
    print("Функция 1: завершена")


def func2():
    print("Функция 2: запущена, ID процесса =", os.getpid())
    time.sleep(1)
    print("Функция 2: завершена")


def func3():
    print("Функция 3: запущена, ID процесса =", os.getpid())
    time.sleep(1)
    print("Функция 3: завершена")


def func4():
    print("Функция 4: запущена, ID процесса =", os.getpid())
    time.sleep(1)
    print("Функция 4: завершена")


if __name__ == "__main__":
    print("Главный процесс, ID =", os.getpid())

    p1 = multiprocessing.Process(target=func1)
    p2 = multiprocessing.Process(target=func2)

    print("Создан процесс p1, ID =", p1.pid)
    print("Создан процесс p2, ID =", p2.pid)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Все процессы завершены")

    print("Результат p1:", p1.exitcode)
    print("Результат p2:", p2.exitcode)