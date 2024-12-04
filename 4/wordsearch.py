#!/usr/bin/python3

import sys

wordsearch = {}
items = 0
xitems = 0

for line in sys.stdin:
  xcoord = 0
  for x in line.rstrip():
    wordsearch[xcoord,items] = x
    xcoord += 1
  xitems = xcoord
  items += 1

count = 0

for ycoord in range(items):
  for xcoord in range(xitems):
    if wordsearch[xcoord,ycoord] == 'X':
      if xcoord > 2:
        if ycoord > 2:
          if wordsearch[xcoord-1,ycoord-1] == 'M':
            if wordsearch[xcoord-2,ycoord-2] == 'A':
              if wordsearch[xcoord-3,ycoord-3] == 'S':
                count += 1
        if wordsearch[xcoord-1,ycoord] == 'M':
          if wordsearch[xcoord-2,ycoord] == 'A':
            if wordsearch[xcoord-3,ycoord] == 'S':
              count += 1
        if ycoord < items - 3:
          if wordsearch[xcoord-1,ycoord+1] == 'M':
            if wordsearch[xcoord-2,ycoord+2] == 'A':
              if wordsearch[xcoord-3,ycoord+3] == 'S':
                count += 1
      if ycoord > 2:
        if wordsearch[xcoord,ycoord-1] == 'M':
          if wordsearch[xcoord,ycoord-2] == 'A':
            if wordsearch[xcoord,ycoord-3] == 'S':
              count += 1
      if wordsearch[xcoord,ycoord] == 'M':
        if wordsearch[xcoord,ycoord] == 'A':
          if wordsearch[xcoord,ycoord] == 'S':
            count += 1
      if ycoord < items - 3:
        if wordsearch[xcoord,ycoord+1] == 'M':
          if wordsearch[xcoord,ycoord+2] == 'A':
            if wordsearch[xcoord,ycoord+3] == 'S':
              count += 1
      if xcoord < xitems - 3:
        if ycoord > 2:
          if wordsearch[xcoord+1,ycoord-1] == 'M':
            if wordsearch[xcoord+2,ycoord-2] == 'A':
              if wordsearch[xcoord+3,ycoord-3] == 'S':
                count += 1
        if wordsearch[xcoord+1,ycoord] == 'M':
          if wordsearch[xcoord+2,ycoord] == 'A':
            if wordsearch[xcoord+3,ycoord] == 'S':
              count += 1
        if ycoord < items - 3:
          if wordsearch[xcoord+1,ycoord+1] == 'M':
            if wordsearch[xcoord+2,ycoord+2] == 'A':
              if wordsearch[xcoord+3,ycoord+3] == 'S':
                count += 1

print(count)
