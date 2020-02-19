from collections import Counter 
from scipy.spatial import distance
import numpy as np
from sympy import *

def input():
  f = open("C:\\Users\\willh\\Documents\\GitHub\\BDA_asignment1\\taskC\\data\\stream_data.txt", "r")
  stream = []
#form word set
  for line in f:
    words = line.split('\t')
    for word in words:
      try:
        stream += [int(word)]
      except Exception as e:
        continue
  return stream

stream = input()
bucket = [] #[start, ending, size]


for i in range(0,len(stream)):
  if stream[i] == 1:
    #create a bucket
    bucket += [[i,i,1]]
    
    #review the bucket list and merge
    bucket, initial_size, acc ,result = list(bucket[::-1]), 0, 0,[]
    for b in bucket:
      if b[-1] != initial_size: #new size
       initial_size, acc = b[-1], 1
       result += [b]
      elif b[-1] == initial_size and acc == 1: #second of new size
        acc += 1
        result += [b]
      elif b[-1] == initial_size and acc == 2: #third then merge
        
        #modify the last one in the result
        #where star, end, current
        result[-1] = [b[0], result[-1][1], b[2]*2] #end is the current

        #initial_size = last digit , acc = 1
        initial_size, acc = result[-1][2], 1

    #update bucket
    bucket = result[::-1]
  else: #dp mothing
    continue


stream = stream[-1000:]
actuall = Counter(stream)

acc = 0

bucket = bucket[::-1]

for b in bucket:
  if 10000 - b[0] <= 1000 and 10000 - b[1] <= 1000:
    acc += b[-1]
  else:
    acc += b[-1]/2
    break
print(bucket)

print("       ")
print("  estimation  "+str(acc))
print("       ")
print("  actuall     "+str(actuall[1]))
