import sys
import screed 

filename = sys.argv[1]
#print filename

count = 0
for record in screed.open(filename):
   count += 1
   if count > 10:
   	break  
   print record


