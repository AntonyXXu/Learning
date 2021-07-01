def reverseBits(n: str):
    ans = 0
    for i in range(len(n)):
        ans += 2**i * int(n[i])
    return ans

print(reverseBits("00000010100101000001111010011100"))
print(reverseBits("11111111111111111111111111111101"))