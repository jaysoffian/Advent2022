#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/6
"""
from functools import partial
from pathlib import Path

HERE = Path(__file__).parent
INPUT = (HERE / "input.txt").read_text()


def detect(seq, length):
    for i in range(len(seq)):
        if len(set(seq[i : i + length])) == length:
            return i + length
    return 0


part1 = partial(detect, length=4)
part2 = partial(detect, length=14)


def test():
    assert part1("abcd") == 4
    assert part1("aabbccddeeff") == 0
    assert part1("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert part1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert part1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11
    assert part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert part2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert part2("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert part2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert part2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26


def main():
    test()
    print(part1(INPUT))
    print(part2(INPUT))


if __name__ == "__main__":
    main()
