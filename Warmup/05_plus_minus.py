import math
import os
import random
import re
import sys

def plusMinus(arr):
    n = len(arr)
    plus_count = 0
    minus_count = 0
    zero_count = 0
    for i in range(n):
        if arr [i] > 0:
            plus_count += 1
        elif arr[i]<0:
            minus_count += 1
        elif arr[i] == 0:
            zero_count += 1

    print(f"{plus_count / n :.6f}")
    print(f"{minus_count / n :.6f}")
    print(f"{zero_count / n :.6f}")


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    plusMinus(arr)