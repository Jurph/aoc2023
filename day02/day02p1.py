# Advent of Code 2023
# Day 2, Part 1
# The elf's cube-choosing game 

from dataclasses import dataclass

# Problem() is my class that ingests the day's input and structures it for easy computation
class Game():
    def __init__(self, filename):
        games = [] 
        lines = open(filename).read().splitlines()
        for line in lines:
            games.append(line)        
        gameindex = 0
        redcubes = 0
        bluecubes = 0
        greencubes = 0
        for game in games:
            index, data = game.split(':')
            gameindex = int(index[4:])
            draws = data.split(';')
            print("Game {}: {} draws of cubes.".format(gameindex, len(draws)))


def main():
    # Ingest and format the data
    t = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day02\\test.txt")
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day02\\input.txt")

    # Set up state variables 
    test = codesum(t)
    print("Sum of {} on test case.".format(test))
    if test == 142:
        print("...tests passed!")
        prod = codesum(p)
        print("Sum of {} on real data.".format(prod))
    return

if __name__ == "__main__":
    main()