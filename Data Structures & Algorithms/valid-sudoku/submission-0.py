class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_x = defaultdict(set)
        check_y = defaultdict(set)
        check_3s = defaultdict(set)

        
        for i in range(len(board)):
            for j in range(len(board[i])):
                val = board[i][j]

                if val == ".":
                    continue
                
                box_idx = (i // 3) * 3 + (j // 3)

                if (val in check_x[i] or 
                val in check_y[j] or 
                val in check_3s[box_idx]):
                    return False
                check_x[i].add(val)
                check_y[j].add(val)
                check_3s[box_idx].add(val)
        return True               
        # col_i = [["."] for i in range(len(board))] #紀錄col
        # square = 3
        # com_3s = [["."] for i in range(square)] #紀錄3* 3 (0,0) (0,1)

        # for row in range(len(board)):
        #     dupli_x = {}

        #     for i, vali in enumerate(board[row]):
        #         col_i[i].append(vali) #col list
                
        #         s = i // 3 
        #         com_3s[s].append(vali)

        #         if vali not in dupli_x:
        #             dupli_x[vali] = 1
        #         else:
        #             dupli_x[vali] += 1
            
        #     for key, val in dupli_x.items():
        #         if val > 1 and key != ".":
        #             return False

        # for col in range(len(col_i)):
        #     dupli_y = {}

        #     for j, valj in enumerate(col_i[col]):
        #         # s = j // 3
        #         # col_3sy[s].append(vali)

        #         if valj not in dupli_y:
        #             dupli_y[valj] = 1
        #         else:
        #             dupli_y[valj] += 1
            
        #     for key, val in dupli_y.items():
        #         if val > 1 and key != ".":
        #             return False

        # for group in range(len(com_3s)):
        #     dupli_group = {}
        #     count = 0

        #     for j, valj in enumerate(com_3s[group]):
        #         # s = j // 3
        #         # col_3sy[s].append(vali)
        #         count += 1
        #         if count < square**2 - 1:
        #             if valj not in dupli_group:
        #                 dupli_group[valj] = 1
        #             else:
        #                 dupli_group[valj] += 1
            
        #         for key, val in dupli_group.items():
        #             if val > 1 and key != ".":
        #                 return False
                
        #         else:
        #             count = 0

        # return True
