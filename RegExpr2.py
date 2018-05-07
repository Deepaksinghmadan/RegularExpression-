import re
p=re.compile("    rat,re.X|re.I")
#data= """CAt. My cat is white.
 #It's a lucky CAT. Cat blah blah"""
#p= "cat"
var=re.search(p,data,re.I)
#if var:
 	#print("Pattern Found",var.start(),var.end(),var.span(),var.group())
#else:
 	#print("Pattern Not Found")
