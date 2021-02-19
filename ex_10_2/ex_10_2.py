name = input("Enter the name:")
fh = open(name)

#seaching for the line start with "From" and append list of time
lst =list()
for line in fh:
    line=line.rstrip()
    words = line.split()
    if len(words) < 1 or words[0] != "From":
        continue
    else:
        lst.append(words[5])

#creating another list by hour
hour = list()
for time in lst:
    hours = time.split(":")
    hour.append(hours[0])

#counting how many times of each hour
dic = dict()
for k in hour:
    dic[k]=dic.get(k,0)+1

#sorting by hour
newLst = sorted(dic.items())
for k,v in newLst:
    print(k,v)
