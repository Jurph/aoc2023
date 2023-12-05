# Advent of Code 2023
# Day 4, Part 2
# Scratch-off tickets for the Elf Lottery
# ...now with recursive bonus winnings!

from dataclasses import dataclass

@dataclass(frozen=True)
class Game(object):
    index: int
    winners: set
    draws: set    

    def score(self) -> int:
        return int(len(self.winners.intersection(self.draws)))
   
def MakeGame(gamestring: str) -> Game:
    # Each line of the game string is of the format: 
    # Game N : a e i o u | a b c d e f g h i j 
    # where the Game N winning numbers are left of the "|"
    # and the numbers you drew are to the right. 
    # Score is calculated based on the intersection of the two.
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

# Sums the number of bonus tickets generated by each ticket with a win, using the following rules:
# A ticket numbered "N" with a score of 4 creates a copy of tickets N+1, N+2, N+3, and N+4,
# then each of the two copies of ticket N+1 create a copy of tickets N+2... based on the score of ticket N+1,
# and so on down the line. No ticket will ever create copies of tickets that don't exist. 

def getScoringTickets(problem) -> int:
    scores = []
    for game in problem.games:
        scores.append(game.score())
    cards = [1]*len(scores)
    # print("Starting with cards {}".format(cards))
    for j, score in enumerate(scores):
        # print("Card {} has a score of {}...".format(j, score))
        for i in range(1, score+1):
            cards[j+i] += cards[j]
            # print("Each of {} copies of card number {} generates a copy of card {}".format(cards[j], j, j+i))
    ticketsum = 0
    for c in cards:
        ticketsum += int(c)
    return ticketsum

    
def main():
    # Ingest and format the data
    t = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day04\\test.txt")
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day04\\input.txt")

    # Run the solvers against each problem 
    print("TEST CASE: total score = {}".format(getScoringTickets(t)))
    print("PROD CASE: total score = {}".format(getScoringTickets(p)))

if __name__ == "__main__":
    main()