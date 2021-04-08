x = [4, 5, 1, 2]

for i in range(len(x)//2):
    x[i], x[-i-1] = x[-i-1], x[i]

print(x)