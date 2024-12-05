import sys, csv
from rc4 import *

ivFilename = "WEPOutputSim.csv"
rows = [[4,31,3,14],[5, 31, 30, 4],[6, 31, 5, 6],[7, 31, 21, 12],[8, 31, 27, 7],[9, 31, 14, 27],[10, 31, 19, 20],[11, 31, 15, 25],[12, 31, 23, 14], [13, 31, 19, 17],[14, 31, 21, 18],[15, 31, 5, 26],[16, 31, 5, 13],[17, 31, 18, 18],[18, 31, 29, 4]]
box = [] # S
# In WEP, the header of SNAP is always 'aa'.
plainSNAP = "aa"


#with open(ivFilename, 'r') as csvfile:
 #   csvreader = csv.reader(csvfile)
  #  for row in csvreader:
   #     rows.append(row)

keyLength = 16
#print("keyLength is: " + str(keyLength))
keyStreamByte_array = [14,16,14,6,22,25,4,17,2,17,15,2,9,22,4]
key = [None,None,None,None]
#for A in range(1,keyLength): # keyLength
    #prob = [0] * 32
for row in range(1,len(rows)+1):
    box.clear()
    for i in range(0,32):
        box.append(i)
    key[0] = int(rows[row-1][0])
    key[1] = int(rows[row-1][1])
    key[2] = int(rows[row-1][2])
    key[3] = int(rows[row-1][3])
    #print(key)
    j = 0
    #initSBox(box)
    # Simulate the S-Box after KSA initialization.
    for i in range(row + 3):
        j = (j + box[i] + key[i]) % 32
        swapValueByIndex(box, i, j)
        # Record the original box[0] and box[1] value.
        if i == 1:
            original0 = box[0]
            original1 = box[1]
    print(box)
    i = row + 3
    z = box[1]
    # if resolved condition is possibly met.
    if z + box[z] == row + 3:
        # If the value of box[0] and box[1] has changed, discard this possibility.
        if (original0 != box[0] or original1 != box[1]):
            continue
        keyStreamByte = keyStreamByte_array[row-1]#int(row[3])
        #assert(box[z+box[z]] == keyStreamByte)
        #print(keyStreamByte)
        #print("j = "+str(j))
        #print("i = " +str(i))
        #print("S an Position i = "+str(box[i]))
        keyByte = (box.index(keyStreamByte) - j - box[i]) % 32
        #print(box[keyByte])
        #print(str(keyByte)+"\n")
        key.append(keyByte)
        #    prob[keyByte] += 1
        # Assume that the most hit is the correct password.
        #higherPossibility = prob.index(max(prob))
    #key.append(higherPossibility)

# Get rid of first 24-bit initialization vector.
#userInput = key[3:]
#result = [format(key, 'x') for key in userInput]
#rawkey = ''.join(result).upper()
#print(rawkey)
print(key[4:])