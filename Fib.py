"""
Небольшое число Фибоначчи
"""

def fib(n):
    # создаем список
    a = list()
    # добавляем первые два числа Фибоначчи
    a.append(0)
    a.append(1)
    # начинаем с 3 числа
    i = 2
    while i <= n:
        # добавляем найденное число
        a.append(a[i-1] + a[i-2])
        i += 1
    return a[n]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
