# Measure, don’t guess

To measure the absolute and relative amounts of time each block consumes
I’ve _instrumented_ the code. The term instrumentation derives from
pre-computer engineering practice where engineers would insert measuring
devices into the engine/mine/bridge they were working on to measure
salient characteristics. For us it means that we insert timers into our
program to measure how long each block takes to run. Here’s the
instrumented code,

``` python
creation_time = 0.0
aging_time = 0.0
copying_time = 0.0
for generation in range(0, generations):

    start = time.time()
    # Create next universe
    next_u = []
    for row in range(u_rows):
        next_u.append(u_cols*[0])
    end = time.time()
    creation_time += end - start

    start = time.time()
    # Age the universe:
    # Consider every cell in the universe
    for row in range(0, u_rows):
        for col in range(0, u_cols):    
            # Count its live neighbours
            neighbours = 0
            for r in range(row-1, row+2):
                for c in range(col-1, col+2):
                    if r >= u_rows: r = 0 # Handle toroidal universe
                    if c >= u_cols: c = 0 # Handle toroidal universe
                    neighbours += u[r][c]
            neighbours -= u[row][col]

            # Decide if it lives, dies or is born.
            if (u[row][col] == 1 and neighbours == 2) or neighbours == 3:
                next_u[row][col] = 1
    end = time.time()
    aging_time +=  end - start

    start = time.time()
    # Replace universe with next universe
    u = next_u
    end = time.time()
    copying_time += end - start
    
    # Display the new universe
    # display(u)

total_time = creation_time + aging_time + copying_time
print(f'total_time    : {total_time:5.2f}')
print(f'creation_time : {creation_time:5.2f} = {creation_time*100.0/total_time:5.2f}%')
print(f'aging_time    : {aging_time:5.2f} = {aging_time*100.0/total_time:5.2f}%')
print(f'copying_time  : {copying_time:5.2f} = {copying_time*100.0/total_time:5.2f}%')
```

And here’s the output it produces (100 generations of a 100x100
universe with random initialization of 42% live cells),

``` python
>>> 
u_rows = 100
u_cols = 100
generations = 100
live_pct = 42

total_time    :  7.73
creation_time :  0.01 =  0.10%
aging_time    :  7.72 = 99.83%
copying_time  :  0.01 =  0.06%
>>> 
```
