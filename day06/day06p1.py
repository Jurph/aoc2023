# Advent of Code 2023
# Day 6, Part 1
# Boat Races ("Wait for it")

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
        maps.append(MakeMap(r))
    return Almanac(seeds=seeds[1:], maps=maps)


def main():
    # Ingest and format the data
    t = MakeAlmanac("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day05\\test.txt")
    p = MakeAlmanac("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day05\\input.txt")

    print(findNearestPlot(getPlantingInstructions(t)))
    print(findNearestPlot(getPlantingInstructions(p)))
 
if __name__ == "__main__":
    main()