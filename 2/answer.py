import re


def part_one(filepath: str) -> int:
    idx_sum = 0
    pattern = r"(\d+)\s(blue|red|green)"
    max_balls = {"red": 12, "green": 13, "blue": 14}
    with open(filepath) as file:
        for idx, line in enumerate(file):
            game_possible = True
            catches = re.findall(pattern, line)
            for count, ball_color in catches:
                if game_possible:
                    game_possible = int(count) <= max_balls[ball_color]

                if not game_possible:
                    break

            if game_possible:
                idx_sum += idx + 1

    return idx_sum


def part_two(filepath: str) -> int:
    set_power = 0
    pattern = r"(\d+)\s(blue|red|green)"
    with open(filepath) as file:
        for line in file:
            power = 1
            max_balls = {"red": 0, "green": 0, "blue": 0}
            catches = re.findall(pattern, line)
            for count, color in catches:
                count_int = int(count)
                if count_int > max_balls[color]:
                    max_balls[color] = count_int

            for color, count_int in max_balls.items():
                power *= count_int

            set_power += power

    return set_power


if __name__ == "__main__":
    part_one("2/test.txt")
