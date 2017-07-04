# Approximation
# find a y s.t. y * y = x +- epsilon (specification)
# brute-force search or exhaustive enumeration

def square_root(x = 2, epsilon = 0.01, stepSize = 0.00001):
    numGuesses = 0
    ans = 0.0
    while abs(ans ** 2 - x) >= epsilon and ans <= x:
        ans += stepSize
        numGuesses += 1
    print 'numGuesses = ', numGuesses
    if abs(ans ** 2 - x) >= epsilon:
        print 'Failed on square root of ', x
    else:
        print ans, 'is close to square root of', x

square_root(12345)

# Bisection search: cut search space in half each iteration

def square_root_log(x = 2, epsilon = 0.01, stepSize = 0.00001):
    numGuesses = 0
    low = 0.0
    high = x
    ans = (high + low) / 2.0
    while abs(ans ** 2 - x) >= epsilon and ans <= x:
        numGuesses += 1
        if ans ** 2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    print 'numGuesses = ', numGuesses
    print ans, 'is close to square root of', x

square_root_log(12345)