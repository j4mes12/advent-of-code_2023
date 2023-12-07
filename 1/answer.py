import re


def part_one(filepath: str):
    sum_nums = 0
    with open(filepath, "rb") as file:
        for line in file:
            num = re.sub(r"\D", "", str(line))
            sum_nums += int(num[0] + num[-1])

    return sum_nums
