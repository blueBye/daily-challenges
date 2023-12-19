t = int(input())
answers = []

for i in range(t):
    n = int(input())
    s = input().split()

    s = list(map(lambda x: int(x[1:]), s))
    counter = 0
    for j in range(n):
        if s[2*j] != s[2*j+1]:
            counter += 1

    if counter <= 2:
        answers.append("YES")
    else:
        answers.append("NO")

[print(a) for a in answers]