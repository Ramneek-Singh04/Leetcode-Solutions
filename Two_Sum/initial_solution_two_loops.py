class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list1=[]
        for i in nums:
            x = target - i
            newnums = nums.copy()
            newnums.remove(i)
            if x in newnums:
                list1.append(nums.index(i))
                if x == i:
                    nums[nums.index(i)] = 'x'
                    list1.append(nums.index(x))
                else:
                    list1.append(nums.index(x))
                return list1