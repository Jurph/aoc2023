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
            if seed in range(src, src + wdt):
                answer = (dst + wdt) - ((src + wdt) - seed)
                return int(answer)
        return seed

    def findDestinations(self, seed: int, span: int) -> list:
        seed = int(seed)
        span = int(span)
        return (self.findDestination(x) for x in range(seed, seed + span))
            
def MakeMap(rows: list) -> Map:
    rows = rows
    source = [None] * (len(rows))
    dest = [None] * (len(rows))
    width = [None] * (len(rows))
    for i, row in enumerate(rows):
        dest[i], source[i], width[i] = row.split(" ")
    return Map(source, dest, width)

@dataclass(frozen=True)
class Almanac(object):
    seeds: list[int]
    spans: list[int]
    maps: list[Map]

def MakeAlmanac(filename: str) -> Almanac:
    lines = open(filename).read().splitlines()
    lines.append("")
    planting = lines[0].split(" ")
    rows = []
    maps = []
    temp_list = []
    seeds = []
    spans = []
    for line in lines[1:]:
        if line == "":
            rows.append(temp_list[1:])
            temp_list = []
        else:
            temp_list.append(line)
    for r in rows[1:]:
        maps.append(MakeMap(r))
    for i, element in enumerate(planting[1:]):
        if i % 2 != 0:
            spans.append(int(element))
        else:
            seeds.append(int(element))
    return Almanac(seeds=seeds, spans=spans, maps=maps)

# Gets a list of planting instructions for each seed being planted
def getPlantingInstructions(a : Almanac) -> list:
    seedlist = []
    for i, s in enumerate(a.seeds):
        print("Considering {} seeds, hold on...".format(a.spans[i]))
        for m in a.maps:
            seedlist.append(list(m.findDestinations(seed=a.seeds[i], span=a.spans[i])))
    return seedlist

# Finds the seed whose final destination on the map is lowest 
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

    print(findNearestPlot(getPlantingInstructions(t)))
    print(findNearestPlot(getPlantingInstructions(p)))
 
if __name__ == "__main__":
    main()