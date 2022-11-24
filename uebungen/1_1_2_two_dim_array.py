from typing import List


# ======================================================================================================================
# # 0498    对角线遍历    数组、矩阵、模拟    中等
# # 给定一个大小为 m * n 的矩阵 mat 。以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。
# # 输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
# # 输出：[1,2,4,7,5,3,6,8,9]
# class Solution:
#     def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
#         rows = len(mat)
#         cols = len(mat[0])
#         count = rows * cols
#         x, y = 0, 0
#         ans = []
#         for i in range(count):
#             ans.append(mat[x][y])
#
#             if (x + y) % 2 == 0:
#                 # 最后一列
#                 if y == cols - 1:
#                     x += 1
#                 # 第一行
#                 elif x == 0:
#                     y += 1
#                 # 右上方向
#                 else:
#                     x -= 1
#                     y += 1
#             else:
#                 # 最后一行
#                 if x == rows - 1:
#                     y += 1
#                 # 第一列
#                 elif y == 0:
#                     x += 1
#                 # 左下方向
#                 else:
#                     x += 1
#                     y -= 1
#         return ans
# mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# sol = Solution()
# print(sol.findDiagonalOrder(mat))
# ======================================================================================================================
# # 0048    旋转图像
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         n = len(matrix)
#         for i in range(n // 2):
#             for j in range((n + 1) // 2):
#                 matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] = \
#                 matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
#         return matrix
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# sol = Solution()
# # 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# # 输出：[[7,4,1],[8,5,2],[9,6,3]]
# print(sol.rotate(matrix))
# ======================================================================================================================
# # 01187    杨辉三角
# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         dp = [[1] * i for i in range(1, numRows + 1)]
#         res = []
#         for i in range(numRows):
#             for j in range(i):
#                 if i != 0 and j != 0:  # 边界条件
#                     dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
#             res.append(dp[i])
#         return res
# numRows = 5
# sol = Solution()
# print(sol.generate(numRows))
# ======================================================================================================================
# # 0119    杨辉三角II
# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         # 本题从 0 行开始计算
#         numRows = rowIndex + 1  # 杨辉三角的第i行有i+1个元素
#         dp = [1 for _ in range(numRows)]  # 新建dp有i+1个元素
#         for i in range(numRows):
#             for j in range(i - 1, -1, -1):
#                 if i != 0 and j != 0:
#                     dp[j] = dp[j - 1] + dp[j]
#         return dp
# rowIndex = 3
# sol = Solution()
# print(sol.getRow(rowIndex))
# ======================================================================================================================
# # 0073    矩阵置零
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         m = len(matrix)    # 行
#         n = len(matrix[0]) # 列
#         # 先判断第一行第一列是否有0，因为正常来说如果有0则第一行或者第一列应该为全0，无法用作记录index，所以先使用第一行第一列记录，最后再全置0
#         flag_col0 = False
#         flag_row0 = False
#         for i in range(m):
#             if matrix[i][0] == 0:
#                 flag_col0 = True
#                 break
#         for j in range(n):
#             if matrix[0][j] == 0:
#                 flag_row0 = True
#                 break
#         # 记录0位置index
#         for i in range(1, m):
#             for j in range(1, n):
#                 if matrix[i][j] == 0:
#                     matrix[i][0] = matrix[0][j] = 0
#         for i in range(1, m):
#             for j in range(1, n):
#                 if matrix[i][0] == 0 or matrix[0][j] == 0:
#                     matrix[i][j] = 0
#         # 根据flag全置0
#         if flag_col0:
#             for i in range(m):
#                 matrix[i][0] = 0
#         if flag_row0:
#             for j in range(n):
#                 matrix[0][j] = 0
# sol = Solution()
# ======================================================================================================================
# # 0054	螺旋矩阵
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         up, down, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
#         ans = []
#         while True:
#             for i in range(left, right + 1):
#                 ans.append(matrix[up][i])
#             up += 1
#             if up > down:
#                 break
#             for i in range(up, down + 1):
#                 ans.append(matrix[i][right])
#             right -= 1
#             if right < left:
#                 break
#             for i in range(right, left - 1, -1):
#                 ans.append(matrix[down][i])
#             down -= 1
#             if down < up:
#                 break
#             for i in range(down, up - 1, -1):
#                 ans.append(matrix[i][left])
#             left += 1
#             if left > right:
#                 break
#         return ans
# # 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# # 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# sol = Solution()
# print(sol.spiralOrder(matrix))
# ======================================================================================================================
# # 0059	螺旋矩阵II
# class Solution:
#     def generateMatrix(self, n: int) -> List[List[int]]:
#         matrix = [[0 for _ in range(n)] for _ in range(n)]
#         up, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
#         index = 1
#         while True:
#             for i in range(left, right + 1):
#                 matrix[up][i] = index
#                 index += 1
#             up += 1
#             if up > down:
#                 break
#             for i in range(up, down + 1):
#                 matrix[i][right] = index
#                 index += 1
#             right -= 1
#             if right < left:
#                 break
#             for i in range(right, left - 1, -1):
#                 matrix[down][i] = index
#                 index += 1
#             down -= 1
#             if down < up:
#                 break
#             for i in range(down, up - 1, -1):
#                 matrix[i][left] = index
#                 index += 1
#             left += 1
#             if left > right:
#                 break
#         return matrix
# ======================================================================================================================
# 0289	生命游戏
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = {(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)}
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                lives = 0
                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    if 0 <= new_row < rows and 0 <= new_col < cols and abs(board[new_row][new_col]) == 1:
                        lives += 1
                if board[row][col] == 1 and (lives < 2 or lives > 3):
                    board[row][col] = -1
                if board[row][col] == 0 and lives == 3:
                    board[row][col] = 2
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1