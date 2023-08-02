'''
Задана рекуррентная функция.
Область определения функции – натуральные числа.
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
Определить границы применимости рекурсивного и итерационного подхода.
Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
В-14.	F(0) = 1, F(1) = 1, F(n) = F(n–1) + F(n-2), при n > 1
'''

import time
import matplotlib.pyplot as plt

recursive_time = []
iterative_time = []

# Рекурсивная функция
def F_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return F_rec(n-1) + F_rec(n-2)

# Итеративная функция
def F_iter(n):
    if n == 0 or n == 1:
        return 1
    else:
        # Первые две переменных
        a, b = 1, 1
        for i in range(2, n+1):
            # Следующее значение
            c = a + b
            a, b = b, c
        return c

# Ввод числа n
n = int(input("Введите число n: "))
nn = []
nnn = []
# Подсчёт времени выполнения рекурсивно
for i in range(n+1):
    start_time = time.time()
    f_rec = F_rec(i)
    end_time = time.time()
    recursive_time.append(end_time - start_time)
    nn.append(i)
    print("F({}) = {} (рекурсивно в {:.6f} секунд)".format(nn[i], f_rec, recursive_time[i]))

# Подсчёт времени выполнения итеративно
for i in range(n+1):
    start_time = time.time()
    f_iter = F_iter(i)
    end_time = time.time()
    iterative_time.append(end_time - start_time)
    nnn.append(i)
    print("F({}) = {} (итеративно в {:.6f} секунд)".format(nnn[i], f_iter, iterative_time[i]))
# Вывод



# График
plt.plot(nn, recursive_time, 'ro', label='Рекурсивно')
plt.plot(nnn, iterative_time, 'bo', label='Итеративно')
plt.xlabel('n')
plt.ylabel('Время (с)')
plt.legend()
plt.show()
