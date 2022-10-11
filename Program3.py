import sys
print (sys.argv)
s=""
for a in sys.argv[1:]:
	s = s + a + " "

print ("Concatinated Strings are --> ", s)