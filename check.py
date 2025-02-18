import os
import pandas as pd
a=os.listdir("/media/appsmartz/storage/annotation/To be done")
print(len(a))
b=os.listdir("/media/appsmartz/storage/annotation/static/instrumantal_midi_unlabled")
print(len(b))
c=0
lis=[]
for i in a:
    for j in b:
        if(i==j):
            print("Same",i)
            c=c+1
            lis.append(i)
print("Same Count",c)
print(lis)




