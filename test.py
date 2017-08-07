import sys, os
sys.path.insert(0, os.getcwd() + os.path.sep + 'Recursion')

from template1 import recursion_function
import strstr 
import strstr_v2

# Recursion tempalte test
#try:
#    recursion_function(5)
#    print 'Success!'
#except:
#    print 'Oops, something wrong and you should take a look.'

# TEST strStr() O(n^2)
print "TEST: strStr() O(n^2)"
new_solution = strstr.Solution()
try:
    print new_solution.strStr('abcd', 'bc')
    print 'Success!'
except:
    print 'Oops, something wrong with your program.'
# TEST strStr() O(n^2)
print "TEST: strStr() O(n^2)"
new_solution = strstr_v2.Solution()
try:
    print new_solution.strStr('12345', 'bcd')
    print 'Success!'
except:
    print 'Oops, something wrong with your program.'
