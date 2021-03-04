value1 = 256
value2 = 256
value3 = 256
state = -1
numImage = 0
myText = ""
level = 0
inPalette = 0

def setup():
    
    size(1000, 780)
    background(256, 256, 256) #rgb
    frameRate(200)
    
    textAlign(100, 700)
    fill(0)
    
def draw(): 
    global value1
    global value2
    global value3
    global myText
    global numImage
    global level
    global inPalette
    
    textSize(30)
    text(myText, 100, 700, 900, 50)
    
    #instructions for each level
    if level == 0:
        textSize(30)
        text("Welcome to Color KickStart!", 300, 300, 900, 50)
        text("Click '/' to start playing", 320, 420, 1000, 50)

    if level == 1:
        textSize(20)
        text("LEVEL 1", 10, 95, 900, 50)
        text("Type in the names of the three primary colors", 10, 120, 1000, 50)
        text("**Your guess is incorrect if it does not make a color appear in the palette**", 10, 195, 900, 50)
        textSize(15)
        text("To move on to the next level or to go back to a previous one, press the '>' and '<' keys", 10, 240, 900, 50)
            
    if level == 2:
        textSize(20)
        text("LEVEL 2", 10, 95, 900, 50)
        text("Type in the names of the seven colors of the rainbow (hint: use the acronym 'ROYGBIV')", 10, 120, 1000, 50)
        text("**Your guess is incorrect if it does not make a color appear in the palette**", 10, 195, 900, 50)
        textSize(15)
        text("To move on to the next level or to go back to a previous one, press the '>' and '<' keys", 10, 240, 900, 50)
        
    if level == 3:
        textSize(20)
        text("LEVEL 3", 10, 95, 900, 50)
        text("Type in the names of ten of the most well known colors (hint: white is not one of them!)", 10, 120, 1000, 50)
        text("**Your guess is incorrect if it does not make a color appear in the palette**", 10, 195, 900, 50)
        textSize(15)
        text("To move on to the next level or to go back to a previous one, press the '>' and '<' keys", 10, 240, 900, 50)
        
    if level == 4:
        textSize(20)
        text("LEVEL 4", 10, 95, 900, 50)
        text("Type in the names of five different shades of red", 10, 120, 1000, 50)
        text("**Your guess is incorrect if it does not make a color appear in the palette**", 10, 195, 900, 50)
        textSize(15)
        text("To move on to the next level or to go back to a previous one, press the '>' and '<' keys", 10, 240, 900, 50)
        
    if level == 5:
        textSize(20)
        text("LEVEL 5", 10, 95, 900, 50)
        text("Type in the names of five different shades of green", 10, 120, 1000, 50)
        text("**Your guess is incorrect if it does not make a color appear in the palette**", 10, 195, 900, 50)
        textSize(15)
        text("To move on to the next level or to go back to a previous one, press the '>' and '<' keys", 10, 240, 900, 50)
        
    if level == 6:
        textSize(20)
        text("LEVEL 6", 10, 95, 900, 50)
        text("Type in the names of five different shades of blue", 10, 120, 1000, 50)
        text("**Your guess is incorrect if it does not make a color appear in the palette**", 10, 195, 900, 50)
        textSize(15)
        text("To move on to the next level or to go back to a previous one, press the '>' and '<' keys", 10, 240, 900, 50)
    
    if level == 7: #white
        textSize(30)
        text("Congratulations! You have completed the game!", 150, 300, 900, 50)
        fill(255)
        noStroke()
        rect(10, 100, 1000, 205)
        
    
    #creates palettes
    if level == 1: #primary colors
        if myText == "red":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(256, 0, 0) #red
            rect(30, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
        if myText == "blue":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(0, 0, 256) #blue
            rect(85, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
        if myText == "yellow":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(256, 256, 0) #yellow
            rect(140, 20, 55, 55, 7)
            myText = ""
            inPalette += 1

        if inPalette == 3:
            fill(0)
            text("Press cooresponding numbers on your keyboard, then click and drag to use colors in your palette", 10, 145, 1000, 50)
            text("Click the 's' key to stop using a certain color", 10, 170, 900, 50)
            text("Press 'q' to generate a random picture to color in; press '-' to reset your drawing", 10, 220, 900, 50)
            inPalette = 0
        
    if level == 2: #rainbow
            
        if myText == "red":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(256, 0, 0) #red
            rect(30, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
            
        if myText == "orange":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(255, 128, 0) #orange
            rect(85, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "yellow":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(256, 256, 0) #yellow
            rect(140, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "green":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(0, 256, 0) #green
            rect(195, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "blue":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(0, 0, 256) #blue
            rect(250, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
        
        if myText == "indigo":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(75, 0, 130) #indigo
            rect(305, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
            
        if myText == "violet":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(148, 0, 211) #violet
            rect(360, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
        
        if inPalette == 7:
            fill(0)
            text("Press cooresponding numbers on your keyboard, then click and drag to use colors in your palette", 10, 145, 1000, 50)
            text("Click the 's' key to stop using a certain color", 10, 170, 900, 50)
            text("Press 'q' to generate a random picture to color in; press '-' to reset your drawing", 10, 220, 900, 50)
            inPalette = 0
            
    if level == 3: #ten most common colors (not including white)
        if myText == "red":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(256, 0, 0) #red
            rect(30, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
            
        if myText == "orange":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(255, 128, 0) #orange
            rect(85, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "yellow":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(256, 256, 0) #yellow
            rect(140, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "green":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(0, 256, 0) #green
            rect(195, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "blue":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(0, 0, 256) #blue
            rect(250, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "purple":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(127, 0, 255) #purple
            rect(305, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "pink":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(255, 51, 255) #pink
            rect(360, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "black":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(0, 0, 0) #black
            rect(415, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "grey" or myText == "gray":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(160, 160, 160) #grey
            rect(470, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
            
        if myText == "brown":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(102, 51, 0) #brown
            rect(525, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
            
        if inPalette == 10:
            fill(0)
            text("Press cooresponding numbers on your keyboard, then click and drag to use colors in your palette", 10, 145, 1000, 50)
            text("Click the 's' key to stop using a certain color", 10, 170, 900, 50)
            text("Press 'q' to generate a random picture to color in; press '-' to reset your drawing", 10, 220, 900, 50)
            inPalette = 0
    
    if level == 4: #shades of red
        if myText == "dark red":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(139, 0, 0) #dark red
            rect(30, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
            
        if myText == "maroon":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(128, 0, 0) #maroon
            rect(85, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "brick":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(178, 34, 34) #brick
            rect(140, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "crimson":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(220, 20, 60) #crimson
            rect(195, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "tomato":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(225, 99, 71) #tomato
            rect(250, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
            
        if inPalette == 5:
            fill(0)
            text("Press cooresponding numbers on your keyboard, then click and drag to use colors in your palette", 10, 145, 1000, 50)
            text("Click the 's' key to stop using a certain color", 10, 170, 900, 50)
            text("Press 'q' to generate a random picture to color in; press '-' to reset your drawing", 10, 220, 900, 50)
            inPalette = 0
        
    if level == 5: #shades of green
        if myText == "dark green":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(0,100,0) #dark green
            rect(30, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
            
        if myText == "forest":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(34,139,34) #forest green
            rect(85, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "lime":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(0,255,0) #lime
            rect(140, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "sea":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(46,139,87) #sea green
            rect(195, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "pale":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(152,251,152) #pale green
            rect(250, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
            
        if inPalette == 5:
            fill(0)
            text("Press cooresponding numbers on your keyboard, then click and drag to use colors in your palette", 10, 145, 1000, 50)
            text("Click the 's' key to stop using a certain color", 10, 170, 900, 50)
            text("Press 'q' to generate a random picture to color in; press '-' to reset your drawing", 10, 220, 900, 50)
            inPalette = 0
            
    if level == 6: #shades of blue
        if myText == "dark blue":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(0,0,139) #dark blue
            rect(30, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
            
        if myText == "cyan":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(0,255,255) #cyan
            rect(85, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "navy":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(0,0,128) #navy
            rect(140, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "sky":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(135,206,235) #sky blue
            rect(195, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
    
        if myText == "royal":
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
            fill(65,105,225) #royal blue
            rect(250, 20, 55, 55, 7)
            myText = ""
            inPalette += 1
            
        if inPalette == 5:
            fill(0)
            text("Press cooresponding numbers on your keyboard, then click and drag to use colors in your palette", 10, 145, 1000, 50)
            text("Click the 's' key to stop using a certain color", 10, 170, 900, 50)
            text("Press 'q' to generate a random picture to color in; press '-' to reset your drawing", 10, 220, 900, 50)
            inPalette = 0
            
        

    #defines state in which coloring function will work
    if state > -1:
        fill(value1, value2, value3)
        stroke(value1, value2, value3)
        strokeWeight(3)
        line(mouseX, mouseY, pmouseX, pmouseY)    
    
    fill(0) #makes text black
    
def mouseDragged(): 
    global value1
    global value2
    global value3
    global state
    global numImage 
    
    #selects/defines color to draw with
    if level == 1:
        if state == 1: #red
            value1 = 256
            value2 = 0
            value3 = 0
        elif state == 2: #blue
            value1 = 0
            value2 = 0
            value3 = 256
        elif state == 3: #yellow
            value1 = 256
            value2 = 256
            value3 = 0
        
    if level == 2:
        if state == 1: #red
            value1 = 256
            value2 = 0
            value3 = 0
        elif state == 2: #orange
            value1 = 255
            value2 = 128
            value3 = 0
        elif state == 3: #yellow
            value1 = 256
            value2 = 256
            value3 = 0
        elif state == 4: #green
            value1 = 0
            value2 = 256
            value3 = 0
        elif state == 5: #blue
            value1 = 0
            value2 = 0
            value3 = 256
        elif state == 6: #indigo
            value1 = 75
            value2 = 0
            value3 = 130
        elif state == 7: #violet
            value1 = 148
            value2 = 0
            value3 = 211
        
    if level == 3:
        if state == 1: #red
            value1 = 256
            value2 = 0
            value3 = 0
        elif state == 2: #orange
            value1 = 255
            value2 = 128
            value3 = 0
        elif state == 3: #yellow
            value1 = 256
            value2 = 256
            value3 = 0
        elif state == 4: #green
            value1 = 0
            value2 = 256
            value3 = 0
        elif state == 5: #blue
            value1 = 0
            value2 = 0
            value3 = 256
        elif state == 6: #purple
            value1 = 127
            value2 = 0
            value3 = 255
        elif state == 7: #pink
            value1 = 255
            value2 = 51
            value3 = 255
        elif state == 8: #black
            value1 = 0
            value2 = 0
            value3 = 0
        elif state == 9: #grey
            value1 = 160
            value2 = 160
            value3 = 160
        elif state == 0: #brown
            value1 = 102
            value2 = 51
            value3 = 0
        
    if level == 4:
        if state == 1: #dark red
            value1 = 139
            value2 = 0
            value3 = 0
        elif state == 2: #maroon
            value1 = 128
            value2 = 0
            value3 = 0
        elif state == 3: #brick
            value1 = 178
            value2 = 34
            value3 = 34
        elif state == 4: #crimson
            value1 = 220
            value2 = 20
            value3 = 60
        elif state == 5: #tomato
            value1 = 225
            value2 = 99
            value3 = 71
    
    if level == 5:
        if state == 1: #dark green
            value1 = 0
            value2 = 100
            value3 = 0
        elif state == 2: #forest green
            value1 = 34
            value2 = 139
            value3 = 34
        elif state == 3: #lime
            value1 = 0
            value2 = 255
            value3 = 0
        elif state == 4: #sea green
            value1 = 46
            value2 = 139
            value3 = 87
        elif state == 5: #pale green
            value1 = 152
            value2 = 251
            value3 = 152
    
    if level == 6:
        if state == 1: #dark blue
            value1 = 0
            value2 = 0
            value3 = 139
        elif state == 2: #cyan
            value1 = 0
            value2 = 255
            value3 = 255
        elif state == 3: #navy
            value1 = 0
            value2 = 0
            value3 = 128
        elif state == 4: #sky blue
            value1 = 135
            value2 = 206
            value3 = 235
        elif state == 5: #royal blue
            value1 = 65
            value2 = 105
            value3 = 225
        
def keyPressed():
    global state
    global myText
    global value1
    global value2
    global value3
    global numImage
    global level
    global inPalette
    
    #creates typing system
    if keyCode == 8:
        if len(myText) > 0: 
            myText = myText[:-1]
            fill(255, 255, 255)
            noStroke()
            rect(100, 700, 900, 50)
    elif keyCode == DELETE or keyCode == RETURN:
        myText = ""
    elif keyCode != SHIFT and keyCode != CONTROL and keyCode != ALT:
        myText = myText + key
    
    #sets the value of state
    if key == '1':
        state = 1 
        myText = ""
    if key == '2':
        state = 2
        myText = ""
    if key == '3':
        state = 3
        myText = ""
    if key == '4':
        state = 4
        myText = ""
    if key == '5':
        state = 5
        myText = ""
    if key == '6':
        state = 6
        myText = ""
    if key == '7':
        state = 7
        myText = ""
    if key == '8':
        state = 8
        myText = ""
    if key == '9':
        state = 9
        myText = ""
    if key == '0':
        state = 0
        myText = ""
    
    #to stop using a color
    if key == 's':
        state = -1
        myText = ""
        
    #to load a different image to draw
    if key == 'q':
        numImage += 1
        
        if numImage >= 0 and numImage < 11:
            fill(255)
            noStroke()
            rect(100, 250, 400, 400)
        if numImage > 10:
            numImage = 1
            fill(255)
            noStroke()
            rect(100, 250, 400, 400)
            
        if numImage == 1:
            doggo = loadImage("doggo.png")
            image(doggo, 100, 250, 400, 400)
        if numImage == 2:
            butter = loadImage("butterfly.gif")
            image(butter, 100, 250, 400, 400)
        if numImage == 3:
            ariel = loadImage("Ariel.png")
            image(ariel, 100, 250, 400, 400)
        if numImage == 4:
            bee = loadImage("bee.png")
            image(bee, 100, 250, 400, 400)
        if numImage == 5:
            goat = loadImage("GOAT.gif")
            image(goat, 100, 250, 400, 400)
        if numImage == 6:
            minion = loadImage("Minions.png")
            image(minion, 100, 250, 400, 400)
        if numImage == 7:
            owhl = loadImage("owhl.gif")
            image(owhl, 100, 250, 400, 400)
        if numImage == 8:
            cookie = loadImage("cookie.png")
            image(cookie, 100, 250, 400, 400)
        if numImage == 9:
            bob = loadImage("Spongebob.png")
            image(bob, 100, 250, 400, 400)
        if numImage == 10:
            turtle = loadImage("turtle.gif")
            image(turtle, 100, 250, 400, 400)
            
        myText = ""
    
    #to change levels
    if level > 0 and level < 8:
        if key == '>':
            level += 1
            fill(255)
            noStroke()
            rect(30, 20, 900, 60, 7)
            fill(255)
            noStroke()
            rect (10, 95, 1000, 50)
            fill(255)
            noStroke()
            rect(0, 250, 1000, 1000)
            myText = ""
        if key == '<':
            level -= 1
            fill(255)
            noStroke()
            rect(30, 20, 900, 60, 7)
            fill(255)
            noStroke()
            rect (10, 95, 1000, 50)
            fill(255)
            noStroke()
            rect(0, 250, 1000, 1000)
            myText = ""
    elif level > 7:
        myText = ""
        

    #to start the game
    if level == 0:
        if key == '/':
            level = 1
            fill(255)
            noStroke()
            rect (300, 300, 1000, 200)
            myText = ""
            
            
    #to reset an image (delete all coloring)
    if key == '-':
        fill(255)
        noStroke()
        rect(0, 250, 1000, 1000)
        
        if numImage == 1:
            doggo = loadImage("doggo.png")
            image(doggo, 100, 250, 400, 400)
        if numImage == 2:
            butter = loadImage("butterfly.gif")
            image(butter, 100, 250, 400, 400)
        if numImage == 3:
            ariel = loadImage("Ariel.png")
            image(ariel, 100, 250, 400, 400)
        if numImage == 4:
            bee = loadImage("bee.png")
            image(bee, 100, 250, 400, 400)
        if numImage == 5:
            goat = loadImage("GOAT.gif")
            image(goat, 100, 250, 400, 400)
        if numImage == 6:
            minion = loadImage("Minions.png")
            image(minion, 100, 250, 400, 400)
        if numImage == 7:
            owhl = loadImage("owhl.gif")
            image(owhl, 100, 250, 400, 400)
        if numImage == 8:
            cookie = loadImage("cookie.png")
            image(cookie, 100, 250, 400, 400)
        if numImage == 9:
            bob = loadImage("Spongebob.png")
            image(bob, 100, 250, 400, 400)
        if numImage == 10:
            turtle = loadImage("turtle.gif")
            image(turtle, 100, 250, 400, 400)
            
        myText = ""
