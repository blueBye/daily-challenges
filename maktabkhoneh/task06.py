
def operation(number):
    result = ""
    half = [f"{(number - i)*' ' + (2 * i + 1) * '*'}" for i in range(number)]
    result += '\n'.join(half)
    result += f"\n{'*' * (2 * number + 1)}\n"
    half.reverse()
    result += '\n'.join(half)
    return result

def main():
    number = int(input())
    print(operation(number))

main()
# tests
assert operation(3) == "   *\n  ***\n *****\n*******\n *****\n  ***\n   *", "test 1 failed"
assert operation(4) == "    *\n   ***\n  *****\n *******\n*********\n *******\n  *****\n   ***\n    *", "test 2 failed"
assert operation(1) == " *\n***\n *", "test 3 failed"