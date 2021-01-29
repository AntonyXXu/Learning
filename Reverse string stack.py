# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:01:16 2021

@author: Test
"""

def reverse(string):
    string = list(string)
    ans = ""
    for index in range(len(string)):
        x = string.pop()
        ans+=x
    ans = str(ans)
    print(x)
    return "".join(ans)

print(reverse("Hello, how are you?"))
