import re
import os
import sys

#modified extract from wordCountTest.py in repository
# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: Decoder.py <input text file> <output file> ") #correct syntax for operating Decoder.py in terminal
    exit()

userInput = sys.argv[1] #stores file name (input)
outputFile = sys.argv[2] #stores file name (output)

#first check to make sure program exists
if not os.path.exists(userInput):
    print ("File doesn't exist! Exiting" % userInput)
    exit()



with open(userInput, "r") as f:
    data = f.read()
    clean = re.sub('[^A-Za-z0-9]+', ' ', data) #removes punctuations and sets a space after the word

words = clean.split()   #splits the words into a list

counts = {}   #space to save the words

for word in words:
    if word in counts:
        counts[word.lower()] += 1  #Every time an element matches with another it updates
    else:
        counts[word.lower()] = 1   #Else word was only found once

tf = open(outputFile, "w+")
for x, y in sorted(counts.items()):    #writes to file items of the dictionary 
    tf.write(str(x) + ' : ' + str(y) + '\n')

tf.close()
