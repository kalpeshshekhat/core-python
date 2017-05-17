def for_loop_range(i,j,d1):
    numbers = []
    for i in range(i,j,d1):
        numbers.append(i)
#    while i < d1:
#        print "At the top i is %d" % i
#
#        numbers.append(i)
#
#        i = i + j
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers

digits = for_loop_range(5,100,10)
print "The numbers: "

for num in digits:
    print num
