from heapq import *
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.lazy = {}
        self.t = []
        for uid, tid, prio in tasks:
            self.add(uid, tid, prio)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.lazy[taskId] = (priority, userId)
        heappush(self.t, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.lazy[taskId][1]
        self.lazy[taskId] = (newPriority, userId)
        heappush(self.t, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        self.lazy.pop(taskId)

    def execTop(self) -> int:
        while self.t and (-self.t[0][1] not in self.lazy or (-self.t[0][0], self.t[0][2]) != self.lazy[-self.t[0][1]]): heappop(self.t)
        if not self.t: return -1
        z = heappop(self.t)
        self.lazy.pop(-z[1])
        return z[2]


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()