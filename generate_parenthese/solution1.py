from typing import List 

class Solution(object):
    def generateParenthesis(self, n):
        return self.generatePrefixesOfAWellFormedParentheses(n, n)

    def generatePrefixesOfAWellFormedParentheses(self, numberOfOpenBracketsIUse: int, numberOfClosedBracketsIUse: int) -> List[str]:
        assert(numberOfOpenBracketsIUse >= numberOfClosedBracketsIUse) # by theorem 4 

        if (numberOfClosedBracketsIUse == 0):
            return ['(' * numberOfOpenBracketsIUse]

        if numberOfOpenBracketsIUse == numberOfClosedBracketsIUse:
            # then this function returns well-formed parentheses
            # thus by theorem 2 I know that all of the strings in the list will end in a closing bracket. 
            res = [
                i + ")"  for i in self.generatePrefixesOfAWellFormedParentheses(numberOfOpenBracketsIUse, numberOfClosedBracketsIUse-1)]
            return res
            
        elif numberOfOpenBracketsIUse > numberOfClosedBracketsIUse:
            res = [
                i + "(" for i in self.generatePrefixesOfAWellFormedParentheses(numberOfOpenBracketsIUse-1, numberOfClosedBracketsIUse)]
            res2 = [
                i + ")" for i in self.generatePrefixesOfAWellFormedParentheses(numberOfOpenBracketsIUse, numberOfClosedBracketsIUse-1)]
            return res + res2