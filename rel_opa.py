# lt(), le() and eq() gt(), ge() and ne()
import operator
a = 3
b = 3
# using lt() to check if a is less than b
if operator.lt(a,b):
    print ("3 is less than 3")
else : print ("3 is not less than 3")
# using le() to check if a is less than or equal to b
if(operator.le(a,b)):
    print ("3 is less than or equal to 3")
else : print ("3 is not less than or equal to 3")
# using eq() to check if a is equal to b
if (operator.eq(a,b)):
    print ("3 is equal to 3")
else : print ("3 is not equal to 3")

c = 4
d = 3
# using gt() to check if c is greater than d
if (operator.gt(c,d)):
    print ("4 is greater than 3")
else : print ("4 is not greater than 3")
# using ge() to check if c is greater than or equal to d
if (operator.ge(c,d)):
    print ("4 is greater than or equal to 3")
else : print ("4 is not greater than or equal to 3")
# using ne() to check if c is not equal to d
if (operator.ne(c,d)):
    print ("4 is not equal to 3")
else : print ("4 is equal to 3")