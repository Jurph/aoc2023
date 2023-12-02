# Advent of Code 2023
# Day 1, Part 2
# Parsing a list of strings for digits, then summing them 

from dataclasses import dataclass

# Problem() is my class that ingests the day's input and structures it for easy computation
class Problem(object):
    def __init__(self, filename):
        strings = [] 
        lines = open(filename).read().splitlines()
        for line in lines:
            strings.append(line)
        self.strings = strings
        return

# Finds the first digit in a string 
def firstDigitIn(string):
    for element in string:
        if element.isdigit():
            return int(element)

def distill(string):
    # This weird dictionary ensures that overlapping pseudodigits are still
    # recoverable, e.g. `oneight` becomes `o1ei8ht` 
    digits = {'one':'o1e', 'two':'t2o', 'three':'t3e', 'four':'4', 'five':'f5ve','six':'s6x', 'seven':'se7en', 'eight':'ei8ht','nine':'ni9e'}
    for key in digits:
        while key in string:
            string = string.replace(key, digits[key])
    return string

# Find the sum of 10x the first digit in the string, and 1x the last digit in the string
# including pseudodigits, which we distill down to digits with distill() 
def codesum(problem):
    codesum = 0
    for scribble in problem.strings:
        scribble = distill(scribble)
        codesum += 10 * firstDigitIn(scribble) + firstDigitIn(reversed(scribble))
    return codesum

def main():
    # Ingest and format the data
    t = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day01\\test2.txt")
    p = Problem("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day01\\input.txt")

    # Set up state variables and run
    print("Sum of {} on test case.".format(codesum(t))) # Should output 281
    print("Sum of {} on real data.".format(codesum(p)))
    return

if __name__ == "__main__":
    main()