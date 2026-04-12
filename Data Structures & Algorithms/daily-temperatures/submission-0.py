class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # 初始化結果陣列，預設全為 0
        res = [0] * len(temperatures)
        stack = [] # 用來存「索引」：[index1, index2, ...]

        for i, t in enumerate(temperatures):
            # 當今天溫度 t 比 stack 頂端的溫度還要暖時
            while stack and t > temperatures[stack[-1]]:
                # 彈出索引，因為那一天終於等到變暖了
                prev_index = stack.pop()
                # 計算天數差
                res[prev_index] = i - prev_index
            
            # 把今天的索引放進去，等待未來更暖的日子
            stack.append(i)
            
        return res