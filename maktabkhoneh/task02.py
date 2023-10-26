
def operation(raw_input):
    return f'saal: {raw_input[:2]}\nmaah: {raw_input[2:4]}\nrooz: {raw_input[4:]}'

def main():
    raw_input = input()
    operation(raw_input)


# tests
assert operation('710612') == "saal: 71\nmaah: 06\nrooz: 12", "test 1 failed"
assert operation('810501') == "saal: 81\nmaah: 05\nrooz: 01", "test 2 failed"
assert operation('000107') == "saal: 00\nmaah: 01\nrooz: 07", "test 3 failed"
