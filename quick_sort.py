"""
В первой строке задано два целых числа 1≤n≤50000 и 1≤m≤50000 — количество отрезков и точек на прямой, соответственно. 
Следующие n строк содержат по два целых числа ai и bi (ai≤bi) — координаты концов отрезков. 
Последняя строка содержит m целых чисел — координаты точек. Все координаты не превышают 108 по модулю. 
Точка считается принадлежащей отрезку, если она находится внутри него или на границе. 
Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.
Sample Input:
2 3
0 5
7 10
1 6 11

Sample Output:
1 0 0
"""

import random
import bisect


def main():
    n, m = map(int, input().split())
    lst_left = list()
    lst_right = list()
    for i in range(n):
        l, r = map(int, input().split())
        lst_left.append(l)
        lst_right.append(r)
    points = [int(q) for q in input().split()]
    lst_left.sort()
    lst_right.sort()
    for p in points:
        index_left = bisect.bisect(lst_left, p)
        index_right = bisect.bisect_left(lst_right, p)
        print(abs(index_left - index_right), end = " ")


if __name__ == "__main__":
    main()
