import sys, os
sys.path.insert(0, os.getcwd() + os.path.sep + 'Recursion')

from template1 import recursion_function

try:
    recursion_function(5)
    print 'Success!'
except:
    print 'Oops, something wrong and you should take a look.'
