import re
p=".*"  #gives all char except new line #like read first line
#o=re.compile("cat",re.I)
#n="rat"
data= """2@CAt. My cat is white.
 It's a lucky CAT. Cat blah blah
 My cat is beautiful cat"""
#p= "cat"
var=re.search(p,data,re.I|re.DOTALL) #count gives no.of ax subsiute req
print(var)
#if var:
 	#print("Pattern Found",var.start(),var.end(),var.span(),var.group())
#else:
 	#print("Pattern Not Found")
