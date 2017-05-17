def math1(a1, a2, a3, a4):
    return a1 + a2 / a3 - a4

b1 = 24
b2 = 34
b3 = 100
b4 = 1023

a5 = math1(b1, b2, b3, b4)

print "Result of first math operation is : %d" % a5

c1 = 100
c2 = 350

def math2(b5, d1, d2):
    return b5 + d1 * d2

a6 = math2(a5, c1, c2)

print "Result of second math operation is : %d" % a6
