name = "Inigo Montoya" # you killed my father, prepare to die
age = 35 # lying
height = 69 # not lying
weight = 185 # lbs
eyes = 'Brown'
teeth = 'White' # why it gotta be white?
hair = 'Mohawked' # FTW

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)