from typing import List 

class Solution: 
    def generateParenthesis(self, n: int) -> List[str]:
        # first create a matrix of 2 rows and n+1 columns
        mat = [[list() for _ in range(n+1)] for _ in range(2)]

        # the column number plays the role of the numberOfClosedBracketsIUse in generatePrefixesOfAWellFormedParentheses
        # the row number plays the role of the numberOfOpenBracketsIUse in generatePrefixesOfAWellFormedParentheses

        # fill in the first column

        for numberOfOpenBracketsIUse in range(1, n+1):
            mat[numberOfOpenBracketsIUse%2][0] = ['(' * numberOfOpenBracketsIUse]
            for numberOfClosedBracketsIUse in range(1, numberOfOpenBracketsIUse+1):
                if numberOfClosedBracketsIUse == numberOfOpenBracketsIUse:
                    mat[numberOfOpenBracketsIUse%2][numberOfClosedBracketsIUse] = [i + ')' for i in mat[numberOfOpenBracketsIUse%2][numberOfClosedBracketsIUse-1]]
                elif numberOfOpenBracketsIUse > numberOfClosedBracketsIUse:
                    res  = [i + ')' for i in mat[numberOfOpenBracketsIUse%2][numberOfClosedBracketsIUse-1]]
                    res2 = [i + '(' for i in mat[(numberOfOpenBracketsIUse-1)%2][numberOfClosedBracketsIUse]]
                    mat[numberOfOpenBracketsIUse%2][numberOfClosedBracketsIUse] = res + res2 
                # there is no else condition. 

        return mat[n%2][n]

print(Solution().generateParenthesis(3))