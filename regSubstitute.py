import re
o=re.compile("cat",re.I)
n="rat"
data= """CAt. My cat is white.
 It's a lucky CAT. Cat blah blah"""
#p= "cat"
var=re.subn(o,n,data,count=2) #count gives no.of ax subsiute req
print(var)
#if var:
 	#print("Pattern Found",var.start(),var.end(),var.span(),var.group())
#else:
 	#print("Pattern Not Found")
