import re
import os
import sys

# set input and output files taken from wordCountTest.py in project repo
if len(sys.argv) is not 3:
    print("Correct usage: Decoder.py <input text file> <output file> ")
    exit()

userInput = sys.argv[1]
outputFile = sys.argv[2]

#first check to make sure program exists
if not os.path.exists("wordCount.py"):
    print ("wordCount.py doesn't exist! Exiting")
    exit()



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
