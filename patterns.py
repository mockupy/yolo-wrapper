import time

def generate_scaffold(cssPath, body):
    outputHtmlText = "<!DOCTYPE html><html lang='en'>\n<head>\n<meta charset='UTF-8'>\n"
    outputHtmlText += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"
    outputHtmlText += "<meta http-equiv='X-UA-Compatible' content='ie=edge'>\n"
    outputHtmlText += "<link href='"+ cssPath +"' rel='stylesheet'>\n"
    outputHtmlText += "<title>Mockupy</title>\n</head><body>\n"
    outputHtmlText += body + "</body>\n</html>"
    return outputHtmlText

def generate_image(xPos, yPos, height, width):
    selector = "image" + str(int(time.time()))
    imgOutput = "<img id='"+ selector +"' src='https://via.placeholder.com/"+ str(width) +"x"+ str(height) +"'>"
    generate_css(xPos, yPos, height, width, selector)
    return imgOutput

def generate_button(xPos, yPos, height, width):
    selector = "button" + str(int(time.time()))
    buttonOutput = "<button id='"+ selector +"'>Button</button>"
    generate_css(xPos, yPos, height, width, selector)
    return buttonOutput

def generate_radiobutton(xPos, yPos, height, width):
    selector = "rbutton" + str(int(time.time()))
    rButtonOutput = "<input type='radio' id='"+ selector +"'>\n"
    rButtonOutput += "<label for='"+ selector +"'>Radio button label</label>"
    generate_css(xPos, yPos, height, width, selector)
    return rButtonOutput

def generate_checkbox(xPos, yPos, height, width):
    selector = "checkbox" + str(int(time.time()))
    checkboxOutput = "<input type='checkbox' id='"+ selector +"'>\n"
    checkboxOutput += "<label for='"+ selector +"'>Checkbox label</label>"
    generate_css(xPos, yPos, height, width, selector)
    return checkboxOutput

def generate_css(xPos, yPos, height, width, selector):
    cssPath = "./data/output.css"
    with open(cssPath, "a") as f:
        cssOutput = "#"+ selector + "{\n"
        cssOutput += "position: absolute;\ntop:"+ str(yPos) + "px;\nleft:"+str(xPos)+"px;\n}\n"
        f.write(cssOutput)
        f.close()

def initialize_output_css():
        cssPath = "./data/output.css"
        open(cssPath, 'w').close()
