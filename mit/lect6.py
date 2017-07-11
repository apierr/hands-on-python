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
        hanoi(n - 1, source, target, helper)
        hanoi(1, source, helper, target)
        hanoi(n - 1, helper, source, target)

# hanoi(2, 'source', 'temp', 'target')

def toChars(s):
    import string
    return string.lower(s)

def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])

def isPalindrome(s):
    """Returns True if s is a palindrome and False otherwise"""
    return isPal(toChars(s))

#print isPalindrome('Anna Anna')