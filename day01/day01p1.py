# Advent of Code 2023
# Day 1, Part 1
# Finding two specific digits in a string 

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

def firstDigitIn(string) -> int:
    for element in string:
        if element.isdigit():
            return int(element)

# Find the sum of 10x the first digit and 1x the last digit 
def codesum(problem) -> int:
    subtotal = 0
    for scribble in problem.strings:
        subtotal += 10 * firstDigitIn(scribble) + firstDigitIn(reversed(scribble))
    return subtotal

def main():
    # Ingest and format the data
    t = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day01\\test.txt")
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day01\\input.txt")

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