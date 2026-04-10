class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        ROWS = len(matrix)       # 有幾列
        COLS = len(matrix[0])    # 有幾欄
        
        # 把矩陣看成一條長度為 ROWS * COLS 的直線，設定左右邊界
        l, r = 0, (ROWS * COLS) - 1
        
        while l <= r:
            mid = (l + r) // 2
            # 將直線的索引轉回 [列][欄] 座標
            # 例如 COLS=4, index=5 => 5//4=1, 5%4=1 => matrix[1][1]
            mid_val = matrix[mid // COLS][mid % COLS]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                l = mid + 1      # 太小了，往右找
            else:
                r = mid - 1      # 太大了，往左找
                
        return False

        # brutal solution
        # for row in matrix:
        #     if target in row:
        #         return True
        
        # return False