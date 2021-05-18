# Given the array queries of positive integers between 1 and m, you have to process all queries[i] 
# (from i=0 to i=queries.length-1) according to the following rules:

# In the beginning, you have the permutation P=[1,2,3,...,m].
# For the current i, find the position of queries[i] in the permutation P (indexing from 0)
# and then move this at the beginning of the permutation P. Notice that the position of queries[i] in P is the result for queries[i].
# Return an array containing the result for the given queries.

queries = [3,1,2,1]
m = 5
queries1 = [4,1,2,2]
m1 = 4
queries2 = [7,5,5,8,3]
m2 = 8

def processQueries(queries, m):
    perm = [i+1 for i in range(m)]
    res = []
    for i in range(len(queries)):
        num = queries[i]
        p_index = perm.index(num)
        res.append(p_index)
        while p_index > 0:
            perm[p_index], perm[p_index - 1] = perm[p_index - 1], perm[p_index]
            p_index -= 1
        perm[0] = num
    return res

print(processQueries(queries, m))
print(processQueries(queries1, m1))
print(processQueries(queries2, m2))