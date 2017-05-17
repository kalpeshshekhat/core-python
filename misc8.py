def books(book1, book2) :
  print "first book name is : %s" % book1
  print "second book name is :%s" % book2

books("the_white_tiger", "life_of_pi")

def book_prices(p1, p2, book1, book2) :
    print "price for %s" %book1
    print "is : %d" % p1
    print "price for %s" %book2
    print "is : %d" % p2

book_prices(1200, 900, "the_white_tiger", "life_of_pi")

def total(t1) :
    print "total for these books is : %d" % t1

total(1200 + 900)
