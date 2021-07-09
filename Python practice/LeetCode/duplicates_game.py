def dup(numbers):
    alice = False
    for i in range(len(numbers) - 1):
        if i >= len(numbers)-1:
            break
        if numbers[i] == numbers[i+1]:
            numbers.pop(i)
            numbers.pop(i)
            alice = not alice
            i -= 2
    if alice:
        return "Alice"
    else:
        return "Bob"

print(dup([1,1,2,2,3,3]))