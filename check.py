import random

path = r"E:\github\Dynamic-Trees-for-Beachparty\run\saves\Growth Chamber\computercraft\computer\6\dtbeachparty\palm.txt"
from utilSimple import FileGetter as fg

txt = fg.getAllTextInFile(path).split('\n')
newt = []

for t in txt:
    if t.split(":")[-1] != "J" * 2 and t.split(":")[-1] != "J" * 3 and t.split(":")[-1] != "J" * 4:
        print(t)
    else:
        if random.random() > 0.9:
            print(t)
