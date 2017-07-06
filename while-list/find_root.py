def isEven(i):
    """
    assumes i a positive int
    returns True if i is even, otherwise False
    """
    return i%2 == 0


def withinEpsilon(x, y, epsilon):
    """
    x,y,epsilon ints or floats.  epsilon > 0.0
    returns True if x is within epsilon of y
    """
    return abs(x - y) <= epsilon

def findRoot(pwr, val, epsilon):
    """
    assume pwr an int; val, epsilon floats
    pwr and espilon > 0
    if it exists,
        return a value within epsilon of val**pwr
        otherwise returns None
    """
    assert type(pwr) == int and type(val) == float and type(epsilon) == float
    assert pwr > 0 and epsilon > 0
    if isEven(pwr) and val < 0:
        return None
    low = -abs(val)
    high = max(abs(val), 1.0)
    ans = (high + low)/2.0
    while not withinEpsilon(ans**pwr, val, epsilon):
        #print 'ans =', ans, 'low =', low, 'high =', high
        if ans**pwr < val:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return ans

print findRoot(3, -27.0, 0.0001)