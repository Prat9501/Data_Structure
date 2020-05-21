# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row_num in range(numRows):
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]
            triangle.append(row)

        return triangle

        # res = []
        # for i in range(1, numRows + 1):
        #     res.append(1)
        #     for j in range(numRows - 2, 0, -1):
        #         res[i] +=  res[i+1]
        # return res
