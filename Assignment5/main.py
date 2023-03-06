import js
p5 = js.window

program_state = 'state1'
program_timer = p5.millis()

def setup():
    p5.createCanvas(300, 300) # 300 x 300 pixel canvas
    print('finished setup')
    p5.mousePressed(mousePressed)
    p5.keyPressed(keyPressed)

def draw():
    global program_state
    global program_timer
    p5.background(255) # white background
    draw_tree()
    draw_ground()
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
    p5.strokeWeight(2) # set stroke thickness
    
    if program_state == 'state1':
        p5.fill(150,180,50)
    elif program_state == 'state2':
        p5.fill(255,0,100)
    elif program_state == 'state3':
        p5.fill(0, 255, 255)
    p5.ellipse(150,100,100,150)

#change from state1 to state2 after 3 seconds
    if p5.millis() > program_timer + 3000:
        program_state = 'state2'
        print("3 seconds have passed")
        print(program_state)
        program_timer = p5.millis()

def mousePressed(event):
    global program_timer
    global program_state
    print('mousePressed..')
    if program_state == 'state2':
        program_state = 'state3'
        program_timer = p5.millis() # update program timer
        print('change program_state to ' + program_state)
    elif program_state == 'state3':
        program_state = 'state1'
        program_timer = p5.millis() # update program timer
        print('change program_state to ' + program_state)

def keyPressed(event):
    print('keyPressed.. ' + str(p5.key))
    global program_state
    if program_state == 'state1' and p5.key == '2':
        program_state = 'state2'
        print(program_state)
    elif program_state == 'state2' and p5.key == '3':
        program_state = 'state3'
        print(program_state)
    elif program_state == 'state3' and p5.key == '1':
        program_state = 'state1'
        print(program_state)


def draw_tree():
    p5.noStroke()
    p5.fill(150,100,50)
    p5.rect(140,100,20,100)
    
def draw_ground():
    p5.noStroke()
    p5.fill(150,180,50)
    p5.rect(0,200,300,200)
    p5.fill(150,100,50)
    p5.rect(0,225,300,75)
