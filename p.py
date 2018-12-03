import os
from getkey import getkey, keys

graf = "****X****"
def printer():
    global graf
    clear()
    for i in range(0,9,3):
        print(graf[i:i+3])
def insert(num = 4):
    global graf
    graf = '*'*num+'X'+'*'*(8-num)

def clear():
    os.system("clear")
pos = 4
while True:
    printer()
    n=getkey()
    if(n==keys.UP):
        pos = (pos - 3) % 9
    if(n==keys.DOWN):
        pos = (pos + 3) % 9
    elif(n==keys.LEFT):
        pos = (pos - 1) % 9
    elif(n==keys.RIGHT):
        pos = (pos + 1) % 9
    insert(pos)