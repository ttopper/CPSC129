# bogosort.py
from random import randint
import time

def is_sorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

def bogosort(lst):
    L = len(lst)
    while not is_sorted(lst):
        i = randint(0, L-1)
        j = randint(0, L-1)
        lst[i], lst[j] = lst[j], lst[i]

REPNS = 10
MAXLEN = 12
print('N', 'Average Time')
for length in range(1,MAXLEN):
    total_time = 0
    for repn in range(REPNS):
        lst = list(range(length,0,-1))
        start = time.time()
        bogosort( lst )
        end = time.time()
        total_time += end-start
    print(length, total_time/REPNS)
