#!/usr/bin/python3
import sys
import re

filepath = os.environ.get('mapreduce_map_input_file')
filename = os.path.split(filepath)[-1]

# input comes from STDIN (standard input)
for line in sys.stdin:
  # remove leading and trailing whitespace
  line = line.strip()
  #remove punctuations
  line = re.sub(r'[^\w\s]','',line)
  #to lower case
  line = line.lower()
  # split the line into words
  words = line.split()
  # increase counters
  for word in words:
    if "plato" in filename:
      print('%s\t%s' % (word, 1))
    else:
      print('%s\t%s' % (word, 0))
