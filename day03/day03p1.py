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

    def x(self) -> int:
        return self.squares[0].x

    def y(self) -> int:
        return self.squares[0].y

    def value(self) -> int:
        v = ''
        for s in self.squares:
            v += s.value
        return int(v)

    def neighbors(self) -> list:
        n = []
        for s in self.squares:
            n.append(s.findNeighbors())
        return n


@dataclass(frozen=True)
class Schematic(object):
    grid: list
    width: int
    height: int

    def print(self):
        print("==========")
        for subgrid in self.grid:
            rowstring = ''
            for g in subgrid:
                rowstring += str(g.value)
            print("{}".format(rowstring))
        print("==========")
        print("Grid of {} x {}".format(self.width, self.height))
    
    def parts(self) -> list:
        parts = []
        for row in self.grid:
            part = []
            for square in row:
                if square.value in '0123456789':
                    part.append(square)
                    print("Found a digit: {} - appending to part".format(square.value)) 
                elif len(part) == 0:
                    pass
                else:
                    parts.append(PartNumber(part))
                    print("Closed out a part: {}".format(parts[-1].value()))
                    part = []
        return parts

def MakeSchematic(filename: str) -> Schematic:
    squares = []
    width = 0
    height = 0
    # for (row, line) in enumerate(open(filename).read().splitlines()):
        # for (column, text) in enumerate(line):
    for (row, line) in enumerate(open(filename)):
        subgrid = []
        for (column, text) in enumerate(line.strip('\n')):
            if str(text) not in '1234567890.':
                text = 'X' # Indicates a connection point. Later we'll search for 'X' in PartNumber.neighbors 
            subgrid.append(GridSquare(x=column, y=row, value=text))
            width = max(width, column)
            height = max(height, row)
        squares.append(subgrid)
    return Schematic(grid=squares, width=width+1, height=height+1) # n.b. we are zero indexed

# def MakePartNumbers(s: Schematic) -> list:
#     parts = []
#     for row in s.grid:
#         print("New row:\n")
#         for square in row:
#             squares = []
#            if square.value in '0123456789':
#                squares.append(square)
#                print("Found a digit; adding {} to this part\n".format(square.value))
#            else:
#                print("Found a non-digit")
#                parts.append(PartNumber(squares))
#                squares = []
#    return parts


def main():
    # Ingest and format the input data
    t = MakeSchematic("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day03\\test.txt")
    p = MakeSchematic("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day03\\input.txt")

    print("TEST GRID:")
    t.print()
    print("\n")
    parts = t.parts()
    print("We've got {} parts:".format(len(parts)))
    for part in parts:
        print("Found a part: {}".format(part.value()))

    # print("REAL GRID:")
    # p.print()

    # Run the solvers against each problem 
    # print("TEST CASE: valid games = {}".format(doTheThing(t)))
    # print("PROD CASE: valid games = {}".format(doTheThing(p)))

if __name__ == "__main__":
    main()