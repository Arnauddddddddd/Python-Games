import pyxel

pyxel.init(256,258,title="Escape")


king_x = 126
king_y = 252
space_memory = 0
fall = ['left', 'right']
stop_fall = True
stop_jump = False
level = 1
platforms = []
destroy = ["Off", "On"]

class Platform:
    def __init__(self, x, y, speed_x, speed_y, length, width, color, counter, sens):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.length = length
        self.width = width
        self.color = color
        self.counter = counter
        self.sens = sens



p1 = Platform(-5, 255, 0, 0, 300, 3, 1, 0, False)
p2 = Platform(0, 102, 0, 0, 51, 153, 1, 0, False)
p3 = Platform(63, 234, 0, 0, 30, 21, 5, 0, False)  #5 couleur moyenne platforme
p4 = Platform(150, 63, 0, 0, 150, 192, 1, 0, False)
p5 = Platform(135, 222, 0, 0, 15, 3, 4, 0, False)  #4 couleur petite platforme bois
p6 = Platform(51, 213, 0, 0, 30, 21, 5, 0, False)
p7 = Platform(60, 189, 0, 0, 30, 21, 5, 0, False)
p8 = Platform(135, 186, 0, 0, 15, 3, 4, 0, False)
p9 = Platform(57, 210, 0, 0, 51, 3, 6, 0, False)
p10 = Platform(72, 159, 0, 0, 21, 30, 5, 0, False)
p11 = Platform(147, 165, 0, 0, 6, 3, 1, 0, False)   #1 couleur micro platforme
p12 = Platform(147, 144, 0, 0, 6, 3, 1, 0, False)
p13 = Platform(48, 171, 0, 0, 6, 3, 1, 0, False)
p14 = Platform(48, 144, 0, 0, 6, 3, 1, 0, False)
p15 = Platform(48, 120, 0, 0, 6, 3, 1, 0, False)
p16 = Platform(98, 96, 0, 0, 52, 3, 4, 0, False)
p17 = Platform(147, 72, 0, 0, 6, 3, 1, 0, False)
p18 = Platform(0, 0, 0, 0, 42, 153, 1, 0, False)
p19 = Platform(0, 0, 0, 0, 300, 33, 1, 0, False)

p20 = Platform(0, 63, 0, 0, 51, 201, 1, 0, False)
p21 = Platform(81, 21, 0, 0, 21, 201, 1, 0, False)
p22 = Platform(-5, 240, 0, 0, 300, 18, 1, 0, False)
p23 = Platform(177, 219, 0, 0, 30, 21, 5, 0, False)
p24 = Platform(210, 219, 0, 0, 30, 21, 5, 0, False)
p25 = Platform(186, 198, 0, 0, 30, 21, 5, 0, False)
p26 = Platform(216, 189, 0, 0, 21, 30, 5, 0, False)
p27 = Platform(102, 207, 0, 0, 21, 3, 4, 0, False)
p28 = Platform(201, 168, 0, 0, 30, 21, 5, 0, False)
p29 = Platform(102, 183, 0, 0, 3, 3, 1, 0, False)
p30 = Platform(102, 159, 0, 0, 3, 3, 1, 0, False)
p31 = Platform(162, 165, 0, 0, 81, 3, 6, 0, False)
p32 = Platform(162, 102, 0, 0, 201, 18, 1, 0, False)
p46 = Platform(102, 90, 0, 0, 21, 3, 4, 0, False)
p47 = Platform(141, 63, 0, 0, 9, 9, 21, 0, False)
p48 = Platform(102, 63, 0, 0, 3, 3, 1, 0, False)
p49 = Platform(219, 51, 0, 0, 9, 9, 21, 0, False)
p50 = Platform(186, 69, 0, 0, 9, 9, 21, 0, False)
p51 = Platform(246, 69, 0, 0, 9, 9, 21, 0, False)



