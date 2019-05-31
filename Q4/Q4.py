import math
import random

def IsInCircle(x,y):
    if x**2 + y**2 <= 1/4:
        return True
    else:
        return False

def Find():
    n=0
    while True:
        n += 1
        cnt = 0
        for _ in range(0,n):
            x = random.random()-1/2
            y = random.random()-1/2
            if IsInCircle(x,y):
                cnt += 1
        if abs(4*(cnt/n)-math.pi) < 0.01:
            return n

n = int(input())
cnt = 0
for _ in range(0,n):
    cnt += Find()
print("{:.5f}".format(cnt/n))
