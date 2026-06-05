class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        for i in range(len(position)):
            combined.append((position[i], speed[i]))
        combined.sort()
        stack = []
        for (position, speed) in combined:
            time_to_arrive = (target - position) / speed
            stack.append(time_to_arrive)
        fleets = 0
        while stack:
            eta = stack.pop()
            while stack and stack[-1] <= eta:
                stack.pop()
            fleets += 1
        return fleets