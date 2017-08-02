import sys, os
sys.path.insert(0, os.getcwd() + os.path.sep + 'Recursion')

from template1 import recursion_function
import strstr 

# Recursion tempalte test
#try:
#    recursion_function(5)
#    print 'Success!'
#except:
#    print 'Oops, something wrong and you should take a look.'

# strStr() test O(n^2)
print "TEST: strStr() O(n^2)"
new_solution = strstr.Solution()
print new_solution.strStr('abcd', 'bc')
