import argparse
from subprocess import call
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(parser.parse_args())

img = cv2.imread(args["image"])
img = cv2.resize(img,(508,704))
img2 = cv2.imwrite("data/testbeh.jpg",img)

darknet_path = 'darknet.exe detector test'
datacfg = 'data/obj.data'
cfgfile = 'yolo-obj.cfg'
weightfile = 'yolo-obj_11000.weights'
img = 'data/testbeh.jpg'

call(darknet_path + " " + datacfg + " " + cfgfile + " " + weightfile + " " + img, shell=True)

f = open("BBoxOutputFile.txt","r")
myList = []
finaldict = []
for line in f:
    myList.append(line)

for j in range(len(myList)):
    parsedData = myList[j].split(',')
    finaldict.append({
        'objID': parsedData[0],
        'name': parsedData[1],
        'xPos': parsedData[2],
        'yPos': parsedData[3],
        'width': parsedData[4],
        'height': parsedData[5].rstrip()
    })
print(finaldict)