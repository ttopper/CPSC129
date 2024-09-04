# subset.py
fullset = ['A', 'B', 'C']
subset_num = 6 # i.e. 110 or the subset with A and B
subset = []
for i in range(len(fullset)): # i.e. i in [0, 1, 2]
    if subset_num & (2**i): # i.e. 6 & 2^0=1 then 6 & 2^1=2 and finally 6 & 2^2=4
        subset.append(fullset[i])
print subset
