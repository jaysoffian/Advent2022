#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/6
"""
from collections import deque
from functools import partial
from pathlib import Path

HERE = Path(__file__).parent
INPUT = (HERE / "input.txt").read_text()


def detect(seq, length):
    d = deque(maxlen=length)
    for i, ch in enumerate(seq, 1):
        d.append(ch)
        if len(set(d)) == length:
            return i
    return 0


part1 = partial(detect, length=4)
part2 = partial(detect, length=14)


def main():
    assert part1("abcd") == 4
    assert part1("aabbccddeeff") == 0
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
