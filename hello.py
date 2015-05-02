# Author: Nadav Luzzato (nadav2051@gmail.com)
import sys
name = "World"
# Comment for git
if (len(sys.argv) > 1):
	name = str(sys.argv[1])
print "Hello " + name + "!"
