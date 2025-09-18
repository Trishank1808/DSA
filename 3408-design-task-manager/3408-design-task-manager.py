import heapq
from typing import List, Dict, Tuple

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.task_map: Dict[int, Tuple[int, int]] = {}  # taskId -> (userId, priority)
        self.heap: List[Tuple[int, int]] = []  # max-heap: (-priority, -taskId)
        for userId, taskId, priority in tasks:
            self.task_map[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.task_map[taskId]
        self.task_map[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self) -> int:
        while self.heap:
            neg_priority, neg_taskId = heapq.heappop(self.heap)
            taskId = -neg_taskId
            priority = -neg_priority
            if taskId in self.task_map and self.task_map[taskId][1] == priority:
                userId = self.task_map[taskId][0]
                del self.task_map[taskId]
                return userId
        return -1
