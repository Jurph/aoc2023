# Advent of Code 2023
# Day 3, Part 1
# Sum of part numbers adjacent to "symbols"

from dataclasses import dataclass

# We represent a Grid Square as an object that can search for its neighbors
@dataclass(frozen=True)
class GridSquare(object):
    x: int
    y: int
    value: str

    def __str__(self):
        return str(self.value)

    def findNeighbors(self):
        neighbors = []
        row, col = self.x, self.y
        if row == 0:
            neighbors.append([row + 1, col])
        elif row == self.height-1:
            neighbors.append([row - 1, col])
        else:
            neighbors.append([row + 1, col])
            neighbors.append([row - 1, col])

        if col == 0:
            neighbors.append([row, col + 1])
        elif col == self.width - 1:
            neighbors.append([row, col - 1])
        else:
            neighbors.append([row, col + 1])
            neighbors.append([row, col - 1])
        return neighbors

@dataclass(frozen=True)
class PartNumber:
    squares: list

    def value(self) -> int:
        v = ''
        for s in self.squares:
            v += s.value
        return int(v)


@dataclass(frozen=True)
class Schematic(object):
    grid: list
    width: int
    height: int
    rowstrings: list

    def print(self):
        print("==========")
        for r in self.rowstrings:
            print(r)
        print("==========")
        rowstring = ''
        for g in self.grid:
            rowstring += str(g.value)
            if ((g.x)+1 % int(self.width)) == self.width:
                 print("{}".format(rowstring))
                 rowstring = ''
        print("==========")
        print("Grid of {} x {}".format(self.width, self.height))

def MakeSchematic(filename: str) -> Schematic:
    squares = []
    rowstrings = []
    width = 0
    height = 0
    for (row, line) in enumerate(open(filename).read().splitlines()):
        for (column, text) in enumerate(line):
            if str(text) not in '1234567890.':
                text = 'P'
            squares.append(GridSquare(x=column, y=row, value=text))
            # TODO: may need to put safety features on that string in case the value is '\'
            width = max(width, column)
            height = max(height, row)
        rowstrings.append(line)
    return Schematic(grid=squares, width=width+1, height=height+1, rowstrings=rowstrings) # n.b. we are zero indexed


def main():
    # Ingest and format the input data
    t = MakeSchematic("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day03\\test.txt")
    p = MakeSchematic("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day03\\input.txt")

    print("TEST GRID:")
    t.print()
    print("REAL GRID:")
    p.print()

    # Run the solvers against each problem 
    # print("TEST CASE: valid games = {}".format(doTheThing(t)))
    # print("PROD CASE: valid games = {}".format(doTheThing(p)))

if __name__ == "__main__":
    main()