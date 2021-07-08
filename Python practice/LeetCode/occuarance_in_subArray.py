import collections
def occurrencesInSubarrays(arr, m):
    ans = []
    window = collections.Counter()
    n = len(arr)
    for i in range(len(arr)-m+1):
        if i == 0:
            for i in range(m):
                window[arr[i]] += 1
        else:
            window[arr[i-1]] -= 1

            window[arr[i+m-1]] += 1
        vals = [j for j in window.values()]
        ans.append(max(vals))
    return ans
        
            