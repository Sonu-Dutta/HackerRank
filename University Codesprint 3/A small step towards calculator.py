#!/bin/python3

import sys

def solve(opr):
    if opr[1]=='+':
        addn=int(opr[0])+int(opr[2])
        return(addn)
    else:
        subt=int(opr[0])-int(opr[2])
        return (subt)

if __name__ == "__main__":
    opr = input().strip()
    result = solve(opr)
    print(result)