import re
from typing import Dict


def part_one(filepath: str, max_balls: Dict[str, int]):
    idx_sum = 0
    pattern = r"(\d+)\s(blue|red|green)"
    with open(filepath) as file:
        for idx, line in enumerate(file):
            row_possible = True
            balls = {"red": 0, "blue": 0, "green": 0}
            catches = re.findall(pattern, line)
            for count, ball_color in catches:
                if row_possible:
                    balls[ball_color] += int(count)
                    row_possible = balls[ball_color] <= max_balls[ball_color]

            if row_possible:
                idx_sum += idx + 1

    return idx_sum
