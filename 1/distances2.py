#!/usr/bin/python3

import sys

DistancesA = []
DistancesB = [0] * 100000
items = 0

for line in sys.stdin:
  a,b = line.rstrip().split()
  DistancesA.append(int(a))
  DistancesB[int(b)] += 1
  items += 1

SortDistA = sorted(DistancesA)

dist = 0

for x in range(items):
  print(f'{SortDistA[x]} {DistancesB[SortDistA[x]]}')
  dist += SortDistA[x] * DistancesB[SortDistA[x]]

print(dist)
