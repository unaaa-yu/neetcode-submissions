class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        seen = []
        ops = {"+", "-", "*", "/"}
        for token in tokens:
            if token in ops:
                num1 = seen.pop()        # 右操作数（后进先出）
                num2 = seen.pop()        # 左操作数
                if token == "+":
                    ans = num2 + num1
                elif token == "-":
                    ans = num2 - num1    # 顺序：左 - 右
                elif token == "*":
                    ans = num2 * num1
                else:  # "/"
                    ans = int(num2 / num1)   # 向 0 截断，而非 //
                seen.append(ans)
            else:
                seen.append(int(token))      # 入栈时就转 int，含负数也 OK
        return seen[-1]    