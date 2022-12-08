#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/7
"""
from pathlib import Path
from collections import Counter
import re

HERE = Path(__file__).parent
INPUT = (HERE / "input.txt").read_text()
SAMPLE = (HERE / "sample.txt").read_text()

TOTAL_SPACE = 70000000
MIN_SPACE = 30000000


def ls_lr(lines):
    sizes = Counter()
    path = Path("/")
    for line in lines:
        if line.startswith("$ cd "):
            path = (path / line.split(maxsplit=2)[2]).resolve()
            # print(line)
            # print(path)
        elif m := re.search(r"^(\d+)", line):
            s = int(m.group(1))
            p = path
            sizes[str(p)] += s
            while str(p) != "/":
                p = p.parent
                sizes[str(p)] += s
    # print(sizes)
    return sizes


def part1(lines):
    sizes = ls_lr(lines)
    return sum(s for s in sizes.values() if s <= 100000)


def part2(lines):
    sizes = ls_lr(lines)
    unused = TOTAL_SPACE - sizes["/"]
    assert unused > 0
    needed = MIN_SPACE - unused
    assert needed > 0
    return min(s for s in sizes.values() if s > needed)


def test():
    lines = SAMPLE.splitlines()
    assert part1(lines) == 95437
    assert part2(lines) == 24933642


def main():
    test()
    lines = INPUT.splitlines()
    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
