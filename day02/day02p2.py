# Advent of Code 2023
# Day 2, Part 2
# The elf's cube-choosing game 

from dataclasses import dataclass

@dataclass(frozen=True)
class Game(object):
    index: int
    maxRed: int
    maxGreen: int
    maxBlue: int
    
    def couldHappen(self) -> bool:
        return (self.maxRed <= 12) and (self.maxGreen <= 13) and (self.maxBlue <= 14)

    def power(self) -> int:
        return self.maxRed * self.maxGreen * self.maxBlue 
    
def MakeGame(gamestring: str) -> Game:
    prefix, data = gamestring.strip().split(':')
    _, index = prefix.split()
    counts = {'red': 0, 'green': 0, 'blue': 0}
    for draw in data.split(';'):
        for count in draw.split(','):
            qty, color = count.split()
            counts[color] = max(counts[color], int(qty))
    return Game(index=int(index), maxRed=counts['red'], maxGreen=counts['green'], maxBlue=counts['blue'])

# Problem() is my class that ingests the day's input and structures it for easy computation
class Problem():
    def __init__(self, filename):
        games = [] 
        lines = open(filename).read().splitlines()
        for line in lines:
            games.append(MakeGame(line))
        self.games = games

# Sums the powers of games in a given problem 
def getPowerTotal(problem):
    subtotal = 0
    for game in problem.games:
        subtotal += game.power()
    return subtotal

# Sums the indices of valid games in a given problem 
def getValidGames(problem):
    subtotal = 0
    for game in problem.games:
        if game.couldHappen():
            subtotal += game.index
    return subtotal
    
def main():
    # Ingest and format the data
    t = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day02\\test.txt")
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day02\\input.txt")

    # Run the solvers against each problem 
    print("TEST CASE: valid games = {}, total power = {}".format(getValidGames(t), getPowerTotal(t)))
    print("PROD CASE: valid games = {}, total power = {}".format(getValidGames(p), getPowerTotal(p)))

if __name__ == "__main__":
    main()