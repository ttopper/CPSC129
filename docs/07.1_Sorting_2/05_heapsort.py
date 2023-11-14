# heapsort.py
def lchild( i ):
    '''Given index of node in list,
    return index of its left child.'''
    return 2*i + 1
def rchild( i ):
    '''Given index of node in list,
    return index of its right child.'''
    return 2*i + 2
def parent( i ):
    '''Given index of node in list,
    return index of its parent.'''
    return (i-1)/2

def reheap(lst, i, stop):
    lc = lchild(i)
    rc = rchild(i)
    # Stop before falling off tree!
    if lc >= stop:
        return
    if lst[lc] >= lst[rc] and lst[lc] > lst[i]:
        lst[lc], lst[i] = lst[i], lst[lc]
        reheap(lst, lc, stop)
    elif lst[rc] >= lst[lc] and lst[rc] > lst[i]:
        lst[rc], lst[i] = lst[i], lst[rc]
        reheap(lst, rc, stop)
    '''
    if lc >= rc and lc > p:
        swap(lc, p)
        reheap(lc)
    elif rc >= lc and rc > p:
        swap(rc, p)
        reheap(rc)
    '''

def heapsort(l):
    for i in range(parent(len(l)-1), -1, -1):
        reheap(l, i, len(l)-1)
    nas = len(l)-1
    for swap in range(len(l)):
        l[0], l[nas] = l[nas], l[0]
        nas -= 1
        reheap(l, 0, nas)
    
l = [ 19, 43, 52, 27, 71, 86, 12 ]
print l
heapsort(l)
print l
