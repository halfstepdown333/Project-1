import re
import os
import sys

#modified extract from wordCountTest.py in repository
# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: Decoder.py <input text file> <output file> ")
    exit()

userInput = sys.argv[1] #stores file name (input)
outputFile = sys.argv[2] #stores file name (output)

#first check to make sure program exists
if not os.path.exists(userInput):
    print ("File doesn't exist! Exiting" % userInput)
    exit()



with open(userInput, "r") as f:
    data = f.read()
    clean = re.sub('[^A-Za-z0-9]+', ' ', data)

words = clean.split()

counts = dict()

for word in words:
    if word in counts:
        counts[word.lower()] += 1
    else:
        counts[word.lower()] = 1

tf = open(outputFile, "w+")
for x, y in sorted(counts.items()):
    tf.write(str(x) + ' : ' + str(y) + '\n')

tf.close()
