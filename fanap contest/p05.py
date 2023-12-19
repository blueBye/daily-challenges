t = int(input())
answers = []

for i1 in range(t):
    ss1 = list(map(lambda x: int(x), input().split()))
    n = ss1[0]
    l = ss1[1]
    s = ss1[2]

    # scan ladders and snakes as jumps
    jumps = {}
    for i2 in range(l + s):
        ss2 = list(map(lambda x: int(x), input().split()))
        jumps[ss2[0]] = ss2[1]

    # fix double jumps
    while True:
        count = 0
        for i2 in jumps:
            if jumps[i2] in jumps:
                count += 1
                jumps[i2] = jumps[jumps[i2]]
        if count == 0:
            break

    positions = [0]
    final_pos = n
    nsteps = 0
    while final_pos not in positions:
        nsteps += 1
        old_positions = positions
        positions = set()
        for pos in old_positions:
            for dice in range(1, 7):
                new_pos = pos + dice
                positions.add(jumps.get(new_pos, new_pos))
    answers.append(nsteps)

[print(a) for a in answers]
