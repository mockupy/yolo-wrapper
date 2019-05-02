import os
import time
import patterns
import shutil

def yoloToHTML(predictions):

    addedArray = []
    bodyContent = ""

    for i in predictions:
        addedArray.append(int(i["yPos"]))

    addedArray = sorted(addedArray)
    
    for i in addedArray:
        for t in predictions:
            if i == (int(t["yPos"])):
                if (t['name']=='image'):
                    height=t['height']
                    width=t['width']
                    bodyContent += patterns.generate_image(t['xPos'], t['yPos'], height, width)
                
                if (t['name']=='button'):
                    height=t['height']
                    width=t['width']
                    bodyContent += patterns.generate_button(t['xPos'], t['yPos'], height, width)
                
                if (t['name']=='checkbox'):
                    height=t['height']
                    width=t['width']
                    bodyContent += patterns.generate_checkbox(t['xPos'], t['yPos'], height, width)
                
                if (t['name']=='radiobutton'):
                    height=t['height']
                    width=t['width']
                    bodyContent += patterns.generate_radiobutton(t['xPos'], t['yPos'], height, width)


    cssFilename = str(int(time.time())) + "yolo.css"
    cssPath = "./output/" + cssFilename
    shutil.copy("./data/output.css", cssPath)
    
    htmlOutput = patterns.generate_scaffold(cssPath, bodyContent)

    path = os.getcwd() + "/output"
    htmlFilename = str(int(time.time())) + "yolo.html"
    savedpath = path + "/" + htmlFilename

    if not os.path.exists(path):
         os.makedirs(os.path.dirname(savedpath))
         
    with open(savedpath, "w") as f:
         f.write(htmlOutput)
         f.close()

    return savedpath
