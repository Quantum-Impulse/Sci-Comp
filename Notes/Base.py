#!/usr/bin/env python3

import sys

def main():
    line = sys.stdin.readline().strip()

    line = line.rstrip()

    line = line.split()

    num = int(line[0])
    base = int(line[1])

    s = ''
    while num > 0:
        s = str(num % base) + s
        num = num // base

    
    print(s)
main()
    
