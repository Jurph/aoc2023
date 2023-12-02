# Advent of Code 2023
# Day 1, Part 1
# Parsing a list of strings for digits, then summing them 

from dataclasses import dataclass
DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

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
            print("Found a digit: {}".format(element))
            return int(element)

def distill(string):
    newstring = string.replace('one','1')
    newstring = newstring.replace('two','2')
    newstring = newstring.replace('three','3')
    newstring = newstring.replace('four','4')
    newstring = newstring.replace('five','5')
    newstring = newstring.replace('six','6')
    newstring = newstring.replace('seven','7')
    newstring = newstring.replace('eight','8')
    newstring = newstring.replace('nine','9')
    return newstring

# Find the total calories carried by all the elves 
def codesum(problem):
    codesum = 0
    for scribble in problem.strings:
        tens = digitin(scribble)
        ones = digitin(reversed(scribble))
        result = 10 * tens + ones
        print("Got a result of {}".format(result))
        codesum += result 
    return codesum

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