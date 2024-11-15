class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        # if (asteroids.empty()) return []
        for i in asteroids:
            if (i < 0):
                dif = -1
                while stack and stack[-1] > 0:
                    dif = stack[-1] + i
                    if dif > 0: break
                    elif dif < 0:
                        stack.pop()
                    else:
                        stack.pop()
                        break
                if dif < 0:
                    stack.append(i)
            else:
                stack.append(i)
        return stack