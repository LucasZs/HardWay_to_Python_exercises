# http://learnpythonthehardway.org/book/ex6.html

x = "There are %d types of people." % 10    # String putting inside string no. 1.
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)    # String putting inside string no. 2.

print(x)
print(y)

print ("I said %r." % x)        # String putting inside string no. 3.
print("I also said '%s'." % y)  # String putting inside string no. 4.

hilarious = False
joke_evaluation = "Isn't joke so funny?! %r"

print (joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print (w + e)