class Solution(object):
    def twoSum(self, nums, target):
        index_list = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i is not j:
                    index_list.append(i)
                    index_list.append(j)
                    return index_list
                else:
                    pass
