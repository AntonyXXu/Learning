# https://leetcode.com/problems/queue-reconstruction-by-height/

def reconstructQueue(people):
    sort_people = sorted(people, key = lambda x: [-x[0], x[1]])
    ans = [sort_people[0]]
    for i in range(1, len(sort_people)):
        ans.insert(sort_people[i][1], sort_people[i])
    return ans

print(reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
print(reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))
