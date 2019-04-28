import os
import time

def yoloToHTML(predictions):
    htmlImage=r'<img src="smiley.gif" alt="Smiley face"'
    htmlButton=r'<button type="button"'
    htmlRadioButton=r'<input type="radio" name="gender" value="male"'
    htmlCheckbox=r'<input type="checkbox" name="vehicle1" value="Bike"'
    outputHtmlText=r'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta http-equiv="X-UA-Compatible" content="ie=edge"><title>Document</title></head><body>' + "\n"

    addedArray = []

    for i in predictions:
        addedArray.append(int(i["yPos"]))

    addedArray = sorted(addedArray)
    
    for i in addedArray:
        for t in predictions:
            if i == (int(t["yPos"])):
                if (t['name']=='image'):
                    height=t['height']
                    width=t['width']
                    outputHtmlText += htmlImage + " height ='{}'".format(height) + " width='{}'".format(width) + ">" +"\n"
                
                if (t['name']=='button'):
                    height=t['height']
                    width=t['width']
                    outputHtmlText+=htmlButton + " height = '{}'".format(height) + " width='{}'".format(width) + "></button>" + "\n"
                
                if (t['name']=='checkbox'):
                    height=t['height']
                    width=t['width']
                    outputHtmlText+=htmlCheckbox + " height = '{}'".format(height) + " width='{}'".format(width) + ">" + "\n"
                
                if (t['name']=='radiobutton'):
                    height=t['height']
                    width=t['width']
                    outputHtmlText+=htmlRadioButton + " height = '{}'".format(height) + " width='{}'".format(width) + ">" + "\n"

    lastBody = r'</body></html>'

    path = os.getcwd() + "/output"

    str(int(time.time())) + "yolo.html"

    filename = str(int(time.time())) + "yolo.html"

    savedpath = path + "/" + filename

    if not os.path.exists(path):
         os.makedirs(os.path.dirname(savedpath))
         
    with open(savedpath, "w") as f:
         f.write(outputHtmlText+lastBody)
         f.close()

    return savedpath
