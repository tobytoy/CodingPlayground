from typing import List


class Solution_1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i,j]


if __name__ == '__main__':
    input_nums = [2,7,11,15]
    input_target = 9

    solution = Solution_1()
    output = solution.twoSum(input_nums, input_target)
    print("Output: ", output)
