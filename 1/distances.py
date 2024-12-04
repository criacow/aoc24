#!/usr/bin/python3

import sys

DistancesA = []
DistancesB = []
items = 0

for line in sys.stdin:
  a,b = line.rstrip().split()
  DistancesA.append(int(a))
  DistancesB.append(int(b))
  items += 1

SortDistA = sorted(DistancesA)
SortDistB = sorted(DistancesB)

dist = 0

for x in range(items):
  dist += abs(SortDistA[x] - SortDistB[x])
  print(f'{SortDistA[x]} {SortDistB[x]} {dist}')
