# https://leetcode.com/problems/delete-columns-to-make-sorted/

s1 =  ["cba","daf","ghi"]
s2 = ["a","b"]
s3 =  ["zyx","wvu","tsr"]

def minDel(arr):
    res = 0
    
    for col in range(len(arr[0])):
        for row in range(1,len(arr)):
            if ord(arr[row][col]) < ord(arr[row-1][col]):
                res += 1
                break
    return res

print(minDel(s1))
print(minDel(s2))
print(minDel(s3))
        

