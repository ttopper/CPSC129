# reheap.py

def left_child( node ):
    return 2*node + 1
def right_child( node ):
    return 2*node + 2

def reheap(lst, node, stop):
    lc = left_child(node)
    rc = right_child(node)
    if lc >= stop:
        return
    if lst[lc] > lst[node] and lst[lc] >lst[rc]:
        (lst[lc], lst[node]) = (lst[node], lst[lc])
        reheap(lst, lc, stop)
    elif lst[rc] > lst[node]:
        (lst[rc], lst[node]) = (lst[node], lst[rc])
        reheap(lst, rc, stop)

lst = [48, 32, 68, 18, 29, 71, 41]
print 'Before:', lst
reheap(lst, 0, len(lst)-1)
print 'After:', lst

def parent(node):
    return (node-1)/2

def heapify(lst):
    for node in range(parent(len(lst)-1), -1, -1):
        reheap(lst, node, len(lst)-1)

lst = [48, 32, 68, 18, 29, 71, 41]
print 'Before:', lst
heapify(lst)
print 'After;', lst
