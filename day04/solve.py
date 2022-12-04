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
        a, b = map(int, r1.split("-"))
        x, y = map(int, r2.split("-"))
        s1 = set(range(a, b + 1))
        s2 = set(range(x, y + 1))
        if s1.issubset(s2) or s2.issubset(s1):
            total += 1
    print(total)


def part2():
    total = 0
    for line in INPUT.splitlines():
        r1, r2 = line.split(",")
        a, b = map(int, r1.split("-"))
        x, y = map(int, r2.split("-"))
        s1 = set(range(a, b + 1))
        s2 = set(range(x, y + 1))
        if s1 & s2:
            total += 1
    print(total)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
