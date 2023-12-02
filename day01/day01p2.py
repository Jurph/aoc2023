# Advent of Code 2023
# Day 1, Part 2
# Parsing a list of strings for digits, then summing them 

from dataclasses import dataclass

# Problem() is my class that ingests the day's input and structures it for easy computation

class Problem():
    def __init__(self, filename):
        strings = [] 
        lines = open(filename).read().splitlines()
        for line in lines:
            strings.append(line)
        self.strings = strings
        return

def digitin(string):
    for element in string:
        if element.isdigit():
            # print("Found a digit: {}".format(element))
            return int(element)

def distill(string):
    newstring = string.replace('one','o1e')
    newstring = newstring.replace('two','t2o')
    newstring = newstring.replace('three','t3e')
    newstring = newstring.replace('four','4')
    newstring = newstring.replace('five','5ve')
    newstring = newstring.replace('six','s6x')
    newstring = newstring.replace('seven','s7en')
    newstring = newstring.replace('eight','ei8t')
    newstring = newstring.replace('nine','ni9e')
    return newstring

# Find the sum of 10x the first digit in the string, and 1x the last digit in the string
# including pseudodigits 
def codesum(problem):
    codesum = 0
    for scribble in problem.strings:
        scribble = distill(scribble)
        tens = digitin(scribble)
        ones = digitin(reversed(scribble))
        result = 10 * tens + ones
        # print("Got a result of {}".format(result))
        codesum += result 
    return codesum

def main():
    # Ingest and format the data
    t = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day01\\test2.txt")
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day01\\input.txt")

    # Set up state variables and run
    test = codesum(t)
    print("Sum of {} on test case.".format(test))
    if test == 281:
        print("...tests passed!")
        prod = codesum(p)
        print("Sum of {} on real data.".format(prod))
    return

if __name__ == "__main__":
    main()