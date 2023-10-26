
def operation(numbers):
    result = {
        'max': max(numbers),
        'min': min(numbers),
        'avg': sum(numbers)/len(numbers),
    }

    return '\n'.join([f"{k}: {v:.3f}" for k, v in result.items()])

def main():
    count = int(input())
    numbers = [float(input()) for _ in range(count)]
    print(operation(numbers))    


# tests
assert operation([3.27]) == "max: 3.270\nmin: 3.270\navg: 3.270", "test 1 failed"
assert operation([3, 7.009, 4.2, 3.3, 2, 1.01]) == "max: 7.009\nmin: 1.010\navg: 3.420", "test 2 failed"
# test 3 was wrong - check max