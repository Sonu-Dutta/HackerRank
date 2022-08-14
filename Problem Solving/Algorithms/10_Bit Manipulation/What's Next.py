import math
import os
import random
import re
import sys


def whatsNext(arr):
    # set bits are at each even index
    l = len(arr) - 1
    # case: l == 0
    if not l:
        if arr[0] == 1:
            print(2)
            print(*[1, 1])
        else:
            print(3)
            print(*[1, 1, arr[0]-1])
        return
    # find index for least significant set bit
    i = l-1 if l & 1 else l
    # case: l == 1
    if l == 1:
        t = [1, arr[1] + 1, arr[0] - 1]
    # case: last bit group is off
    elif l - i:
        t = arr[:i-1] + [arr[i-1] - 1, 1, arr[-1] + 1, arr[i] - 1]
    # case: last bit group is set
    else:
        t = arr[:i-1] + [arr[i-1] - 1, 1, 1, arr[i] - 1]
    # handle zeros
    if not t[-1]:
        t.pop(-1)
    if t.count(0):
        i_lst = []
        for i, a in enumerate(t):
            if not a:
                #  combine bits around zero
                t[i-1] += t[i+1]
                i_lst.append(i)
        # remove zero and extra bits
        for i in i_lst[-1:-1-len(i_lst):-1]:
            t.pop(i+1)
            t.pop(i)
    print(len(t))
    print(*t)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        whatsNext(arr)
