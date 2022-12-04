import static java.lang.Integer.parseInt;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Main {

  public static List<String> readInput() {
    try {
      var path = (new File("input.txt")).toPath();
      return Files.readAllLines(path);
    } catch (IOException e) {
      throw new RuntimeException(e);
    }
  }

  public static void part1(List<String> input) {
    var elves = new ArrayList<Integer>();
    int calories = 0;
    for (String line : input) {
      if (line.isBlank()) {
        elves.add(calories);
        calories = 0;
      } else {
        calories += parseInt(line);
      }
    }
    System.out.println(Collections.max(elves));
  }

  public static void part2(List<String> input) {
    var elves = new ArrayList<Integer>();
    int cals = 0;
    for (String line : input) {
      if (line.isBlank()) {
        elves.add(cals);
        cals = 0;
      } else {
        cals += parseInt(line);
      }
    }
    Collections.sort(elves);
    int total = 0;
    for (var cals2 : elves.subList(elves.size() - 3, elves.size())) {
      total += cals2;
    }
    System.out.println(total);
  }

  public static void main(String[] args) {
    var input = readInput();
    part1(input);
    part2(input);
  }
}
