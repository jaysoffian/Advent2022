#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/4
"""
from pathlib import Path

HERE = Path(__file__).parent
# INPUT = (HERE / "sample.txt").read_text().strip()
INPUT = (HERE / "input.txt").read_text().strip()


def part1():
    total = 0
    for line in INPUT.splitlines():
        r1, r2 = line.split(",")
        x = tuple(map(int, r1.split("-")))
        y = tuple(map(int, r2.split("-")))
        if y < x:
            x, y = y, x
        if x[0] == y[0] or x[1] >= y[1]:
            total += 1
    assert total == 556, total
    print(total)


def part2():
    total = 0
    for line in INPUT.splitlines():
        r1, r2 = line.split(",")
        x = tuple(map(int, r1.split("-")))
        y = tuple(map(int, r2.split("-")))
        if y < x:
            x, y = y, x
        if x[0] <= y[0] <= x[1]:
            total += 1
    assert total == 876, total
    print(total)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
