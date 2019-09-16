"""
двоичный поиск
в первой строке число 1≤n≤10^5 и массив A[1…n]  из n различных натуральных чисел, не превышающих 109, в порядке возрастания, 
во второй — целое число 1≤k≤10^5 и k натуральных чисел b1,…,bk, не превышающих 109.
Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n, для которого A[j]=bi, или −1, если такого j нет.
"""

def binary_search(b_i, n, arr):
    left = 0
    right = n - 1
    while left <= right:
        m = left + ((right - left) // 2)
        if arr[m] == b_i:
            return m
        elif arr[m] > b_i:
            right = m - 1
        else:
            left = m + 1
    return -2


def main():
    n, *arr = map(int, input().split())
    k, *b = map(int, input().split())
    for i in b:
        print(binary_search(i, n, arr) + 1, end=" ")


if __name__ == "__main__":
    main()
