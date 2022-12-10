#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/10
"""
from pathlib import Path

HERE = Path(__file__).parent
SAMPLE = (HERE / "sample.txt").read_text().strip().splitlines()
INPUT = (HERE / "input.txt").read_text().strip().splitlines()


class Cpu:
    INSTRUCTIONS = {
        "noop": 1,
        "addx": 2,
    }

    def __init__(self):
        self.cycle = 1
        self.x = 1

    def run(self, lines):
        for line in lines:
            args = line.split()
            inst = args.pop(0)
            for _ in range(Cpu.INSTRUCTIONS[inst]):
                yield
                self.cycle += 1
            if inst == "addx":
                self.x += int(args[0])

    def __str__(self):
        return f"{self.cycle} {self.x}"


class Crt:
    def __init__(self):
        self.cycle = 0
        self.rows = [["."] * 40 for _ in range(6)]

    def tick(self, x):
        row, col = divmod(self.cycle, 40)
        lit = col - 1 <= x <= col + 1
        self.rows[row % 6][col] = "#" if lit else "."
        self.cycle += 1

    def __str__(self):
        return "\n".join("".join(row) for row in self.rows)


def part1(lines):
    total = 0
    cpu = Cpu()
    for _ in cpu.run(lines):
        if cpu.cycle in (20, 60, 100, 140, 180, 220):
            total += cpu.x * cpu.cycle
    return total


def part2(lines):
    cpu = Cpu()
    crt = Crt()
    for _ in cpu.run(lines):
        crt.tick(cpu.x)
    return str(crt)


def test1a():
    cpu = Cpu()
    for i, _ in enumerate(cpu.run(["noop", "addx 3", "addx -5"]), 1):
        # print(cpu)
        assert i == cpu.cycle
        assert (
            cpu.x
            == {
                1: 1,
                2: 1,
                3: 1,
                4: 4,
                5: 4,
                6: -1,
            }[i]
        )


def test1b():
    cpu = Cpu()
    total = 0
    for _ in cpu.run(SAMPLE):
        x = {
            20: 21,
            60: 19,
            100: 18,
            140: 21,
            180: 16,
            220: 18,
        }.get(cpu.cycle)
        assert x is None or cpu.x == x, f"{x} {cpu.x}"
        if x:
            total += cpu.x * cpu.cycle
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
    test2()

    print(part1(INPUT))
    assert part1(INPUT) == 16880

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
