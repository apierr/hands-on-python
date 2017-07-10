"""
Recursion
"""
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

hanoi(2, 'source', 'temp', 'target')