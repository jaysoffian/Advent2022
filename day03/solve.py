#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/3
"""
from pathlib import Path
from string import ascii_letters

HERE = Path(__file__).parent
# INPUT = (HERE / "sample.txt").read_text().strip()
INPUT = (HERE / "input.txt").read_text().strip()


def part1():
    total = 0
    for line in INPUT.splitlines():
        line = line.strip()
        half_len = len(line) // 2
        a, b = line[:half_len], line[half_len:]
        common = list(set(a) & set(b))
        assert len(common) == 1
        c = common[0]
        p = ascii_letters.index(c) + 1
        # print(c, p)
        total += p
    print(total)


def part2():
    total = 0
    group = []
    for line in INPUT.splitlines():
        group.append(line.strip())
        if len(group) < 3:
            continue
        common = list(set(group[0]) & set(group[1]) & set(group[2]))
        group = []
        assert len(common) == 1
        c = common[0]
        p = ascii_letters.index(c) + 1
        # print(c, p)
        total += p
    print(total)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
