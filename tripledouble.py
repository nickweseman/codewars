import re


def triple_double(num1, num2):
    digits = [match.group(1) for match in re.finditer(r"([0-9]){3}", str(num1))]

    for digit in digits:
        if re.search(digit + r"{2}", str(num2)):
            return 1
    return 0


print(triple_double(451999277, 41177722899))
print(triple_double(1222345, 12345))
print(triple_double(12345, 12345))
print(triple_double(666789, 12345667))
print(triple_double(10560002, 100))
