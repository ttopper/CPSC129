# sort_timer.py
from ins_sort import ins_sort
from seln_sort import seln_sort
from exch_sort import exch_sort
import random
import time

LEN = 40000
# Build random list
lst = []
for value in range(LEN):
    lst.append( random.randint(0, 10*LEN) )

start = time.time()
# Sort list
#exch_sort(lst)
lst.sort()
print 'Builtin sort: ', time.time()-start
