# Scheduling
# List of tasks to schedule on single cor
# task has id: string
# time of queue: int
# time to execution: int
# {"string", "int", "int"}

# if cpu idle, it picks the task with shortest execution time

# given 1cpu and list of tasks, return sequence


# at least one task
# no timeout
# can have duplicate tasks
# if duplicate, order won't matter

# function:
#     sort tasks by startTime

#     1, 2, 3, 4
#     ans array (id)
#     current time = 0
#     while len(taskList) and while heap:
#         if heap is empty:
#             current time to taskList[0]
#             current = taskist.pop(0)
#             heap.push(current)

#         heap.pop()
#         current time += duration

#         ans.append(id)

#         while startTime < currentTime:
#             taskList.pop(0)
#             heap . push (current task)

# O(nlogn)

import heapq
Input = [("id1", 3, 10), ("id2", 5, 10), ("id3", 9, 5), ("id4", 15, 1)]
Output = ["id1", "id2", "id4", "id3"]


class Task:
    def __init__(self, task):
        self.task = task

    def __cmp__(self, other):
        if self.task[2] == other.task[2]:
            return 0
        if self.task[2] < other.task[2]:
            return -1
        return 1


def tasks(taskList):
    taskList.sort(key=lambda x: x[1])
    cpus = [0, 0]
    currentTime = 0
    index = 0
    heap = []
    ans = []
    while index < len(taskList):
        currentTime = max(currentTime, taskList[index][1])

        while index < len(taskList) and currentTime >= taskList[index][1]:
            heapq.heappush(heap, taskList[index])
            index += 1

        task = heapq.heappop(heap)
        currentTime += task[2]
        ans.append(task[0])
    while heap:
        task = heapq.heappop(heap)
        currentTime += task[2]
        ans.append(task[0])
    return ans

# K (cpu)
# N (tasks)
# N times
#     logN

#     logK

#     O(K)

#     O(K)
# N
#     O(K)

# O(NlogN + Nlog(K))


def tasks(n, taskList):
    taskList.sort(key=lambda x: x[1])
    cpuHeap = [("", 0)] * n
    currentTime = 0
    index = 0
    heap = []
    ans = []
    DECREMENT_TIME = 0
    while index < len(taskList):
        while index < len(taskList) and currentTime >= taskList[index][1]:
            heapq.heappush(heap, taskList[index])
            index += 1

        while cpuHeap[0][1] <= currentTime and heap:
            task = heapq.heappop(heap)
            cpuHeap[0][1] += task[2]
            cpuHeap[0][0] = task[0]
            heapq.heapify(cpuHeap)

        if heap:
            currentTime = currentTime + max(0, cpuHeap[0][1])
            time = max(0, cpuHeap[0][1])
            DECREMENT_TIME + time
            cpuHeap[i] - DECREMENT_TIME
            for i in range(len(cpuHeap)):
                cpuHeap[i][1] -= time
            task = cpuHeap[0]
            if task[0] != "":
                ans.append(task[0])
        else:
            currentTime = max(currentTime, taskList[index][1])
            for i in range(len(cpuHeap)):
                cpuHeap[i][1] -= time

    while heap:
        currentTime = currentTime + cpuHeap[0][1]
        time = cpuHeap[0][1]
        for i in range(len(cpuHeap)):
            cpuHeap[i][1] -= time
        task = cpuHeap[0]
        ans.append(task[0])
    return ans
