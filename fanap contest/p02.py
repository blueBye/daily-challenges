s = input().split()
p = int(s[0])
q = int(s[1])

for i in range(p):
    print(' _' * q)
    print('| ' * q, end='')
    print('|')
print(' _' * q)
