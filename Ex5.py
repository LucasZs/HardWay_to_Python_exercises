# http://learnpythonthehardway.org/book/ex5.html

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print ("Let's talk about %s." % my_name)
print ("He's %s inches tall." % my_height)
print ("He's %s pounds heavy." % my_weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight ))

name = 'Zed A. Shaw'
age = 35 # not a lie
height = (my_height * 2.54)# cm
weight = (my_weight * 0.453) # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print ("Let's talk about %s." % name)
print ("He's %s cm tall." % height)
print ("He's %s kg heavy." % weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (eyes, hair))
print ("His teeth are usually %s depending on the coffee." % teeth)


print ("If I add %d, %d and %d I get %d." % (age, height, weight, age + height + weight ))