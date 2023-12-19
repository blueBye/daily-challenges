t = int(input())
answers = []

for i1 in range(t):
    s = list(map(lambda x: int(x), input().split()))
    n = s[0]
    k = s[1]

    obj = list(map(lambda x: int(x), input().split()))

    for i2 in range(n - k + 1):
        subtract = obj[i2]
        for i3 in range(k):
            obj[i2 + i3] -= subtract
    
    if any(obj):
        answers.append('Fake')
    else:
        answers.append('Cake')

[print(a) for a in answers]