p33 = Platform(42, 222, 0, 0, 9, 9, 20, 0, False)
p34 = Platform(0, 102, 0, 0, 201, 18, 1, 0, False)
p35 = Platform(87, 201, 0, 0, 9, 9, 20, 0, False)
p36 = Platform(63, 180, 0, 0, 9, 9, 20, 0, False)
p37 = Platform(111, 165, 0, 0, 9, 9, 20, 0, False)
p38 = Platform(141, 180, 0, 0, 9, 9, 20, 0, False)
p39 = Platform(168, 201, 0, 0, 9, 9, 20, 0, False)
p40 = Platform(195, 177, 0, 0, 9, 9, 20, 0, False)
p41 = Platform(240, 60, 0, 0, 20, 250, 1, 0, False)
p42 = Platform(225, 153, 0, 0, 15, 3, 4, 0, False)
p43 = Platform(237, 132, 0, 0, 3, 3, 1, 0, False)
p44 = Platform(237, 111, 0, 0, 3, 3, 1, 0, False)
p45 = Platform(0, 0, 0, 0, 75, 33, 1, 0, False)
p52 = Platform(9, 72, 0, 0, 9, 9, 21, 0, False)
p53 = Platform(39, 60, 0, 0, 9, 9, 21, 0, False)
p54 = Platform(66, 66, 0, 0, 9, 9, 21, 0, False)
p55 = Platform(81, 51, 1, 0, 27, 3, 22, 0, False)
p56 = Platform(222, 51, -1, 0, 27, 3, 22, 0, False)


def all_levels(platforms, level):
    if level == 1:
        platforms = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19]
    if level == 2:
        platforms = [p20, p19, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p46, p47, p48, p49, p50, p51]
    if level == 3:
        platforms = [p34, p22, p33, p35, p36, p37, p38, p39, p40, p41, p42, p43, p44, p45, p52, p53, p54, p55, p56]
    if level == 4:
        platforms = []
    if level == 5:
        platforms = []
    
    
    
   
        
        
    
    return platforms, level
    

def change_level(king_x, king_y, level, platforms):
    if king_x > 255:
        level += 1
        king_x = 0
        
    if king_x < 0:
        level -= 1
        king_x = 255
    
    return king_x, king_y, level, platforms


def press(space_memory,  fall, stop_fall):
    
    if stop_fall == True:            
       if pyxel.btn(pyxel.KEY_SPACE):
           space_memory = 10 
            
    return space_memory, fall, stop_fall

def movements(x):
    if pyxel.btn(pyxel.KEY_RIGHT) and wall_left(platforms) == False:
        x += 3
    if pyxel.btn(pyxel.KEY_LEFT) and wall_right(platforms) == False:
        x -= 3
    return x
    
    


def jump(x, y, space_memory, fall, stop_fall, stop_jump, platforms):
    if stop_jump == True:
        space_memory = 0
        
    if space_memory > 0:     
        y-= 1
        y-= 1
        y-= 1
        space_memory -= 1
       
    if stop_fall == False and space_memory == 0 and floor(platforms) == False:        
        y += 1
        y += 1
        y += 1       
    return x, y, space_memory, fall, stop_fall, stop_jump, platforms



def reset(king_x, king_y, level, stop_fall):    
    if pyxel.btn(pyxel.KEY_Z):
        king_y -= 3
        stop_fall = True
    if pyxel.btn(pyxel.KEY_S):
        king_y += 3
        stop_fall = True
    if pyxel.btn(pyxel.KEY_Q):
        king_x -= 3
        stop_fall = True
    if pyxel.btn(pyxel.KEY_D):
        king_x += 3
        stop_fall = True
    if pyxel.btn(pyxel.KEY_T):
        level += 1
    if pyxel.btn(pyxel.KEY_G):
        level -= 1
        
    if  king_y > 260 and level == 1 :       
        king_x = 222
        king_y = 252
    
       
    return king_x, king_y, level, stop_fall


def ceiling(platforms):
    for i in range(len(platforms)):
        if (king_x > platforms[i].x-3) and (king_x < platforms[i].x + platforms[i].length) and (king_y == platforms[i].y + platforms[i].width):
            return True
    else:
        return False

    
def floor(platforms):    
    for i in range(len(platforms)):
        if (king_x >= platforms[i].x and king_x <= (platforms[i].x + platforms[i].length) and (king_y == platforms[i].y-3)):
            return True   
    else:
        return False
 
 
def wall_right(platforms):
    for i in range(len(platforms)):
        if king_y > (platforms[i].y-3) and king_y <= (platforms[i].y-3 + platforms[i].width) and king_x == (platforms[i].x + platforms[i].length):
            return True   
    else:
        return False
    


def wall_left(platforms):
    for i in range(len(platforms)):
        if king_y > (platforms[i].y-3) and king_y <= (platforms[i].y-3 + platforms[i].width) and king_x == platforms[i].x-3:
            return True   
    else:
        return False
 
 

