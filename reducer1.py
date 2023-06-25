import sys
authors=[]
for line in sys.stdin:
	if line[:-3] not in authors: #DISREGARDING THE COUNT OF AUTHORS, ONLY THOSE AUTHOR NAMES WERE APPENDED INTO THE LIST THAT WERE NOT PRESENT BEFORE, HENCE MAKING THEM UNIQUE
		authors.append(line[:-3])
		
		
		
		
f = open("myfile.txt", "x")		 #THE NAMES OF FREQUENT AUTHORS FROM ALL THE CHUNKS (MADE UNIQUE) WERE WRITTEN INTO A FILE TO BE PROCESSED BY MAPPPER 2
for i in authors:
	f.write(i)
	f.write("\n")
f.close()
