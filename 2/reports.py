#!/usr/bin/python3

import sys, copy

part = 1

def check_safe(levels):
  direction = 0
  if levels[0] < levels[1]:
    direction = 1
  if levels[0] > levels[1]:
    direction = -1

  if direction != 0:
    for x in range(len(levels)-1):
      if direction == 1 and levels[x] > levels[x+1]:
        return 0
      if direction == -1 and levels[x] < levels[x+1]:
        return 0
      if abs(levels[x+1] - levels[x]) > 3:
        return 0
      if levels[x] == levels[x+1]:
        return 0
    return 1
  return 0

safecount = 0

for line in sys.stdin:
  levels = [int(x) for x in line.rstrip().split()]

  is_safe = check_safe(levels)
  if is_safe == 0 and part == 2:
    for x in range(len(levels)):
      levelcopy = copy.deepcopy(levels)
      del levelcopy[x]
      chkval = check_safe(levelcopy)
      if chkval == 1:
        is_safe = 1
  safecount += is_safe

print(safecount)
sys.exit()

