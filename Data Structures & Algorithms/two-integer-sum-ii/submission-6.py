class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 # pointer 1
        j = len(numbers) - 1 # pointer 2

        while i < len(numbers): 
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i+1, j+1]


        # while i < len(numbers)//2: 
        #     while j < len(numbers):
        #         if numbers[i] + numbers[j] != target:
        #             j += 1
        #         else:
        #             return [i+1, j+1]
        
                