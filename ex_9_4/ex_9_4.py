name = input("Enter file")
fh = open(name)
name=list()

#look for the person who sent the mail
for line in fh:
    line=line.rstrip()
    words = line.split()
    if len(words) < 1 or words[0] != "From":
        continue
    else:
        name.append(words[1])

#Map the name and the time they sent the mail
count=dict()
for element in name:
    count[element]=count.get(element,0)+1

#Get the frequent people who sent the most mail
bigName = None
bigCount = None
for element,count in count.items():
    if bigCount is None or count > bigCount:
        bigCount = count
        bigName = element

#result
print(bigName,bigCount)
