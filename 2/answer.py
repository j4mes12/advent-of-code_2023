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
    return 0


if __name__ == "__main__":
    part_one("2/test.txt")
