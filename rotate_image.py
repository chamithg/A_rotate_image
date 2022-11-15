class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                print(matrix[i][j],matrix[len(matrix)-1-j][i])
                
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        return matrix
        
         
        
matrix = [[1,2,3],[4,5,6],[7,8,9]]
mat1 = [[7,4,1],[8,5,2],[9,6,3]]
#Output: [[7,4,1],[8,5,2],[9,6,3]]

matrix1 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

obj = Solution()
print(obj.rotate(matrix))