
u = [ 
     [0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [0, 0, 0, 0, 0],
    ]

##u_rows = len(u)
##u_cols = len(u[0])
##
##LIVE_CELL = '@'
##DEAD_CELL = '-'
##
##fname = raw_input('Name of file to store universe in: ')
##outfile = open(fname, 'w')
##for row in range(u_rows):
##    for col in range(u_cols):
##        if u[row][col] == 1:
##            outfile.write(LIVE_CELL+' ')
##        elif u[row][col] == 0:
##            outfile.write(DEAD_CELL+' ')
##    outfile.write('\n')
##outfile.close()
##
##fname = raw_input('Name of file to store universe in: ')
##outfile = open(fname, 'w')
##for row in universe:
##    for cell in row:
##        outfile.write(str(cell))
##        outfile.write(' ')
##    outfile.write('\n')
##outfile.close()
##
fname = raw_input('Name of file to store universe in: ')
outfile = open(fname, 'w')
outfile.write(str(u))
outfile.close()
##
infile = open(fname, 'r')
input_line = infile.read()
u = eval(input_line)
print u
print type(u)
##
##Options:
##    a : Age universe one generation
##    m : Age universe multiple generations
##    s : Save universe to disk
##    l : Load universe from disk
##    q : Quit program
##
##Command (a|m|s|l):

print 'Done.'
