from collections import Counter 
from scipy.spatial import distance
import numpy as np
from sympy import *

def input():
  f = open("C:\\Users\\willh\\Documents\\GitHub\\BDA_asignment1\\B\\data\\LSH_data.txt", "r")
  dic = {}
  max_word = 0
  max_doc =  0
#form word set
  for line in f:
    doc_i, word_j, val = line.split(',',2)
    if dic.get(int(doc_i))  == None:
      dic[int(doc_i)] = [[int(word_j), int(val)]]
    else:
      dic[int(doc_i)] += [[int(word_j), int(val)]]
    max_doc = max(max_doc, int(doc_i))
    max_word = max(max_word, int(word_j))

  for k in dic:
    base = np.zeros(max_word)
    word_and_val = dic[k]
    for i in range(0,len(word_and_val)):
        base[word_and_val[i][0]-1] += word_and_val[i][1]
    #print(base)
    dic[k] = base
    
  return dic, max_word

def compare_all_word(dic):

  doc_2 = dic[2]
  #dic.pop(2)
  for k in dic:
    dic[k] = 1- distance.jaccard(dic[k],doc_2)

  most_common = Counter(dic).most_common(len(dic))
  return most_common[:100]


dic, max_word = input()

out_all_words = compare_all_word(dict(dic))

print("    ")
print(out_all_words)


def mini_hashing(dic, num_of_function, max_word):
  #find the primer
  m =  list(primerange(max_word, 2*max_word))[0]

  #replicate the dic
  hash_result, index = dict(dic), np.arange(max_word)
  for k in hash_result:
    hash_result[k] = []

  # for every hash function, we have a distinct permutation
  for j in range(0, num_of_function):
    permutation = np.random.permutation(max_word)
    print(permutation)
    temp_dic = dict(dic)
    #for every permutation, we want to loop through the dic 
    #with the order of words 
    for i in range(0, max_word):
      index = np.where(permutation == i)
      l = []
      for k in temp_dic:
        if temp_dic[k][index] != 0:
          hash_result[k] += [i]
          l += [k]
      for ls in l:
        temp_dic.pop(ls)

  # for k in hash_result:
  #   print(hash_result[k])
  
  doc_2 = hash_result[2]
  temp = {}
  # hash_result.pop(2)
  print(doc_2)
  for k in hash_result:
    # print(k)
    # print(hash_result[k])
    # print("   ")
    temp[k] = 1 - distance.jaccard(hash_result[k],doc_2)
  most_common = Counter(temp).most_common(len(temp))
  return most_common[:100], hash_result

out_signiture, signiture = mini_hashing(dic,400,max_word) #try 200



print("    ")

print(out_signiture)


print("   ")
d1 = set(dict((x, y) for x, y in out_signiture).keys())
d2 = set(dict((x, y) for x, y in out_all_words).keys())
print(d1.intersection(d2))

print(len(d1.intersection(d2)))


print(len(d1.intersection(d2)) / (200-len(d1.intersection(d2))))