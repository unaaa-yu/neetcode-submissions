class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n          # 默认 0：没有更暖的一天
        stack = []                # 存下标，温度单调递减

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prev = stack.pop()
                result[prev] = i - prev   # 等了 i - prev 天
            stack.append(i)

        return result

        