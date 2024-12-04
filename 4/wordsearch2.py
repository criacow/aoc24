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
    istrue = 0
    if wordsearch[xcoord,ycoord] == 'A':
      if xcoord >= 1 and ycoord >= 1 and xcoord < xitems - 1 and ycoord < items - 1:
        if wordsearch[xcoord-1,ycoord-1] == 'M':
          if wordsearch[xcoord+1,ycoord+1] == 'S':
            if wordsearch[xcoord-1,ycoord+1] == 'M':
              if wordsearch[xcoord+1,ycoord-1] == 'S':
                istrue = 1
            if wordsearch[xcoord+1,ycoord-1] == 'M':
              if wordsearch[xcoord-1,ycoord+1] == 'S':
                istrue = 1
        if wordsearch[xcoord+1,ycoord+1] == 'M':
          if wordsearch[xcoord-1,ycoord-1] == 'S':
            if wordsearch[xcoord-1,ycoord+1] == 'M':
              if wordsearch[xcoord+1,ycoord-1] == 'S':
                istrue = 1
            if wordsearch[xcoord+1,ycoord-1] == 'M':
              if wordsearch[xcoord-1,ycoord+1] == 'S':
                istrue = 1

        if wordsearch[xcoord-1,ycoord+1] == 'M':
          if wordsearch[xcoord+1,ycoord-1] == 'S':
            if wordsearch[xcoord-1,ycoord-1] == 'M':
              if wordsearch[xcoord+1,ycoord+1] == 'S':
                istrue = 1
            if wordsearch[xcoord+1,ycoord+1] == 'M':
              if wordsearch[xcoord-1,ycoord-1] == 'S':
                istrue = 1
        if wordsearch[xcoord+1,ycoord-1] == 'M':
          if wordsearch[xcoord-1,ycoord+1] == 'S':
            if wordsearch[xcoord-1,ycoord-1] == 'M':
              if wordsearch[xcoord+1,ycoord+1] == 'S':
                istrue = 1
            if wordsearch[xcoord+1,ycoord+1] == 'M':
              if wordsearch[xcoord-1,ycoord-1] == 'S':
                istrue = 1
    if istrue == 1:
      count += 1

print(count)
