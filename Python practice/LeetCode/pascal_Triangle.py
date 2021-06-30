def pascal(numRows):
    res = []
    for i in range(numRows):
        if i == 0:
            res.append([1])
        else:
            subArr = [0]*(i+1)
            for j in range(len(subArr)):
                
                if j == 0:
                    subArr[j] = res[i-1][j]
                elif j == len(subArr)-1:
                    subArr[j] = 1

                else:
                    subArr[j] = res[i-1][j-1] + res[i-1][j]
            res.append(subArr)
    return res

print(pascal(1))
print(pascal(30))