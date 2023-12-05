# Advent of Code 2023
# Day 4, Part 1
# Scratch-off tickets for the Elf Lottery

from dataclasses import dataclass

@dataclass(frozen=True)
class Game(object):
    index: int
    winners: set
    draws: set    

    def score(self) -> int:
        return int(2**((len(self.winners.intersection(self.draws)))-1))
   
def MakeGame(gamestring: str) -> Game:
    prefix, data = gamestring.strip().split(':')
    _, index = prefix.split()
    left, right = data.split("|")
    winners = set(left.split())
    draws = set(right.split())

    return Game(index=int(index), winners=winners, draws=draws)

# Problem() is my class that ingests the day's input and structures it for easy computation
class Problem():
    def __init__(self, filename):
        games = [] 
        lines = open(filename).read().splitlines()
        for line in lines:
            games.append(MakeGame(line))
        self.games = games

# Sums the scores of winning tickets 
def getTotalScore(problem):
    subtotal = 0
    for game in problem.games:
        subtotal += game.score()
    return subtotal
    
def main():
    # Ingest and format the data
    t = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day04\\test.txt")
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day04\\input.txt")

    # Run the solvers against each problem 
    print("TEST CASE: total score = {}".format(getTotalScore(t)))
    print("PROD CASE: total score = {}".format(getTotalScore(p)))

if __name__ == "__main__":
    main()