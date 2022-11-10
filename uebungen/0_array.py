from typing import List
# ======================================================================================================================
# # 0189    轮转数组    python    数组    中等
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
# 0724    寻找数组的中心下标    python    数组    简单
