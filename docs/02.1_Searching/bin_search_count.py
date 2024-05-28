length = int(input('What is the list length? '))
times = 1
while length > 1:
    length = length//2
    times += 1
print('At most',times,'guesses.')

print('Length Times')
for length in range(100,2000,100):
    print(f'{length:6d}',end='')
    times = 1
    while length > 1:
        length = length//2
        times += 1
    print(f'{times:5d}')



print('Length Times')
for length in range(1000,10000,1000):
    print(f'{length:6d}',end='')
    times = 1
    while length > 1:
        length = length//2
        times += 1
    print(f'{times:5d}')


