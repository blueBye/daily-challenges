
n, q, l = [int(i) for i in input().split((' '))]

dataset = {}
for _ in range (n):
    k, v = input().split(' ')
    dataset[k] = v

answeres = []
for _ in range(q):
    answeres.append(dataset.get(input(), 'Unknown'))

[print(i) for i in answeres]
