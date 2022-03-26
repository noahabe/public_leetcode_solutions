from typing import List 

class Solution: 
    def generateParenthesis(self, n: int) -> List[str]:
        # first create a matrix of n+1 rows and n+1 columns
        mat = [[list() for _ in range(n+1)] for _ in range(n+1)]

        # the column number plays the role of the numberOfClosedBracketsIUse in generatePrefixesOfAWellFormedParentheses
        # the row number plays the role of the numberOfOpenBracketsIUse in generatePrefixesOfAWellFormedParentheses

        # fill in the first column
        for i in range(1, n+1):
            mat[i][0].append('(' * i)

        for numberOfOpenBracketsIUse in range(1, n+1):
            for numberOfClosedBracketsIUse in range(1, numberOfOpenBracketsIUse+1):
                if numberOfClosedBracketsIUse == numberOfOpenBracketsIUse:
                    mat[numberOfOpenBracketsIUse][numberOfClosedBracketsIUse] = [i + ')' for i in mat[numberOfOpenBracketsIUse][numberOfClosedBracketsIUse-1]]
                elif numberOfOpenBracketsIUse > numberOfClosedBracketsIUse:
                    res  = [i + ')' for i in mat[numberOfOpenBracketsIUse][numberOfClosedBracketsIUse-1]]
                    res2 = [i + '(' for i in mat[numberOfOpenBracketsIUse-1][numberOfClosedBracketsIUse]]
                    mat[numberOfOpenBracketsIUse][numberOfClosedBracketsIUse] = res + res2 
                # there is no else condition. 

        return mat[n][n]