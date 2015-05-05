# Author: Nadav Luzzato (nadav2051@gmail.com)
import sys
from greeter import Greeter
name = "World"
# Comment for git
if (len(sys.argv) > 1):
	name = str(sys.argv[1])
greeter = Greeter(name)
greeter.greet()
