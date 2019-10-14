#!/usr/bin/python3
from operator import itemgetter
import sys
from collections import Counter 
#hold a dictionary
dic = {}
for line in sys.stdin:
  doc, words = line.split('\t', 1)
  if dic.get(doc)  == None:
    dic[doc] = words
  else:
    dic[doc] += words

for doc, words in most_common:
  print('%s\t%s' % (doc, words))
