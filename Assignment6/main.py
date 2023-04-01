import js
p5 = js.window

program_state = 'start'
#bg image
bg = p5.loadImage('bg.png')  # load image data to bg
#set font
font = p5.loadFont('PressStart2P.otf')

class Player:  
    x = 150  # set x at 150
    y = 215  # set y at 225

    player_img = p5.loadImage('player.png')  # load image data to player
    
    def draw(self):
        p5.image(self.player_img, self.x, self.y)

    def move_player(self, distance_x, distance_y):
        self.x = self.x + distance_x
        self.y = self.y + distance_y

class Iceberg:
    x = 0
    y = 0
    speed = 0


    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        
class Big(Iceberg):
    ib_1 = p5.loadImage('ib_1.png')
    def draw(self):
        p5.image(self.ib_1, self.x, self.y)


class Medium(Iceberg):
    ib_2 = p5.loadImage('ib_2.png')
    def draw(self):
        p5.image(self.ib_2, self.x, self.y)

class Small(Iceberg):
    ib_3 = p5.loadImage('ib_3.png')
    def draw(self):
        p5.image(self.ib_3, self.x, self.y)

class Background():
    x = 0
    y = 0
    bg = p5.loadImage('bg.png')
    def draw(self):
        p5.image(self.bg, self.x, self.y)

def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 

player = Player()    
ib_1 = Big(p5.random(1,255),0,0.75)
ib_2 = Medium(p5.random(1,255),0,1.5)
ib_3 = Small(p5.random(1,255),0,2)
background = Background()

def draw():
    global program_state
    p5.background(255) 
    background.draw()
    if (program_state == 'start'):
        p5.fill(255)
        p5.textFont(font)
        p5.textSize(20)
        p5.text('ARCTIC VOYAGE', 25, 115)
        p5.textSize(10)
        p5.text('click anywhere to start!', 40,130) 
        
    player.draw()
    
    dis1 = p5.dist(player.x , player.y , ib_1.x , ib_1.y)
    dis2 = p5.dist(player.x , player.y , ib_2.x , ib_2.y)
    dis3 = p5.dist(player.x , player.y , ib_3.x , ib_3.y)
    
    if (program_state == 'play'):
        p5.fill(255)
        
        ib_1.draw()
        if (ib_1.y == 300):
            resetProj(ib_1)
            
        ib_2.draw()
        if (ib_2.y == 300):
            resetProj(ib_2)
            
        ib_3.draw()
        if (ib_3.y == 300):
            resetProj(ib_3)

        ib_1.y = ib_1.y + ib_1.speed
        ib_2.y = ib_2.y + ib_2.speed
        ib_3.y = ib_3.y + ib_3.speed
    
    
    if (dis1 <= 25 or dis2 <= 25 or dis3 <= 25):

        program_state = 'gameover'
        
        p5.fill(255)
        p5.textFont(font)
        p5.textSize(20)
        p5.text("TRY AGAIN",50,100)
        p5.textSize(9)
        p5.text("click anywhere to restart game",15,125)

def resetProj(proj):
    proj.y = 0
    proj.x = p5.random(1,300)
    
def keyPressed(event): 
    global program_state
        
    if(program_state == 'play'):
        if(300 > player.x and player.x > 0):
            if(p5.keyCode == p5.RIGHT_ARROW):
                player.move_player(10, 0)
            if(p5.keyCode == p5.LEFT_ARROW):
                player.move_player(-10, 0)
                
        if(0 >= player.x):
            if(p5.keyCode == p5.RIGHT_ARROW):
                player.move_player(10, 0) 
                
        if(300 <= player.x):
            if(p5.keyCode == p5.LEFT_ARROW):
                player.move_player(-10, 0)   

def keyReleased(event):
    pass

def mousePressed(event):
    global program_state
    
    if(program_state == 'start'):
        program_state = 'play'

    elif(program_state == 'gameover'):
        program_state = 'start'

def mouseReleased(event):
    pass
    
