# https://leetcode.com/problems/repeated-dna-sequences/

import collections


def dna(s: str) -> list[str]:
    res = set()
    seen = set()
    for i in range(len(s) - 9):
        curr = s[i:i+10]
        if curr in seen:
            res.add(curr)
        seen.add(curr)
    return list(res)


print(dna("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(dna("AAAAAAAAAAAAA"))
print(dna(""))
print(dna("adafs"))
