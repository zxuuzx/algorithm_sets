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
    def strStr(self, haystack, needle):
        """Find if needle in haystack."""
        m = len(haystack)
        n = len(needle)
        # Edge
        if needle is None or n == 0:
            return -1
        if haystack is None or m == 0:
            return -1
        if m < n:
            return -1
        # sliding window witdth
        for i in range(m + n - 1):
            for j in range(n):
                if haystack[i + j] != needle[j]:
                    break
                if j == n - 1:
                    return i 
        return -1
