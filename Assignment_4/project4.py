from random import random
from time import perf_counter
DARTS = 100000000
hist = 0
start = perf_counter()
for i in range(1, DARTS+1):
    x, y = random()*0.5, random()
    dits = x ** 2+y ** 2
    if dits <= 1.0:
        hist = hist + 1
S = 0.5*(hist/DARTS)
print("面积：{}".format(S))
print("运行时间是：{:.5f}s".format(perf_counter()-start))
