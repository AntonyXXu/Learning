# https://leetcode.com/problems/queue-reconstruction-by-height/

def reconstructQueue(people):
    sort_people = sorted(people, key = lambda x: [-x[0], x[1]])
    ans = [sort_people[0]]
    for i in range(1, len(sort_people)):
        ans.insert(sort_people[i][1], sort_people[i])
    return ans

def reconstructQueue(people):
    p = sorted(people, key=lambda x: [x[0], x[1]])
    ans = [None] * len(people)
    for person in p:
        bigger = 0
        position = 0
        while position < len(p) and bigger <= person[1]:
            if ans[position] == None or ans[position][0] >= person[0]:
                bigger += 1
            position += 1
        ans[position-1] = person

    return ans

print(reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
print(reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))
