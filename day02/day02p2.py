# Advent of Code 2023
# Day 2, Part 1
# The elf's cube-choosing game 

from dataclasses import dataclass

class Game():
    def __init__(self, gamestring):
        gameindex = 0
        red = 0
        blu = 0
        grn = 0
        index, data = gamestring.split(':')
        gameindex = int(index[4:])
        draws = data.split(';')
        # print("Game {}: {} draws of cubes.".format(gameindex, len(draws)))
        for d in draws:
            draw = d.split(',')
            for cubes in draw:
                r = 0
                g = 0
                b = 0
                if " red" in cubes:
                    r = int(cubes.strip(" red"))
                elif " green" in cubes:
                    g = int(cubes.strip(" green"))
                elif " blue" in cubes:
                    b = int(cubes.strip(" blue"))
                else:
                    print("GLITCH: seems like you didn't draw any cubes?")
                    pass
                red = max(r, red)
                grn = max(g, grn)
                blu = max(b, blu)
        self.index = gameindex
        self.red = red
        self.grn = grn
        self.blu = blu
        self.isPossible = self.couldhappen()
        # A game's "power", per the problem statement for Part 2, is the 
        # product of the highest number of red, green, and blue cubes seen
        self.power = int(red * grn * blu)
        return 

    def couldhappen(self):
        # A game is "possible", per the problem statement for Part 1, if we've
        # never seen more than 12 red, 13 green, or 14 blue cubes 
        if (self.red <= 12) and (self.grn <= 13) and (self.blu <= 14):
            return True

# Problem() is my class that ingests the day's input and structures it for easy computation
class Problem():
    def __init__(self, filename):
        games = [] 
        lines = open(filename).read().splitlines()
        for line in lines:
            games.append(Game(line))
        self.games = games

def main():
    # Ingest and format the data
    t = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day02\\test.txt")
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day02\\input.txt")

    subtotal = 0
    for game in p.games:
        subtotal += game.power
    print("Total power: {}".format(subtotal))

if __name__ == "__main__":
    main()