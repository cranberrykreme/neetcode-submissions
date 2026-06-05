class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        stack = []
        for pos, sp in reversed(cars):
            time_to_arrive = (target-pos) / sp
            if not stack or stack[-1] < time_to_arrive:
                stack.append(time_to_arrive)
        return len(stack)