# rqsort2.py

def qsort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    smaller = []
    larger = []
    for item in lst[1:]:
        if item <= pivot:
            smaller.append(item)
        else:
            larger.append(item)
    #print(smaller, '+', pivot, '+', larger)
    return qsort(smaller) + [pivot] + qsort(larger)

l = [49, 12, 67, 87, 21, 94, 24, 73, 69, 34]
print(qsort(l))
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(qsort(l))
l = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(qsort(l))
l = []
print(qsort(l))
l = [1]
print(qsort(l))
l = [1,2]
print(qsort(l))
l = [2,1]
print(qsort(l))
l = [3, 3, 3]
print(qsort(l))
