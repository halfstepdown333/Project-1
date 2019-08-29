
with open("speech.txt", "r") as f:
    data = f.read()

words = data.split()

counts = dict()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

tf = open("test.txt", "w")
for x, y in counts.items():
    tf.write(str(x) + ' : ' + str(y) + '\n')

tf.close()
