import os
import time

def yoloToHTML():
    test = [
    {
    'name': 'image',
    'yPos': '93',
    'height': '114',
    'width': '290',
    'objID': '0',
    'xPos': '254'
    }, 
    {
    'name': 'button',
    'yPos': '287',
    'height': '129',
    'width': '198',
    'objID': '1',
    'xPos': '147'
    }, 
    {
    'name': 'radiobutton',
    'yPos': '104',
    'height': '102',
    'width': '242',
    'objID': '3',
    'xPos': '390'
    }, 
    {
    'name': 'checkbox',
    'yPos': '411',
    'height': '140',
    'width': '181',
    'objID': '2',
    'xPos': '125'
    },
    ]
    
    htmlImage=r'<img src="smiley.gif" alt="Smiley face"'
    htmlButton=r'<button type="button"'
    htmlRadioButton=r'<input type="radio" name="gender" value="male"'
    htmlCheckbox=r'<input type="checkbox" name="vehicle1" value="Bike"'
    outputHtmlText=r'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta http-equiv="X-UA-Compatible" content="ie=edge"><title>Document</title></head><body>' + "\n"

    addedArray = []

    for i in test:
        addedArray.append(int(i["yPos"]))

    addedArray = sorted(addedArray)
    
    for i in addedArray:
        for t in test:
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

    print("Filename: {}\nFilepath: {}".format(filename,path))

yoloToHTML()
