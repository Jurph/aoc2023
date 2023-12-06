# Advent of Code 2023
# Day 5, Part 1
# Mapping seeds to fertilizer zones 

from dataclasses import dataclass

@dataclass(frozen=True)
class Map(object):
    source: list
    dest: list
    width: list

    def findDestination(self, seed: int) -> int:
        seed = int(seed)
        for (i, width) in enumerate(self.width):
            src = int(self.source[i])
            dst = int(self.dest[i])
            wdt = int(width)
            # print("Checking step {} of {}: Is {} between {} and {}?".format(i+1, len(self.width), seed, src, src + wdt))
            if seed in range(src, src + wdt):
                answer = (dst + wdt) - ((src + wdt) - seed)
                # print("YEP. Returning {} for seed {}".format(answer, seed))
                # print("SRC : {}  | DST: {}  | WDT: {}".format(src, dst, wdt))
                # print("SEED: {}  | OFF: {}  | ANS: {}".format(seed, dst-src, answer))
                return int(answer)
        # print("NOPE. Seed {} maps to itself.".format(seed))
        return seed
        
def MakeMap(rows: list) -> Map:
    rows = rows
    # print("Rows to be split: {}".format(rows))
    source = [None] * (len(rows))
    dest = [None] * (len(rows))
    width = [None] * (len(rows))
    for i, row in enumerate(rows):
        # print("Splitting row {} of {}: {}".format(i+1, len(rows), row))
        dest[i], source[i], width[i] = row.split(" ")
    # print("Sources for map: {}".format(source))
    return Map(source, dest, width)

@dataclass(frozen=True)
class Almanac(object):
    seeds: list[int]
    maps: list[Map]
   
def MakeAlmanac(filename: str) -> Almanac:
    lines = open(filename).read().splitlines()
    lines.append("")
    seeds = lines[0].split(" ")
    rows = []
    maps = []
    temp_list = []
    for line in lines[1:]:
        if line == "":
            rows.append(temp_list[1:])
            temp_list = []
        else:
            temp_list.append(line)
    for r in rows[1:]:
        # print("Making list of maps from rows: {}".format(r))
        maps.append(MakeMap(r))
    return Almanac(seeds=seeds[1:], maps=maps)

def getPlantingInstructions(a : Almanac) -> list:
    seedlist = []
    for s in a.seeds:
        tmp = [int(s)]
        # print("-------------------")
        # print("Evaluating seed: {}".format(s))
        for map in a.maps:
            # print("Evaluating map : {}".format(map))
            tmp.append(map.findDestination(tmp[-1]))
            # print("Seed {} goes to {}".format(s, seedlist[i][-1]))
        seedlist.append(tmp)
    return seedlist

def findNearestPlot(i : list) -> int:
    distances = []
    for seedlist in i:
        distances.append(int(seedlist[-1]))
        print(int(seedlist[-1]))
    return sorted(distances)[0]

def main():
    # Ingest and format the data
    t = MakeAlmanac("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day05\\test.txt")
    p = MakeAlmanac("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day05\\input.txt")

    print("Made an Almanac with {} maps and {} seeds:".format(len(t.maps),len(t.seeds)))
    print("Seeds: {}".format(t.seeds))
    print("Last Map: {}".format(t.maps[-1]))
    print(getPlantingInstructions(t))
    print(findNearestPlot(getPlantingInstructions(t)))

    print(findNearestPlot(getPlantingInstructions(p)))
    # Run the solvers against each problem 
    # print("TEST CASE: nearest plot = {}".format(findNearestPlot(getPlantingInstructions(t))))
    # print("PROD CASE: total score = {}".format(findNearestPlot(getPlantingInstructions(p))))

if __name__ == "__main__":
    main()