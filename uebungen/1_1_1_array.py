from typing import List


# ======================================================================================================================
# # 0189    轮转数组    python    数组    中等
# 将数组中的元素向右移动 k 个位置。
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         n = len(nums)
#         self.reverse(nums, 0, n-1)
#         self.reverse(nums, 0, k-1)
#         self.reverse(nums, k, n-1)
#     def reverse(self, nums: List[int], left: int, right: int) -> None:
#         while left < right:
#             tmp = nums[left]
#             nums[left] = nums[right]
#             nums[right] = tmp
#             left += 1
#             right -= 1
# nums = [1,2,3,4,5,6,7]
# k = 3
# sol = Solution()
# sol.rotate(nums, k)
# print(nums)
# ======================================================================================================================
# # 0066    加一    python    数组    简单
# 给定一个非负整数数组，数组每一位对应整数的一位数字。
# # 数组前补0；将个位数字进行+1运算；遍历数组，如果该位数字大于10，则向下一位进1，继续进行下一位判断，否则跳出循环
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         digits = [0] + digits
#         digits[len(digits)-1] += 1
#         for i in range(len(digits)-1, 0, -1):
#             if digits[i] != 10:
#                 break
#             else:
#                 digits[i] = 0
#                 digits[i-1] += 1
#         if digits[0] == 0:
#             return digits[1:]
#         else:
#             return digits
# a = [9,0,9]
# sol = Solution()
# digits = sol.plusOne(a)
# print(digits)
# ======================================================================================================================
# # 0724    寻找数组的中心下标    python    数组    简单
# 找到「左侧元素和」与「右侧元素和相等」的位置，若找不到，则返回 -1。
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         summ = sum(nums)
#         for i in range(1, len(nums)):
#             if sum(nums[:i]) * 2 + nums[i] == summ:
#                 return i
#         return -1
# nums = [1, 7, 3, 6, 5, 6]
# sol = Solution()
# print(sol.pivotIndex(nums))
# ======================================================================================================================
# # 0485    最大连续1的个数
# 给定一个二进制数组，数组中只包含 0 和 1，计算其中最大连续 1 的个数。
# 使用两个变量 sum 和 ans。sum 用于存储当前连续 1 的个数，ans 用于存储最大连续 1 的个数。然后进行一次遍历，统计当前连续 1 的个数，并更新最大的连续 1 个数。
# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         ans = 0  # 用于存储最大连续 1 的个数
#         sum = 0  # 用于存储当前连续 1 的个数
#         for num in nums:
#             if num == 1:
#                 sum += 1
#                 ans = max(ans, sum)
#             else:
#                 sum = 0
#         return ans
# nums = [1,1,0,1,1,1]
# sol = Solution()
# print(sol.findMaxConsecutiveOnes(nums))
# # 输出：3    解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
# ======================================================================================================================
# # 0238    除自身以外数组的乘积    数组    中等
# # 给定一个数组 nums。要求输出数组 output，其中 output[i] 为数组 nums 中除了 nums[i] 之外的其他所有元素乘积。要求不能使用除法，且在 O(n) 时间复杂度、常数空间复杂度内解决问题。
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         size = len(nums)
#         res = [1 for _ in range(size)]
#         left = 1
#         for i in range(size):
#             res[i] *= left
#             left *= nums[i]
#         right = 1
#         for i in range(size-1, -1, -1):
#             res[i] *= right
#             right *= nums[i]
#         return res
# nums = [1, 2, 3, 4]
# # nums = [-1, 1, 0, -3, 3]
# sol = Solution()
# print(sol.productExceptSelf(nums))
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [1 for _ in range(size)]
        left = 1
        for i in range(size):
            res[i] *= left
            left *= nums[i]
        right = 1
        for i in range(size-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res