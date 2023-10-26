
def operation(num_1, num_2, operator):
    if operator == '+':
        return num_1 + num_2
    return num_1 - num_2

def main():
    num_1 = int(input())
    operator = input()
    num_2 = int(input())
    operation(num_1, num_2, operator)


# tests
assert operation(8, 9, '+') == 17, "test 1 failed"
assert operation(110, 97, '-') == 13, "test 2 failed"
assert operation(1000, 1, '-') == 999, "test 3 failed"
