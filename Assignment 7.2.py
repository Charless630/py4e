fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0


for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        pos = line.find(':')
        value = float(line[pos + 1:])
        total = total + value

average = total / count if count != 0 else 0

print('Average spam confidence:', average)