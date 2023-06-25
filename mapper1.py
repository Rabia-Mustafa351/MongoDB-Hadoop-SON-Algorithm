import sys
t=62.5
dict1={}
word = None
for line in sys.stdin:
	line = line.strip()
	words = line.split(",") #SPLITTING ON THE BASIS OF COMA
	if words[0][1:7]=="author": #IF AUTHOR FOUND
		authorname=(words[0][11:-1]) #PUT AUTHORNAME EQUALS TO THE NAME OF THE THE AUTHOR
		if authorname not in dict1: #IF THE NAME OF AUTHOR DOESN'T EXISTS IN DICTIONARY ADD IT TO THE DICTIONARY OTHERWISE INCREMENT ITS COUNT
			dict1[authorname]=1
		else:
			dict1[authorname]+=1
for i in dict1:
	if dict1[i]>=t:	#IF THE AUTHORS COUNT IS GREATER THAN OR EQUALS TO THE SMALLER THRESHOLD PRINT IT WITH 1 
		print(i,1)
		
