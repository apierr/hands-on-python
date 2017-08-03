"""
Recursion
"""

def simpleExp(b, n):
    """
    Recursive power function
    """
    if n == 0:
        return 1
    return b * simpleExp(b, n - 1)

print simpleExp(2, 2)
print simpleExp(2, 8)

def hanoi(n, source, helper, target):
    """
    The Tower of Hanoi problem with 3 pegs and n disks takes  2**n - 1 moves to solve
    n is the number of disks
    source is the first pole
    helper is the pole used for transferring
    target is the pole for the destination of the transferred disk
    """
    if n == 1:
        print 'move from ' + source, ' to ', target
    else:
        hanoi(n - 1, source, target, helper) # remove n − 1 discs to get access to the nth one.
        hanoi(1, source, helper, target)
        hanoi(n - 1, helper, source, target)

# hanoi(2, 'source', 'temp', 'target')

def toLowerCase(str):
    import string
    return string.lower(str)

def isPal(str):
    if len(str) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])

def isPalindrome(str):
    """Returns True if s is a palindrome and False otherwise"""
    return isPal(toLowerCase(sre))

#print isPalindrome('Anna Anna')