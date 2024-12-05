#!/usr/bin/python3

import sys, re

part = 1
count = 0

bigstr = ""
for line in sys.stdin:
  bigstr += line.rstrip()

if part == 2:
  bigstr = re.sub(r'don\'t\(\).*?do\(\)', '', bigstr)

muls = re.findall(r'mul\(\d{1,3},\d{1,3}\)', bigstr)
for mul in muls:
  a,b = re.findall(r'\d{1,3}', mul)
  count += int(a) * int(b)

print(count)
