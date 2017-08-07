"""This is a implementation for strStr()"""
#Description
#For a given source string and a target string, you should output the first
# index(from 0) of target string in source string.
#
#If target does not exist in source, just return -1.
#Clarification
#Do I need to implement KMP Algorithm in a real interview?
#
#Not necessary. When you meet this problem in a real interview, the interviewer
# may just want to test your basic implementation ability. But make sure your
# confirm with the interviewer first.
#
#Example
#If source = "source" and target = "target", return -1.
#
#If source = "abcdabcdefg" and target = "bcd", return 1."""


class Solution(object):
    """Solution of strstr"""
    def strStr(self, haystack, needle):
        """Find if needle in haystack."""
        # Edge
        if needle is None:
            return -1
        if haystack is None:
            return -1
        m = len(haystack)
        n = len(needle)
        if m < n:
            return -1
        if m == 0 or n == 0:
            return 0

        # Only 1 loop but compare sub-string
        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1


#test case
print "TEST:"
my_solution = Solution()
print 'result:' + str(my_solution.strStr('abcdefgabc','efg')) + ' expected: 4' 
print 'result:' + str(my_solution.strStr('abc','abcefg')) + ' expected: -1'
print 'result:' + str(my_solution.strStr(None,'efg')) + ' expected: -1'
print 'result:' + str(my_solution.strStr('abc', None)) + ' expected: -1'
print 'result:' + str(my_solution.strStr('','efg')) + ' expected: -1'
print 'result:' + str(my_solution.strStr('abcdefgabc','')) + ' expected: 0'
print 'result:' + str(my_solution.strStr('','')) + ' expected: 0'
