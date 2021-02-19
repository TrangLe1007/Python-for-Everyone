fname = input("Enter file name: ")
fh = open(fname)
count=0
for line in fh:
 line=line.rstrip()
 word=line.split()
 if len(word) < 1 or word[0] != "From":
  continue
 print(word[1])
 count=count+1
print("There were",count,"lines in the file with From as the first word")
