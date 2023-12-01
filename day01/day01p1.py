# Advent of Code 2023
# Day 1, Part 1
# Parsing a list of strings for digits, then summing them 

from dataclasses import dataclass

# Problem() is my class that ingests the day's input and structures it for easy computation

class Problem():
    def __init__(self, filename):
        strings = [] # We don't need strings in this chapter but it's a neat feature
        integers = []
        lines = open(filename).read().splitlines()
        for line in lines:
            strings.append(line)
            try:
                integers.append(int(line))
            except(ValueError):
                integers.append(int(0))
        self.strings = strings
        self.integers = integers
        return

def digitin(string):
    for element in string:
        if element.isdigit():
            return element
        else:
            print("GLITCH: no digits found")
            return -1

# Find the total calories carried by all the elves 
def codesum(problem):
    codesum = 0
    for scribble in problem.strings:
        tens = digitin(scribble)
        ones = digitin(reversed(scribble))
        result = 10 * tens + ones
        codesum += result 
    return codesum

def main():
    # Ingest and format the data
    t = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day01\\test.txt")
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day01\\input.txt")

    # Set up state variables 
    test = codesum(t)
    if test == 77:
        print("Test passed: sum of [] on test case.".format(test))
    return

if __name__ == "__main__":
    main()