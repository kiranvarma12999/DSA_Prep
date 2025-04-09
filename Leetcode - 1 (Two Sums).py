class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for x in range(l): #traverse the list starting with the first value at pos 0
            for y in range(x + 1, l): #compare all the elements after x to see which combination gives the target value
                if nums[x] + nums[y] == target:
                    return x, y
        return None 