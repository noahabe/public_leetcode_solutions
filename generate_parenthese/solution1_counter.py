from typing import List 

class Solution(object):
    def __init__(self):
        self.a = dict()

    def generateParenthesis(self, n):
        return self.generatePrefixesOfAWellFormedParentheses(n, n)

    def generatePrefixesOfAWellFormedParentheses(self, numberOfOpenBracketsIUse: int, numberOfClosedBracketsIUse: int) -> List[str]:
        assert(numberOfOpenBracketsIUse >= numberOfClosedBracketsIUse) # by theorem 4 

        #########[just to calculate, the frequencies of the overlapping subproblems]#######
        x = (numberOfOpenBracketsIUse, numberOfClosedBracketsIUse)
        if self.a.get(x) == None:
            self.a[x] = 1
        else:
            self.a[x] += 1
        ####################################################################################

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

if __name__ == '__main__':
    s = Solution()
    answer = s.generateParenthesis(8)
    frequency_table = s.a
    for subproblem, frequency in frequency_table.items():
        print(f"{subproblem}: {frequency}")