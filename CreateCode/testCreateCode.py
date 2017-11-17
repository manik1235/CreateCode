'''
Test for CreateCode.py
'''

#A test case answers a single question about the code it is testing. A test case should be able to...

#    ...run completely by itself, without any human input. Unit testing is about automation.
#    ...determine by itself whether the function it is testing has passed or failed, without a human interpreting the results.
#    ...run in isolation, separate from any other test cases (even if they test the same functions). Each test case is an island. 

import CreateCode
import unittest

class CopiesItself(unittest.TestCase):
    '''
    Test case for CreateCode
    '''
    
    known_values = (copyExample.py)
    
    def test_readAndCopyMyself(self):
        '''given a py filename, it should output the contents line by line.'''

