import sys
import ijson
frequentauthors=[]
for line in sys.stdin: 
	line = line.strip()
	frequentauthors.append(line) #READING THE OUTPUT OF REDUCER 1 AND APPENDING IT INTO A LIST

with open("DBLP_DATA.json", "r") as f: #READING THE WHOLE JSON FILE 
	for record in ijson.items(f, "item"):
		try:
			if record['author'] in frequentauthors: #IF THE NAME OF THE AUTHOR IN THE JASON FILE EXISTS IN THE OUTPUT FROM REDUCER 1 PRINT IT
				print("%s,%s" %(record['author'],1)) 
		except:
			pass
#IN THIS WAY ALL THE OCCURENCES OF ALL THE AUTHORS IN THE OUTPUT OF REDUCER1 ARE PRINTED WITH 1