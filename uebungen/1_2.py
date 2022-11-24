from typing import List
# ======================================================================================================================
# # 冒泡排序
# class Solution:
#     def bubbleSort(self, arr):
#         # 第 i 趟排序
#         for i in range(len(arr)):
#             # 从序列中前 n - i + 1 个元素的第 1 个元素开始，相邻两个元素进行比较
#             for j in range(len(arr) - i - 1):
#                 # 相邻两个元素进行比较，如果前者大于后者，则交换位置
#                 if arr[j] > arr[j + 1]:
#                     arr[j], arr[j + 1] = arr[j + 1], arr[j]
#         return arr
#     def sortArray(self, nums: List[int]) -> List[int]:
#         return self.bubbleSort(nums)
# ======================================================================================================================
# # 选择排序
# class Solution:
#     def selectionSort(self, arr):
#         for i in range(len(arr) - 1):
#             # 记录未排序部分中最小值的位置
#             min_i = i
#             for j in range(i + 1, len(arr)):
#                 if arr[j] < arr[min_i]:
#                     min_i = j
#             # 如果找到最小值的位置，将 i 位置上元素与最小值位置上的元素进行交换
#             if i != min_i:
#                 arr[i], arr[min_i] = arr[min_i], arr[i]
#         return arr
#     def sortArray(self, nums: List[int]) -> List[int]:
#         return self.selectionSort(nums)
# sol = Solution()
# print(sol.sortArray([6, 2, 3, 5, 1, 4]))
# ======================================================================================================================
# # 插入排序 Insertion Sort
# class Solution:
#     def insertionSort(self, arr):
#         # 遍历无序序列
#         for i in range(1, len(arr)):
#             temp = arr[i]  # 先把未排序部分的第一个值赋值给temp
#             j = i
#             # 从右至左遍历有序序列
#             while j > 0 and arr[j - 1] > temp:
#                 # 将有序序列中插入位置右侧的元素依次右移一位
#                 arr[j] = arr[j - 1]
#                 j -= 1
#             # 将该元素插入到适当位置
#             arr[j] = temp
#         return arr
#     def sortArray(self, nums: List[int]) -> List[int]:
#         return self.insertionSort(nums)
# ======================================================================================================================
# # 希尔排序（Shell Sort）
# class Solution():
#     def shellSort(self, arr):
#         size = len(arr)  # 整个数组有size个数字
#         gap = size // 2  # size个数字被分为gap个组
#         # 按照gap进行分组
#         while gap > 0:
#             # temp为每组中无序序列第1个元素
#             for i in range(gap, size):  # 关于这里为什么是
#                 # ================= 插入排序 ============================
#                 temp = arr[i] # 这里开始就是插入排序了
#                 j = i
#                 # 从右到左遍历每组中的有序序列元素
#                 while j >= gap and arr[j - gap] > temp:
#                     # 将每组有序序列中插入位置右侧的元素一次在组中右移一位
#                     arr[j] = arr[j - gap]
#                     j -= gap  # 在第一个gap循环，因为每个gap只有2个值，所以这一步之后j一定是<gap的，会退出循环；后面则不会
#                 # 将该元素插入到适当位置
#                 arr[j] = temp
#                 # ================= 插入排序 ============================
#             # 缩小gap间隔
#             gap = gap // 2
#         return arr
#     def sortArray(self, nums: List[int])->List[int]:
#         return self.shellSort(nums)
# nums = [10,9,8,7,6,5,4,3,2,1,0]
# sol = Solution()
# print(sol.sortArray(nums))
# ======================================================================================================================
# # 归并排序    Merge Sort
# class Solution():
#     def merge(self, left_arr, right_arr):  # 归并过程
#         arr = []
#         left_i, right_i = 0, 0
#         while left_i < len(left_arr) and right_i < len(right_arr):  # 将left_arr和right_arr中的小的值先插入到arr中，因为是递归，所以能保证给的left_arr和right_arr已经是小到大的顺序了
#             # 将两个有序子序列中较小的元素一次插入到结果数组中
#             if left_arr[left_i] < right_arr[right_i]:
#                 arr.append(left_arr[left_i])
#                 left_i += 1
#             else:
#                 arr.append(right_arr[right_i])
#                 right_i += 1
#         while left_i < len(left_arr):
#             # 如果左子集有剩余元素，则将其插入到结果数组中
#             arr.append(left_arr[left_i])
#             left_i += 1
#         while right_i < len(right_arr):
#             # 如果右子序列有剩余元素，则将其插入到结果数组中
#             arr.append(right_arr[right_i])
#             right_i += 1
#         return arr
#     def mergeSort(self, arr):
#         if len(arr) <= 1:
#             return arr
#         mid = len(arr) // 2
#         left_arr = self.mergeSort(arr[0:mid])
#         right_arr = self.mergeSort(arr[mid:])
#         return self.merge(left_arr, right_arr)
#     def sortArray(self, nums:List[int])->List[int]:
#         return self.mergeSort(nums)
# ======================================================================================================================
# # 快速排序（Quick Sort）
# import random
# class Solution:
#     # 从 arr[low: high + 1] 中随机挑选一个基准数，并进行移动排序
#     def randomPartition(self, arr: [int], low: int, high: int):
#         # 随机挑选一个基准数
#         i = random.randint(low, high)
#         # i = 3
#         # 将基准数与最低位互换
#         arr[i], arr[low] = arr[low], arr[i]
#         # 以最低位为基准数，然后将序列中比基准数大的元素移动到基准数右侧，比他小的元素移动到基准数左侧。最后将基准数放到正确位置上
#         return self.partition(arr, low, high)
#     # 以最低位为基准数，然后将序列中比基准数大的元素移动到基准数右侧，比他小的元素移动到基准数左侧。最后将基准数放到正确位置上
#     def partition(self, arr: [int], low: int, high: int):  # partition：分区，隔断
#         pivot = arr[low]  # 以第 1 为为基准数
#         i = low + 1  # 从基准数后 1 位开始遍历，保证位置 i 之前的元素都小于基准数
#         for j in range(i, high + 1):
#             # 发现一个小于基准数的元素
#             if arr[j] < pivot:
#                 # 将小于基准数的元素 arr[j] 与当前 arr[i] 进行换位，保证位置 i 之前的元素都小于基准数
#                 arr[i], arr[j] = arr[j], arr[i]
#                 # i 之前的元素都小于基准数，所以 i 向右移动一位
#                 i += 1
#         # 将基准节点放到正确位置上
#         arr[i - 1], arr[low] = arr[low], arr[i - 1]
#         # 返回基准数位置
#         return i - 1
#     def quickSort(self, arr, low, high):
#         if low < high:
#             # 按照基准数的位置，将序列划分为左右两个子序列
#             pi = self.randomPartition(arr, low, high)
#             # 对左右两个子序列分别进行递归快速排序
#             self.quickSort(arr, low, pi - 1)
#             self.quickSort(arr, pi + 1, high)
#         return arr
#     def sortArray(self, nums: List[int]) -> List[int]:
#         return self.quickSort(nums, 0, len(nums) - 1)
# nums = [7, 6, 5, 4, 3, 2, 1, 0]
# sol = Solution()
# print(sol.sortArray(nums))
# ======================================================================================================================
# 堆排序（Heap sort）https://algo.itcharge.cn/01.Array/02.Array-Sort/07.Array-Heap-Sort/
class Solution:
    # 调整为大顶堆
    def heapify(self, arr: [int], index: int, end: int):
        # 根节点为 index，左节点为 2 * index + 1， 右节点为 2 * index + 2
        left = index * 2 + 1
        right = left + 1
        while left <= end:
            # 当前节点为非叶子结点
            max_index = index
            if arr[left] > arr[max_index]:
                max_index = left
            if right <= end and arr[right] > arr[max_index]:
                max_index = right
            if index == max_index:
                # 如果不用交换，则说明已经交换结束
                break
            arr[index], arr[max_index] = arr[max_index], arr[index]
            # 继续调整子树
            index = max_index
            left = index * 2 + 1
            right = left + 1
    # 初始化大顶堆
    def buildMaxHeap(self, arr: [int]):
        size = len(arr)
        # (size - 2) // 2 是最后一个非叶节点，叶节点不用调整
        last_non_leaf_node = (size - 2) // 2
        for i in range(last_non_leaf_node, -1, -1):
            self.heapify(arr, i, size - 1)
        return arr  # 建立大顶堆，此时arr中最大的值到了第0位置
    # 升序堆排序，思路如下：
    # 1. 先建立大顶堆
    # 2. 让堆顶最大元素与最后一个交换，然后调整第一个元素到倒数第二个元素，这一步获取最大值
    # 3. 再交换堆顶元素与倒数第二个元素，然后调整第一个元素到倒数第三个元素，这一步获取第二大值
    # 4. 以此类推，直到最后一个元素交换之后完毕。
    def maxHeapSort(self, arr: [int]):
        self.buildMaxHeap(arr)
        size = len(arr)
        for i in range(size):
            arr[0], arr[size - i - 1] = arr[size - i - 1], arr[0]
            self.heapify(arr, 0, size - i - 2)
        return arr
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.maxHeapSort(nums)
nums = [5, 6, 7, 2, 3, 4, 1, 0]
sol = Solution()
print(sol.sortArray(nums))