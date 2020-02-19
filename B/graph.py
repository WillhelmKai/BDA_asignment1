import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def LSH(r, b):
  similarity = np.arange(0,1000)/1000
  prob_sharing_buckets = 1- (1- similarity**r)**b

  return  prob_sharing_buckets

# fig = plt.figure()
# ims = []
min_FP_FN, min_r, min_b, min_s = 1,0,0,0.0477
fig, ax = plt.subplots()

ideal_situation = np.zeros(1000)
ideal_situation[int(min_s*100):] = 1
ax.plot(np.arange(0,1000)/1000, ideal_situation, label = "ideal situation")

M = 500

for r in range(1,M):
  b = M//r
  if b*r != M:
    continue
  FP = LSH(r,b)
  FN = (1 - FP)
  ax.plot(np.arange(0,1000)/1000, FP, label = "r= "+str(r)+"  b= "+str(b))
  FP_FN = sum(FP[:int(min_s*100)])/1000  + sum(FN[int(min_s*100):])/1000
  if FP_FN < min_FP_FN:
    min_FP_FN, min_r, min_b = FP_FN, r,b
  # print(FP_FN)
  print(b)

print(min_r,min_b,min_FP_FN,min_s)

# ax.plot(np.arange(0,1000)/1000, LSH(min_r, min_b))

ax.set(xlabel='Similarity', ylabel='Prob.sharing buckets')
ax.grid()
plt.legend()

fig.savefig("test.png")
plt.show()
