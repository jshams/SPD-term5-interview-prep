'''
You are given a square 2D image matrix (List of Lists) where each integer represents a pixel. 
Write a method transpose_matrix to transform the matrix into its Transpose - in-place. 
The transpose of a matrix is a matrix which is formed by turning all the rows of the source matrix into columns and vice-versa. 

Example:
Input image : 
1 0
1 0
 
Modified to: 
1 1
0 0
'''

def transpose_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        new_lst = []
        for lst in matrix:
            new_lst.append(lst[i])
        new_matrix.append(new_lst)
    return new_matrix

trial = [[1, 0, 1], [1, 0, 1], [1, 0, 1]]
print(transpose_matrix(trial))