def platform_move(king_x, king_y, platforms, stop_fall):
    for i in range(len(platforms)):
        if platforms[i].counter == 50:
            platforms[i].sens = True
        if platforms[i].counter == 0:
            platforms[i].sens = False
            
        if (pyxel.frame_count % 1) == 0 and platforms[i].sens == False:
            platforms[i].x += platforms[i].speed_x
            platforms[i].y += platforms[i].speed_y
            platforms[i].counter += 1
            if king_x >= platforms[i].x and king_x <= platforms[i].x + platforms[i].length and (king_y == platforms[i].y-3):
                king_x += platforms[i].speed_x
                king_y += platforms[i].speed_y
                
                               
        if (pyxel.frame_count % 1) == 0  and platforms[i].sens == True:
            platforms[i].x -= platforms[i].speed_x
            platforms[i].y -= platforms[i].speed_y
            platforms[i].counter -= 1
            
            if king_x >= platforms[i].x and king_x <= platforms[i].x + platforms[i].length and (king_y == platforms[i].y-3):
                king_x -= platforms[i].speed_x
                king_y -= platforms[i].speed_y
                                
       
    return king_x, king_y, platforms, stop_fall
        
        
    
    
def update():
    global king_x, king_y, space_memory, fall, stop_fall, stop_jump, platforms, level
    
    king_x, king_y, platforms, stop_fall = platform_move(king_x, king_y, platforms, stop_fall)
    
    stop_fall = floor(platforms)
    stop_jump = ceiling(platforms)
        
    king_x, king_y, level, stop_fall = reset(king_x, king_y, level, stop_fall)
    king_x, king_y, level, platforms = change_level(king_x, king_y, level, platforms)
    platforms, level = all_levels(platforms, level)
    
    
    space_memory, fall, stop_fall = press(space_memory, fall, stop_fall)
    king_x, king_y, space_memory, fall, stop_fall, stop_jump, platforms = jump(king_x, king_y, space_memory, fall, stop_fall, stop_jump, platforms)
    king_x = movements(king_x)
   
   
def draw():
    pyxel.cls(0)

    
    pyxel.rect(0, 0, 256, 258, 0)
    
    
    pyxel.text(110,12.5, str(king_x),13)
    pyxel.text(110,20.5, str(king_y),13)
    
    pyxel.rect(king_x, king_y, 3, 3, 7)    
    
    
    
    
    #platforms
    
        
    for i in range(len(platforms)):
       
       
       
        # y =  120 
        final_y = 102        
        if platforms[i].color == 20:
            if (pyxel.frame_count % 1) == 0 :
                    pyxel.rect(platforms[i].x, platforms[i].y, platforms[i].length, platforms[i].width, 4)
                    pyxel.rect(platforms[i].x+4, final_y+18  , 1,  255-final_y-(255-platforms[i].y)-18, 7)
            
        
        final_y2 = 15        
        if platforms[i].color == 21:
            if (pyxel.frame_count % 1) == 0 :
                    pyxel.rect(platforms[i].x, platforms[i].y, platforms[i].length, platforms[i].width, 4)
                    pyxel.rect(platforms[i].x+4, final_y2+18  , 1,  255-final_y2-(255-platforms[i].y)-18, 7)
        
        
        final_y3 = -20        
        if platforms[i].color == 22:
            if (pyxel.frame_count % 1) == 0 :
                    pyxel.rect(platforms[i].x, platforms[i].y, platforms[i].length, platforms[i].width, 5)
                    pyxel.rect(platforms[i].x+13, final_y3+18  , 1,  255-final_y3-(255-platforms[i].y)-18, 7)
        
        
        if platforms[i].color <= 13:
            if platforms[i].color == 5:
                if (pyxel.frame_count % 1) == 0 :
                    pyxel.rect(platforms[i].x, platforms[i].y, platforms[i].length, platforms[i].width, 1)
                
                if (pyxel.frame_count % 1) == 0 :
                    pyxel.rect(platforms[i].x+1, platforms[i].y+1, platforms[i].length-2, platforms[i].width-2, platforms[i].color)
            else:
                if (pyxel.frame_count % 1) == 0 :
                    pyxel.rect(platforms[i].x, platforms[i].y, platforms[i].length, platforms[i].width, platforms[i].color)
                
        
            
        
   
                        
             
     
  
    
pyxel.run(update, draw)

    
    

    
