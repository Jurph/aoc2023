# Advent of Code 2023
# Day 6, Part 1
# Boat Races ("Wait for it")

from dataclasses import dataclass

@dataclass(frozen=True)
class Schedule(object):
    races: list[int]

def MakeSchedule(filename: str) -> Schedule:
    t, d = open(filename).read().splitlines()
    time = list(map(int, t.split()[1:]))
    dist = list(map(int, d.split()[1:]))
    return Schedule(races = zip(time, dist))

def distanceTraveled(holdtime: int, totaltime: int) -> int:
    if (holdtime % 10 == 0):
        print("Holding for {} seconds; coasting {} meters.".format(holdtime, (holdtime * (totaltime - holdtime))))
    return (holdtime * (totaltime - holdtime))

def isWinner(race: list, holdtime: int) -> bool:
    totaltime, distance = race[0], race[1]
    return (distanceTraveled(holdtime=holdtime, totaltime=totaltime) > distance)

def countWinners(s: Schedule) -> int:
    wins = 1
    for race in s.races:
        print("This race is trying to beat a record of {} meters with a total duration of {} seconds.".format(race[1], race[0]))
        winners = 0
        for holdtime in range(0, race[0]+1):
            if isWinner(race=race, holdtime=holdtime):
                winners += 1
                if winners == 1:
                    print("First winner is at {} seconds and a record of {} meters.".format(holdtime, distanceTraveled(holdtime, race[0])))
        print("Found {} winners in this race after trying all combinations up to {} seconds".format(winners, race[0]))
        wins *= winners
    return wins


def main():
    # Ingest and format the data
    t = MakeSchedule("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day06\\test.txt")
    p = MakeSchedule("C:\\Users\\Jurph\\Documents\\Python Scripts\\aoc2023\\day06\\input.txt")

    print(countWinners(t))
    print(countWinners(p))
 
if __name__ == "__main__":
    main()