class Solution(object):
    def generateParenthesis(self, n):
        return self.generatePrefixesOfAWellFormedParentheses(n, n)

    def generatePrefixesOfAWellFormedParentheses(self, openCount, closedCount):
        if (closedCount == 0):
            return ['(' * openCount]
        if openCount == closedCount:
            res = [
                i + ")"  for i in self.generatePrefixesOfAWellFormedParentheses(openCount, closedCount-1)]
            return res
        else:
            res = [
                i + "(" for i in self.generatePrefixesOfAWellFormedParentheses(openCount-1, closedCount)]
            res2 = [
                i + ")" for i in self.generatePrefixesOfAWellFormedParentheses(openCount, closedCount-1)]
            return res + res2