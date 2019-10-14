#!/usr/bin/python3
import sys
import re
# input comes from STDIN (standard input)
for line in sys.stdin:
  #separate by ,
  doc_i, word_j, val = line.strip(',',2)
  result = ""
  for i in range(0,val):
    result += word_j+","
  print('%s\t%s' % (doc_i, result))