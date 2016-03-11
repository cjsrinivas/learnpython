fruits = ['apple','bannana','pear','grapes','orange']
counter = 0
for fruit in fruits:
    print "%s is an awesome fruit" % fruit
    counter += 1
    print "The counter is %d" % counter
    if counter == 2:
        break
