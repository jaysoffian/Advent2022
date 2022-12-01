#!/opt/homebrew/bin/python3
"""
https://adventofcode.com/2022/day/1


"""
from pathlib import Path

HERE = Path(__file__).parent
# INPUT = (HERE / "sample.txt").read_text()
INPUT = (HERE / "input.txt").read_text()


def part1():
    elves = [0]
    for line in INPUT.splitlines():
        if line:
            elves[-1] += int(line)
        else:
            elves.append(0)
    # print(elves)
    print(max(elves))


def part2():
    elves = [0]
    for line in INPUT.splitlines():
        if line:
            elves[-1] += int(line)
        else:
            elves.append(0)
    # print(elves)
    top_3 = sorted(elves)[-3:]
    print(sum(top_3))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
