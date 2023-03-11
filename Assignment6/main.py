import js
p5 = js.window

state = 'PAUSE'

class Player:  
    x = 0  # set x at 0
    y = 0  # set y at 0
    distance_x = 0
    distance_y = 0
    
    def __init__(self, x, y, distance_x, distance_y):
        self.x = x  # initialize attribute x 
        self.y = y  # initialize attribute y 
        self.distance_x = distance_x
        self.distance_y = distance_y

    def draw(self,r,g,b):
        p5.fill(r,g,b)
        p5.noStroke()
        p5.push()
        p5.translate(self.x, self.y)
        p5.rect(-5, 5, 15, 5)
        p5.rect(0, 0, 5, 15)
        p5.pop()

    def move_enemy(self):
        self.x = self.x + self.distance_x
        self.y = self.y + self.distance_y
    
    def move_player(self, distance_x, distance_y):
        self.x = self.x + distance_x
        self.y = self.y + distance_y
    
def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 
player = Player(150,150,0,0)
enemy = Player(100,100,p5.random(0,2),p5.random(4,6))

def draw():
    p5.background(255)        
    player.draw(245, 221, 66)
    enemy.draw(198, 29, 245)
    enemy.move_enemy()

    #setting limit for enemy
    if(300 < enemy.x or 0 > enemy.x):
        enemy.distance_x *= -1
    if(300 < enemy.y or 0 > enemy.y):
        enemy.distance_y *= -1
    
    dis = p5.dist(player.x , player.y , enemy.x , enemy.y)

    if(dis <= 15):
        player.distance_x = 0
        player.distance_y = 0
        enemy.distance_x = 0
        enemy.distance_y = 0

        p5.fill(0)
        p5.textSize(27)
        p5.text("TRY AGAIN",100,100)
        
def keyPressed(event):
    if(300 > player.x and player.x > 0):
        if(p5.keyCode == p5.RIGHT_ARROW):
           print('move point 10 pixels to the right..')
           player.move_player(10, 0)
        if(p5.keyCode == p5.LEFT_ARROW):
            print('move point 10 pixels to the left..')
            player.move_player(-10, 0)

    if(0 >= player.x):
        if(p5.keyCode == p5.RIGHT_ARROW):
            print('move point 10 pixels to the right..')
            player.move_player(10, 0) 

    if(300 <= player.x):
        if(p5.keyCode == p5.LEFT_ARROW):
            print('move point 10 pixels to the left..')
            player.move_player(-10, 0)  
            
def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass
