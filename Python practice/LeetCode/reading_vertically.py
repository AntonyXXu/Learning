def readingVertically(arr):
    ans = ""
    longest = 0
    for i in range(len(arr)):
        longest = max(len(arr[i]), longest)
    for col in range(longest):
        for i in range(len(arr)):
            if col < len(arr[i]):
                ans += arr[i][col]
                    
    return ans
