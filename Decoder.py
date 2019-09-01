import re


with open("speech.txt", "r") as f:
    data = f.read()
    clean = re.sub('[^A-Za-z0-9]+', ' ', data)

words = clean.split()

counts = dict()

for word in words:
    if word in counts:
        counts[word.lower()] += 1
    else:
        counts[word.lower()] = 1

tf = open("test.txt", "w")
for x, y in sorted(counts.items(),key=str, reverse=False):
    tf.write(str(x) + ' : ' + str(y) + '\n')

tf.close()
