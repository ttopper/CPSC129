def rbsearch(lst, target):
    if len(lst) == 0:
        return False
    
    mid = len(lst)/2
    if lst[mid] == target:
        return True
    elif lst[mid]>target:
        return rbsearch(lst[:mid], target)
    else:
        return rbsearch(lst[mid+1:], target)

l = [1,3,6,8,11,14,18,21,25,28]
 
print l
print rbsearch(l,11)
