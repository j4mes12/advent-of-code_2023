import re


def part_one(filepath: str) -> int:
    sum_nums = 0
    with open(filepath) as file:
        for line in file:
            num = re.sub(r"\D", "", line)
            sum_nums += int(num[0] + num[-1])

    return sum_nums


def part_two(filepath: str) -> int:
    num_chars = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    sum_nums = 0
    pattern = r"(?=(\d|" + "|".join(num_chars.keys()) + r"))"
    with open(filepath) as file:
        for line in file:
            num = re.findall(pattern, line)
            sum_nums += int(
                num_chars.get(num[0], num[0]) + num_chars.get(num[-1], num[-1]),
            )

    return sum_nums


if __name__ == "__main__":
    part_two("1/test.txt")
