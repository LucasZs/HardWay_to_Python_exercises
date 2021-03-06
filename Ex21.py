#http://learnpythonthehardway.org/book/ex21.html

def add(a, b):
    print ("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print ("SUBTRACTING %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print ("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print ("DIVIDING %d / %d" % (a, b))
    return a / b


print ("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print ("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))


# A puzzle for the extra credit, type it in anyway.
print ("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
other_form = age + (height - (weight * (iq / 2)))
simple_formula = (2 + 2) / (2 * 2)
simple_formula_with_functions = divide((add(2, 2)), (multiply(2, 2)))

print ("That becomes: ", what, "Can you do it by hand?")
print ("That becomes: ", other_form, "Can you do it by hand?")
print (simple_formula)
print (simple_formula_with_functions)