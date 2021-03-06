import os
import time
from subprocess import call
import cv2
import html_converter
from dotenv import load_dotenv

def runYolo(img):
    load_dotenv()
    img = cv2.imread(img)
    img = cv2.resize(img,(308,504))
    img2 = cv2.imwrite("data/test.jpg",img)

    darknet_path = os.getenv("DARKNET_BINARY_PATH")
    datacfg = os.getenv("DATA_CFG")
    cfgfile = os.getenv("CFG_FILE")
    weightfile = os.getenv("WEIGHT_FILE")
    img = 'data/test.jpg'

    call(darknet_path + " detector test " + datacfg + " " + cfgfile + " " + weightfile + " " + img, shell=True)

    f = open(os.getenv("BBOX_OUTPUT_FILE"),"r")
    boundingBoxes = []
    parsedObjects = []
    for line in f:
        boundingBoxes.append(line)

    for j in range(len(boundingBoxes)):
        parsedData = boundingBoxes[j].split(',')
        parsedObjects.append({
            'objID': parsedData[0],
            'name': parsedData[1],
            'xPos': int(parsedData[2]) * 2,
            'yPos': int(parsedData[3]) * 2,
            'width': int(parsedData[4]) * 2,
            'height': int(parsedData[5].rstrip()) * 2
        })

    return html_converter.yoloToHTML(parsedObjects)
