fname = input ("Enter file name")
fh = open(fname)
count = 0
total = 0
for line in fh:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        number = line.find(":")
        extractNum = float(line[number+2:])
        total = total + extractNum
print("Average spam confidence:", total/count)
