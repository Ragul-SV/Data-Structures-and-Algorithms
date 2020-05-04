#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'changeBits' function below.
#
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#  3. STRING_ARRAY queries
#

def modifyBit(n,p,b):
    mask = 1<<p
    if b:
        return n | mask
    else:
        return n & ~mask
    # return (n & ~mask)|((b<<p) & mask)
    
def changeBits(a, b, queries):
    # Write your code here
    a = int(a.strip(),2)
    b = int(b.strip(),2)
    res = ""
    for cases in queries:
        q = cases.strip().split()
        
        if q[0]=="set_a":
            a = modifyBit(a,int(q[1]),int(q[2]))
        elif q[0]=="set_b":
            b = modifyBit(b,int(q[1]),int(q[2]))
        else:
            c = a+b
            val = int(bool(c & (1<<(int(q[1])))))
            res += str(val)
    print(res)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    ab_size = int(first_multiple_input[0])

    queries_size = int(first_multiple_input[1])

    a = input()

    b = input()

    queries = []

    for _ in range(queries_size):
        queries_item = input()
        queries.append(queries_item)

    changeBits(a, b, queries)
