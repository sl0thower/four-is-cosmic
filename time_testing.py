import os
import time
import numpy as np

l = "this, is my-test"

t0 = time.time()

x=0
while x < 1e6:
    counter=0
    for i in l:
        if i not in [","," ","-"]:
            counter+=1
    x+=1
    #print(x)
    #os.system('clear')

t1 = time.time()

x=0
while x< 1e6:
    counter=0
    for i in l:
        if i != "," and i != " " and i != "-":
            counter+=1
    x+=1

t2 = time.time()

print(" not in: ", np.round(t1-t0,4), "s")
print("and and: ", np.round(t2-t1,4), "s")
