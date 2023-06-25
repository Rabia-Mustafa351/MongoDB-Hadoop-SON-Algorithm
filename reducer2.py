import sys
st=500
authors={}
for line in sys.stdin:
	line = line.strip()
	authorname=line[:-2] 
	if authorname not in authors: #IF THE NAME OF AUTHOR DOESN'T EXISTS IN DICTIONARY ADD IT TO THE DICTIONARY OTHERWISE INCREMENT ITS COUNT
		authors[authorname]=1
	else:
		authors[authorname]+=1
		  
f = open("myfile1.txt", "x")	#WRITING THE NAMES OF ALL THE FREQUENT AUTHORS (WITH COUNT GREATER THAN OR EQUALS TO THE SUPPORT THRESHOLD) AND THEIR COUNT IN A TEXT FILE	
for i in authors:
	if authors[i]>=st:
		f.write(i)
		f.write(", ")
		f.write(str(authors[i]))
		f.write("\n")
f.close()		
