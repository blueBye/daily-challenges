
def operation(n, k):
    return int(n / 2 ** k) % 10

def main():
    n = int(input())
    k = int(input())
    print(operation(n, k))


# tests
assert operation(17, 3) == 2, "test 1 failed"
assert operation(29, 4) == 1, "test 2 failed"
assert operation(213, 5) == 6, "test 3 failed"
