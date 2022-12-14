#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/13
"""
from functools import cmp_to_key
from pathlib import Path
from json import loads

HERE = Path(__file__).parent
SAMPLE = (HERE / "sample.txt").read_text().strip().splitlines()
INPUT = (HERE / "input.txt").read_text().strip().splitlines()


def isint(x):
    return isinstance(x, int)


def islist(x):
    return isinstance(x, list)


def compare(left, right, print=lambda *_: None, _depth=0):
    pad = "  " * _depth
    print(f"{pad}- Compare {left} vs {right}")
    if not islist(left):
        print(
            f"{pad}  - Mixed types; "
            "convert left to [{left}] and retry comparison"
        )
        return compare([left], right, print, _depth)
    if not islist(right):
        print(
            f"{pad}  - Mixed types; "
            "convert right to [{right}] and retry comparison"
        )
        return compare(left, [right], print, _depth)
    for x, y in zip(left, right):
        if isint(x) and isint(y):
            print(f"{pad}  - Compare {x} vs {y}")
            if x < y:
                print(
                    f"{pad}    - Left side is smaller, "
                    "so inputs are in the right order"
                )
                return -1
            if x > y:
                print(
                    f"{pad}    - Right side is smaller, "
                    "so inputs are NOT in the right order"
                )
                return 1
        elif rv := compare(x, y, print, _depth + 1):
            return rv

    if len(left) < len(right):
        print(
            f"{pad} - Left side ran out of items, "
            "so inputs are in the right order"
        )
        return -1
    elif len(left) > len(right):
        print(
            f"{pad}  - Right side ran out of items, "
            "so inputs are NOT in the right order"
        )
        return 1
    else:
        return 0


def part1(lines, print=lambda *_: None):
    packets = [loads(line) for line in lines if line]
    pairs = zip(packets[::2], packets[1::2])
    total = 0
    for i, (left, right) in enumerate(pairs, 1):
        print(f"== Pair {i} ==")
        if compare(left, right, print) < 0:
            total += i
        print()
    return total


def part2(lines, print=lambda *_: None):
    packets = [loads(line) for line in lines if line]
    d1 = [[2]]
    d2 = [[6]]
    packets.extend([d1, d2])
    packets.sort(key=cmp_to_key(compare))
    print("\n".join(str(p) for p in packets))
    return (packets.index(d1) + 1) * (packets.index(d2) + 1)


def test():
    assert part1(SAMPLE) == 13
    assert part2(SAMPLE) == 140


def main():
    test()

    assert part1(INPUT) == 5905
    print(part1(INPUT))

    assert part2(INPUT) == 21691
    print(part2(INPUT))


if __name__ == "__main__":
    main()
