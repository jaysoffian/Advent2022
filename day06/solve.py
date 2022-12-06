#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/6
"""
from collections import deque
from functools import partial
from pathlib import Path

HERE = Path(__file__).parent
INPUT = (HERE / "input.txt").read_text()


def detect(line, length):
    d = deque(line[:length], length)
    for i, ch in enumerate(line[length:], length):
        if len(set(d)) == length:
            break
        d.append(ch)
    return i


part1 = partial(detect, length=4)
part2 = partial(detect, length=14)


def main():
    assert part1("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert part1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert part1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11
    print(part1(INPUT))

    assert part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert part2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert part2("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert part2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert part2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
    print(part2(INPUT))


if __name__ == "__main__":
    main()
