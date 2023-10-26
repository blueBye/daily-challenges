
def operation(number):
    if number == number[::-1]:
        return 'yes'
    return 'no'

def main():
    number = str(int(input()))
    print(operation(number))


# tests
assert operation("1537351") == "yes", "test 1 failed"
assert operation("00100") == "no", "test 2 failed"  # wrong testcase?
assert operation("23") == "no", "test 3 failed" 
