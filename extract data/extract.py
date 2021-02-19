import re
name = input("Enter the file:")
fh = open(name)
lst = list()
for line in fh:
    line = line.rstrip()
#extracting the number into the list
    num = re.findall('[0-9]+', line)
    lst = lst + num
print(lst)
