n = int(input())

fibnacch = [0] * (n + 1)

for i in range(n + 1):
    if i == 0 or i == 1:
        fibnacch[i] = 1
    else:
        fibnacch[i] = fibnacch[i - 1] + fibnacch[i - 2]

print(fibnacch[n])
