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
    selector = str(int(time.time())) + "image"
    imgOutput = "<img id='"+ selector +"' src='https://via.placeholder.com/"+ str(width) +"x"+ str(height) +"'>"
    generate_css(xPos, yPos, height, width, selector)
    return imgOutput

def generate_button(xPos, yPos, height, width):
    selector = str(int(time.time())) + "button"
    buttonOutput = "<button id='"+ selector +"'>Button</button>"
    generate_css(xPos, yPos, height, width, selector)
    return buttonOutput

def generate_radiobutton(xPos, yPos, height, width):
    selector = str(int(time.time())) + "rbutton"
    rButtonOutput = "<input type='radio' id='"+ selector +"'>\n"
    rButtonOutput += "<label for='"+ selector +"'>Radio button label</label>"
    generate_css(xPos, yPos, height, width, selector)
    return rButtonOutput

def generate_checkbox(xPos, yPos, height, width):
    selector = str(int(time.time())) + "checkbox"
    checkboxOutput = "<input type='checkbox' id='"+ selector +"'>\n"
    checkboxOutput += "<label for='"+ selector +"'>Checkbox label</label>"
    generate_css(xPos, yPos, height, width, selector)
    return checkboxOutput

def generate_css(xPos, yPos, height, width, selector):
    pass
