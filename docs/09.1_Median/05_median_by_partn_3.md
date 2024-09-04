# Median by Partitioning: Version 3

Let's make sure that our function works on a wider variety of lists. As
always when picking tests make sure to consider some of the edge
conditions our function might encounter. Here we're going to really
think about duplicates.

```python
if __name__ == '__main__':
    lst = [37, 61, 42, 21, 19, 86, 95, 78, 54]
    print(median(lst))
    print(median([1])) # lists of length 1
    print(median([1, 42, 99]))
    print(median([1, 42, 42, 42, 99]))
    print(median([42, 42, 42, 42, 99]))

```

We haven't yet handled the cases where there are an even number of
elements in the list. That is an exercise for the assignment!