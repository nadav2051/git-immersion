import sys
name = "World"
if (len(sys.argv) > 1):
	name = str(sys.argv[1])
print "Hello " + name + "!"
