#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/10
"""
from pathlib import Path

HERE = Path(__file__).parent
SAMPLE = (HERE / "sample.txt").read_text().strip().splitlines()
INPUT = (HERE / "input.txt").read_text().strip().splitlines()


class Cpu:
    def __init__(self, lines):
        self.lines = lines
        self.x = 1

    def __iter__(self):
        for i, line in enumerate(self.lines, 1):
            args = line.split()
            inst = args[0]
            if inst == "noop":
                assert len(args) == 1, f"{i}: {line!r}"
                yield self.x
            elif inst == "addx":
                assert len(args) == 2, f"{i}: {line!r}"
                yield self.x
                yield self.x
                self.x += int(args[1])
            else:
                assert False, f"{i}: {line!r}"
        yield self.x


class Crt:
    def __init__(self, cpu, num_rows=6, num_cols=40):
        self.rows = [["."] * num_cols for _ in range(num_rows)]
        for i, x in zip(range(0, num_rows * num_cols), cpu):
            row, col = divmod(i, num_cols)
            lit = col - 1 <= x <= col + 1
            self.rows[row % num_rows][col] = "#" if lit else "."

    def __str__(self):
        return "\n".join("".join(row) for row in self.rows)


def part1(lines):
    total = 0
    for i, x in enumerate(Cpu(lines), 1):
        if i in range(20, 221, 40):
            total += i * x
    return total


def part2(lines):
    return str(Crt(Cpu(lines)))


def test1a():
    ops = ["noop", "addx 3", "addx -5"]
    expect = [1, 1, 1, 4, 4, -1]
    for x, y in zip(expect, Cpu(ops)):
        assert x == y


def test1b():
    total = 0
    expect = dict(zip(range(20, 221, 40), [21, 19, 18, 21, 16, 18]))
    for i, x in enumerate(Cpu(SAMPLE), 1):
        if i in expect:
            assert x == expect[i], f"i={i}"
            total += i * x
    assert i == 241
    assert total == 13140, total
    assert part1(SAMPLE) == 13140, part1(SAMPLE)


def test2():
    expect = """
    ##..##..##..##..##..##..##..##..##..##..
    ###...###...###...###...###...###...###.
    ####....####....####....####....####....
    #####.....#####.....#####.....#####.....
    ######......######......######......####
    #######.......#######.......#######.....
    """
    expect = "\n".join(line.strip() for line in expect.strip().splitlines())
    assert str(part2(SAMPLE)) == expect


def main():
    test1a()
    test1b()
    print(part1(INPUT))
    assert part1(INPUT) == 16880

    test2()
    print(part2(INPUT))
    expect = """
    ###..#..#..##..####..##....##.###..###..
    #..#.#.#..#..#....#.#..#....#.#..#.#..#.
    #..#.##...#..#...#..#..#....#.###..#..#.
    ###..#.#..####..#...####....#.#..#.###..
    #.#..#.#..#..#.#....#..#.#..#.#..#.#.#..
    #..#.#..#.#..#.####.#..#..##..###..#..#.
    """
    expect = "\n".join(line.strip() for line in expect.strip().splitlines())
    assert part2(INPUT) == expect


if __name__ == "__main__":
    main()
