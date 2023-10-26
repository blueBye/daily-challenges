
def operation(people: list[str]):
    dialogs = []
    for idx in range(len(people)):
        dialogs.extend([f"{people[idx]}: salam {people[i]}!" for i in range(idx-1, -1, -1)])
    for idx in range(len(people)):
        dialogs.append(f"{people[idx]}: khodafez bacheha!")
        dialogs.extend([f"{people[i]}: khodafez {people[idx]}" for i in range(idx + 1, len(people))])
    return '\n'.join(dialogs)

def main():
    count = int(input())
    people = [input() for i in range(count)]
    print(operation(people))

main()
# tests
# test 1 is wrong

assert operation(['negar', 'zahra', 'yasaman']) == """zahra: salam negar!
yasaman: salam zahra!
yasaman: salam negar!
negar: khodafez bacheha!
zahra: khodafez negar
yasaman: khodafez negar
zahra: khodafez bacheha!
yasaman: khodafez zahra
yasaman: khodafez bacheha!""", "test 2 failed"