#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/12
"""
import math
from collections import namedtuple
from pathlib import Path
from string import ascii_lowercase

from dijkstra import DijkstraSPF, Graph

HERE = Path(__file__).parent
SAMPLE = (HERE / "sample.txt").read_text().strip().splitlines()
INPUT = (HERE / "input.txt").read_text().strip().splitlines()


Node = namedtuple("Node", "row col char")


def parse_maze(lines):
    start, end = None, None
    nodes = {}
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "S":
                nodes[row, col] = start = Node(row, col, "a")
            elif char == "E":
                nodes[row, col] = end = Node(row, col, "z")
            else:
                assert char in ascii_lowercase
                nodes[row, col] = Node(row, col, char)

    graph = Graph()
    for row, col in nodes:
        src = nodes[row, col]
        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dst = nodes.get((row + i, col + j))
            if dst and ord(dst.char) - ord(src.char) <= 1:
                graph.add_edge(dst, src, 1)

    return start, end, graph, [n for n in nodes.values() if n.char == "a"]


def part1(lines):
    start, end, graph, _ = parse_maze(lines)
    spf = DijkstraSPF(graph, end)
    return spf.get_distance(start)


def part2(lines):
    _, end, graph, starts = parse_maze(lines)
    spf = DijkstraSPF(graph, end)
    for start in starts:
        shortest_len = min(shortest_len, spf.get_distance(start))
    return shortest_len


def test():
    assert part1(SAMPLE) == 31
    assert part2(SAMPLE) == 29


def main():
    test()

    part1_answer = part1(INPUT)
    assert part1_answer == 408
    print(part1_answer)

    part2_answer = part2(INPUT)
    assert part2_answer == 399
    print(part2_answer)


if __name__ == "__main__":
    main()
