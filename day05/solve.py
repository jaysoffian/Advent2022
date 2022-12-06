#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/5
"""
from pathlib import Path
import re

HERE = Path(__file__).parent
INPUT = (HERE / "sample.txt").read_text()
INPUT = (HERE / "input.txt").read_text()


def line_iter():
    for line in INPUT.splitlines():
        yield line


def parse_stacks():
    stacks, columns = [], []
    # search for " 1 2 3 " line to figure out number
    # of stacks and column position for each stack.
    for line in line_iter():
        if not re.search(r"^ \d", line):
            continue
        num_stacks = int(line.split()[-1])
        for i in range(num_stacks):
            stacks.append([])
            columns.append(line.index(f"{i+1}"))

    # populate stacks
    lines = line_iter()
    for line in lines:
        if not line:
            break
        # 0123456789
        # [Z] [M] [P]
        if "[" in line:
            for i, j in enumerate(columns):
                c = line[j]
                if c != " ":
                    stacks[i].append(c)
    for stack in stacks:
        stack.reverse()

    return stacks, lines


def move_iter(stacks, lines):
    for line in lines:
        match = re.search(r"^move (\d+) from (\d+) to (\d+)", line)
        n, x, y = map(int, match.groups())
        yield n, stacks[x - 1], stacks[y - 1]


def part1():
    stacks, lines = parse_stacks()
    for n, src, dst in move_iter(stacks, lines):
        dst.extend(reversed(src[-n:]))
        src[:] = src[:-n]
    print("".join(stack[-1] for stack in stacks))


def part2():
    stacks, lines = parse_stacks()
    for n, src, dst in move_iter(stacks, lines):
        dst.extend(src[-n:])
        src[:] = src[:-n]
    print("".join(stack[-1] for stack in stacks))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
