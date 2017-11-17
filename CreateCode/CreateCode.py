'''
When run, creates a copy of itself, then runs that copy if it's file clone instance is less than n.
The file always runs, it should determine whether to kill itself.

To create the copy, the script will read itself and then reprint itself in a new file.

Perhaps with error.

The copy filename will have  "_n" added to it, where n ranges from 1 to 9, as inputted at runtime. 
n Defaults to 4

Test Driven Development is used.
'''

def readAndCopyMyself(myname):
    '''
    iterator.
    is given a string, myname, and reads myname.py line by line and outputs it as a string, via yield.

    '''
    #with open(myname, encoding='utf-8') as a_file:
    #    for a_line in a_file:
    #        yield a_line
    pass