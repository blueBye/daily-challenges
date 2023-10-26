import re


def operation(raw_input):
    count = len(re.findall('[LXTN]', raw_input))
    return 2 ** count

def main():
    raw_input = input()
    print(operation(raw_input))

# tests
assert operation("MAKTABSHARIF") == 2, "test 1 failed"
assert operation("CODINGBOOTCAMP") == 4, "test 2 failed"
assert operation("TEHRAN-IRAN") == 8, "test 3 failed"