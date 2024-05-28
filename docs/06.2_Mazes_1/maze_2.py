# maze_2.py
#
# A Maze an array of Cells, each of which has four Walls, and may or may not have been visited.

(INT, EXT, DOOR) = list(range(3))
class Wall:
    def __init__(self, s):
        self.state = s

    def __str__(self):
        s = ''
        if self.state == INT:
            s += 'I'
        elif self.state == EXT:
            s += 'E'
        elif self.state == DOOR:
            s += 'D'
        return s
            

class Cell:
    def __init__(self, n, e, s, w):
        self.north = n
        self.east = e
        self.south = s
        self.west = w
        self.visited = False

    def __str__(self):
        s = ''
        s += str(self.north)
        s += str(self.east)
        s += str(self.south)
        s += str(self.west)
        if self.visited: s += 'V'
        else: s += 'U'
        s += ' '
        return s

class Maze:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.cells = []
        for r in range(self.height):
            # Build a row of cells and append it to self.cells
            row = []
            for c in range(self.width):
                if r == 0: # Top row
                    if c == 0:
                        row.append( Cell(Wall(EXT), Wall(INT), Wall(INT), Wall(EXT)))
                    elif c == self.width - 1:
                        row.append( Cell(Wall(EXT), Wall(EXT), Wall(INT), row[c-1].east))                       
                    else:
                        row.append( Cell(Wall(EXT), Wall(INT), Wall(INT), row[c-1].east))
                elif r == self.height - 1: # Bottom row
                    if c == 0:
                        row.append( Cell(self.cells[r-1][c].south, Wall(INT), Wall(EXT), Wall(EXT)))
                    elif c == self.width - 1:
                        row.append( Cell(self.cells[r-1][c].south, Wall(EXT), Wall(EXT), row[c-1].east))                       
                    else:
                        row.append( Cell(self.cells[r-1][c].south, Wall(INT), Wall(EXT), row[c-1].east))
                else: # Interior row
                    if c == 0:
                        row.append( Cell(self.cells[r-1][c].south, Wall(INT), Wall(INT), Wall(EXT)))
                    elif c == self.width - 1:
                        row.append( Cell(self.cells[r-1][c].south, Wall(EXT), Wall(INT), row[c-1].east))                       
                    else:
                        row.append( Cell(self.cells[r-1][c].south, Wall(INT), Wall(INT), row[c-1].east))
            self.cells.append(row)

    def __str__(self):
        s = ''
        for r in range(self.height):
            for c in range(self.width):
                s += str(self.cells[r][c])
            s += '\n'
        return s

    def carve(self):
        pass

    def display(self):
        pass

if __name__ =='__main__':
    m = Maze(5,5)
    m.carve()
    m.display()
    print(m)
    m.cells[1][1].east.state = DOOR
    m.cells[0][2].north.state = DOOR
    m.cells[2][3].south.state = DOOR
    print(m)
   
        
##  ==============
##||  |  |  |  |  ||
##||--+--+--+--+--||
##||  |  D  |  |  ||
##||--+--+--+--+--||
##||  |  |  |  |  ||
##||--+--+--+--+--||
##||  |  |  |  |  ||
##||--+--+--+--+--||
##||  |  |  |  |  ||
##  ==============
