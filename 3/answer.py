import re


def part_one(filepath: str) -> int:
    sum_val = 0
    record, previous_digit_coords, previous_symbol_coords = [], [], []

    with open(filepath) as file:
        for line in file:
            digits_coords = [
                (match.group(), match.start(), match.end())
                for match in re.finditer(r"\d+", line)
            ]
            symbol_coords = [match.start() for match in re.finditer(r"[^\.\d\s]", line)]

            matching_digits = [
                coords
                for coords in previous_digit_coords + digits_coords
                if coords not in record
            ]

            matching_symbols = [
                coords
                for coords in previous_symbol_coords + symbol_coords
                if coords not in record
            ]

            if matching_symbols and matching_digits:
                for num, start, end in matching_digits:
                    for sym_coords in matching_symbols:
                        if sym_coords < start - 1:
                            continue
                        if sym_coords >= start - 1 and sym_coords <= end + 1:
                            sum_val += int(num)
                            record.append((num, start, end))
                            break

            # Update previous coordinates of digits and symbols
            previous_digit_coords = digits_coords
            previous_symbol_coords = symbol_coords

    return sum_val


if __name__ == "__main__":
    result = part_one("3/test.txt")
    print(result)
