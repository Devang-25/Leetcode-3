"""Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""

def spiral_copy(inputMatrix):
    """
    1) learn about the length of each row, and how many rows
    cell[i][j]

    4 x 5 matrix
    ++j, row[0][0:4] .  1, 2, 3, 4, 5 , so i know the index == len(row_i), then I go down
    ++i, row[1][4], row[2][4].... row [3][4] so when j == len(matrix) - 1
    --j:row [3][3], cell[3][2], cell[3][1], cell[3][0]
    --i: cell[2][0] cell[1][0]
    ++j: cell[1][1], cell[1][2]
    """
    top_row = 0
    bottom_row = len(inputMatrix) - 1
    left_col = 0
    right_col = len(inputMatrix[0]) - 1
    result = []

    while top_row <= bottom_row and left_col <= right_col:
        for j in range(left_col, right_col+1):
            result.append(inputMatrix[top_row][j])
        top_row += 1

        for i in range(top_row, bottom_row+1):
            result.append(inputMatrix[i][right_col])
        right_col -= 1


        if top_row <= bottom_row:
            for j in reversed(range(left_col, right_col+1)):
                result.append(inputMatrix[bottom_row][j])
            bottom_row -= 1


        if left_col <= right_col:
            for i in reversed(range(top_row, bottom_row+1)):
                result.append(inputMatrix[i][left_col])
            left_col += 1
    return result

spiral_copy([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
spiral_copy([[1,2]])
spiral_copy([[1]])
spiral_copy([[1,2],[3,4]])
