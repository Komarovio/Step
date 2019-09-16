"""
Небольшое число Фибоначчии
"""

def fib(n):
    a = list()
    a.append(0)
    a.append(1)
    i = 2
    while i <= n:
        a.append(a[i-1] + a[i-2])
        i += 1
    return a[n]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
