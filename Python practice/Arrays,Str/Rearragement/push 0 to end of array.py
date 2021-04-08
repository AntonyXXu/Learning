#Move all zeroes to end of array
x = [1, 2, 0, 4, 3, 0, 5, 0]
def move(x):
    count = 0
    for i in range(len(x)):
        if x[i]:
            x[count] = x[i]
            count += 1
    for i in range(count, len(x)):
        x[i] = 0
    print(x)

move(x)
    