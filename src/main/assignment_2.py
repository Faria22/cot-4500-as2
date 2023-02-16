def createMantisa(s):
    num = 0
    for n, l in enumerate(s, 1):
        num += int(l)*2**(-1*n)
    return num

def convertNum(s):
    sign = int(s[0])
    c = int(s[1:12], 2)
    f = createMantisa(s[12:])
    return (-1)**sign * 2**(c-1023) * (1+f)

def findPoint(s):
    try:
        return s.index('.')
    except:
        return -1

def digitChopping(n, d):
    pIndex = findPoint(str(n))
    if pIndex != -1:
        n = n*10**(-pIndex)
        n = int(n*10**(d))
        n = n*10**(-d+pIndex)
        return n

def minNumTerms(prec):
    i = 0
    func = lambda x: x**3
    while func(i) < prec:
        i += 1
    return i
    
def digitRounding(n, d):
    pIndex = findPoint(str(n))
    if pIndex != -1:
        n = n*10**(-pIndex)
        n = int(n*10**(d)+0.5)
        n = n*10**(-d+pIndex)
        return n

def absoluteError(ext, app):
    return abs(ext-app)

def relativeError(ext, app):
    return abs(ext-app)/ext

def newtonian(val, prec):
    i = 0

    f = lambda x: x**3 + 4*x**2-10
    d = lambda x: 3*x**2 + 8*x

    while abs(f(val)/d(val)) > prec:
        i += 1
        val = val - f(val)/d(val)
    return i

def bisection(left, right, prec):
    i = 0

    f = lambda x: x**3 + 4*x**2-10

    while abs(left-right) > prec:
        i += 1
        p = (left+right)/2
        if (f(left) < 0 and f(p) > 0) or (f(left)>0 and f(p)<0):
            right = p
        else:
            left = p
    return i

s = '010000000111111010111001'

# Adds all the zeros
s = s+'0'*(64-len(s))

num = convertNum(s)
print(num)
print()
print(digitChopping(num, 3))
print()
app = digitRounding(num, 3)
print(app)
print()
print(absoluteError(num, app))
print()
print(relativeError(num, app))
print()
print(minNumTerms(10**4))
print()
print(bisection(-4, 7, 10**(-4)))
print()
print(newtonian(7, 10**(-4)))
