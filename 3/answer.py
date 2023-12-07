import re


def part_one(filepath: str) -> int:
    sum_val = 0
    record, prev_digit_coords, prev_symbol_coords = [], [], []

    with open(filepath) as file:
        for line_num, line in enumerate(file):
            digit_matches = re.finditer(r"\d+", line)
            symbol_matches = re.finditer(r"[^\.\d\s]", line)
            digits_coords = [
                (match.group(), match.start(), match.end()) for match in digit_matches
            ]
            symbol_coords = [(match.group(), match.start()) for match in symbol_matches]

            if symbol_coords:
                for _, sc in symbol_coords:
                    if digits_coords:
                        for num, start, end in digits_coords:
                            if (sc == start - 1 or sc == end) and (num not in record):
                                sum_val += int(num)
                                record.append(num)

                    if line_num > 0 and prev_digit_coords != []:
                        for num, start, end in prev_digit_coords:
                            if sc >= start - 1 and sc <= end and num not in record:
                                sum_val += int(num)
                                record.append(num)

            if digits_coords and line_num > 0 and prev_symbol_coords:
                for num, start, end in digits_coords:
                    for _, sc in prev_symbol_coords:
                        if sc >= start - 1 and sc <= end and num not in record:
                            sum_val += int(num)
                            record.append(num)

            # update prev coords of digits
            prev_digit_coords = digits_coords
            prev_symbol_coords = symbol_coords

    return sum_val
