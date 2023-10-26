from collections import defaultdict 

def operation(color_dict):
    sorted_dict = dict(sorted(color_dict.items()))
    return min(sorted_dict, key=sorted_dict.get)

def main():
    count = int(input())
    color_dict = defaultdict(lambda: 0)
    for i in range(count):
        color_dict[input()] += 1
    print(operation(color_dict))

main()
# tests
assert operation({'1': 2, '2': 1}) == '2', "test 1 failed"
assert operation({'5': 1, '1': 2, '2': 1, '3': 1, '4': 1}) == '2', "test 2 failed"
assert operation({'6': 1, '4': 1, '8': 1}) == '4', "test 3 failed"
