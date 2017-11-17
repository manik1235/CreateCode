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
    
    known_values = (('example1.py',["print('My Name is example 1')",
                                    "print('Today is Tuesday November 3rd, 1972.')",
                                    "print('Do not buy my famous cakes!')",
                                    "print('Thank you')"]))
    
    def test_readAndCopyMyself(self):
        '''given a py filename, it should output the contents line by line.'''
        for inputfile, filecontents in self.known_values:
            result = tuple(CreateCode.readAndCopyMyself(inputfile)) # Output a list of the contents of an iterator with the file contents
            print('filecontents={},\nresult={}'.format(filecontents,result))
            self.assertEqual(filecontents, result)

if __name__ == '__main__':
    unittest.main()

