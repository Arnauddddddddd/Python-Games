import pyxel

pyxel.init(256,258,title="JumpKing")


king_x = 220
king_y = 252
right_memory = 0
left_memory = 0
fall = ['left', 'right']
stop_fall = True
stop_jump = False
level = 1
platforms = []
destroy = ["Off", "On"]

class Platform:
    def __init__(self, x, y, speed_x, speed_y, length, color, counter, sens):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.length = length
        self.color = color
        self.counter = counter
        self.sens = sens


p1 = Platform(205, 255, 0, 0, 30, 6, 0, False)
p2 = Platform(130, 231, 0, 0, 60, 3, 0, False)
p3 = Platform(80, 213, 0, 0, 30, 10, 0, False)
p4 = Platform(25, 192, 0, 0, 30, 10, 0, False)
p5 = Platform(115, 162, -1, 0, 30, 11, 0, False)
p6 = Platform(160, 141, 0, 0, 60, 3, 0, False)
p7 = Platform(100, 111, 0, 0, 30, 10, 0, False)
p8 = Platform(15, 90, 0, 0, 60, 3, 0, False)
p9 = Platform(105, 72, 1, 0, 30, 11, 0, False)
p10 = Platform(190, 51, 0, 0, 60, 3, 0, False)
p11 = Platform(125, 39, -1, 0, 30, 11, 0, False)
p12 = Platform(15, 12, 0, 0, 60, 3, 0, False)
p13 = Platform(105, 6, 0, 0, 60, 3, 0, False)

plat0 = Platform(195, 255, 0, 0, 60, 6, 0, False)    
plat1 = Platform(150, 240, 0, 0, 30, 10, 0, False)    
plat2 = Platform(72, 210, 1, 0, 30, 11, 0, False)
plat3 = Platform(25, 180, 0, 0, 30, 10, 0, False)
platt3 = Platform(30, 66, 0, 0, 30, 10, 0, False)
plat4 = Platform(100, 150, -1, 0, 30, 11, 0, False)
plat5 = Platform(170, 141, 0, 0, 10, 8, 0, False)
plat6 = Platform(220, 123, 0, 0, 30, 10, 0, False)
plat7 = Platform(170, 105, 0, 0, 20, 9, 0, False)
plat8 = Platform(80, 84, 2, 0, 20, 3, 0, False)
plat9 = Platform(180, 51, -2, 0, 20, 3, 0, False)
plat10 = Platform(220, 30, 0, 0, 20, 9, 0, False)
plat11 = Platform(170, 15, 0, 0, 10, 8, 0, False)
plat12 = Platform(110, 15, 0, 0, 10, 8, 0, False)

plat13 = Platform(0, 255, 0, 0, 75, 6, 0, False)
plat14 = Platform(100, 225, 0, 0, 20, 9, 0, False)
plat15 = Platform(139, 219, 0, 0, 10, 8, 0, False)
plat16 = Platform(169, 219, 0, 0, 10, 8, 0, False)
plat17 = Platform(70, 120, 0, 0, 10, 8, 0, False)
plat18 = Platform(225, 201, 0, 0, 20, 9, 0, False)
plat19 = Platform(40, 180, 1, 0, 30, 11, 3, False)
plat20 = Platform(130, 171, 0, 0, 75, 6, 0, False)
plat21 = Platform(25, 144, 0, 0, 30, 10, 0, False)
plat22 = Platform(95, 111, 2, 0, 10, 2, 0, False)
plat23 = Platform(225, 96, 0, 0, 20, 9, 0, False)
plat24 = Platform(120, 72, 0, 0, 75, 6, 0, False)
plat25 = Platform(0, 51, 0, 0, 75, 6, 0, False)
plat26 = Platform(200, 27, -2, 0, 20, 3, 0, False)
plat27 = Platform(40, 6, 0, 0, 75, 6, 0, False)

plat28 = Platform(0, 255, 0, 0, 60, 6, 0, False)
plat29 = Platform(6, 231, 2, 0, 20, 3, 0, False)
plat30 = Platform(236, 231, -2, 0, 20, 3, 0, False)
plat31 = Platform(122, 210, 0, 0, 20, 9, 0, False)
plat32 = Platform(196, 255, 0, 0, 60, 6, 0, False)
plat33 = Platform(10, 180, 2, 0, 10, 2, 0, False)
plat34 = Platform(240, 180, -2, 0, 10, 2, 0, False)
plat35 = Platform(122, 153, 0, 0, 20, 9, 0, False)
plat36 = Platform(205, 123, -3, 0, 20, 7, 0, False)
p36 = Platform(25, 90, 0, 0, 60, 3, 0, False)
plat37 = Platform(115, 66, 0, 0, 10, 8, 0, False)
plat38 = Platform(156, 57, 0, 0, 30, 10, 0, False)
plat39 = Platform(120, 33, 0, 0, 5, 0, 0, False)
plat40 = Platform(83, 24, 0, 0, 5, 0, 0, False)
plat41 = Platform(140, 6, 0, 0, 5, 0, 0, False)
plat42 = Platform(200, 6, 0, 0, 10, 8, 0, False)

pl1 = Platform(246, 255, 0, 0, 10, 8, 0, False)
pl2 = Platform(234, 213, 0, 0, 10, 8, 0, False)
pl3 = Platform(183, 201, 0, 0, 5, 0, 0, False)
pl4 = Platform(125, 192, 0, 0, 5, 0, 0, False)
pl5 = Platform(67, 183, 0, 0, 5, 0, 0, False)
pl6 = Platform(95, 141, 0, 0, 10, 8, 0, False)
pl7 = Platform(129, 102, 0, 0, 10, 8, 0, False)
pl8 = Platform(183, 153, 0, 0, 3, 14, 0, False)
pl9 = Platform(235, 141, 0, 0, 3, 14, 0, False)
pl10 = Platform(241, 102, 0, 0, 3, 14, 0, False)
pl11 = Platform(216, 96, 0, 0, 3, 14, 0, False)
pl12 = Platform(180, 57, 0, 0, 3, 14, 0, False)

plfinal = Platform(35, 33, 0, 0, 30, 15, 0, False)
plfinal2 = Platform(-1, 255, 0, 0, 260, 6, 0, False)

def all_levels(platforms, level, destroy):
    if level == 1:
        platforms = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13]
    if level == 2:
        platforms = [plat0, plat1, plat2, plat3,platt3, plat4, plat5, plat6, plat7, plat8, plat9, plat10, plat11, plat12, plat13]
    if level == 3:
        platforms = [plat13, plat14, plat15, plat16, plat17, plat18, plat19, plat20, plat21, plat22, plat23, plat24, plat25, plat26, plat27]
    if level == 4:
        platforms = [plat28, plat29, plat30, plat31, plat32, plat33, plat34, plat35, plat36, p36, plat37, plat38, plat39, plat40, plat41, plat42]
    if level == 5:
        platforms = [pl1, pl2, pl3, pl4, pl5, pl6, pl7, pl8, pl9, pl10, pl11, pl12, plat26, plfinal]
    
    
    
    if destroy == "On":
        platforms = []
        if level == 1:
            platforms = [plfinal2]
            
        
        
    
    return platforms, level, destroy
    

def change_level(king_x, king_y, level, platforms):
    if king_y <= 0 and level < 5:
        level += 1
        king_y = 255
    if king_y >= 258 and level > 1:
        level -= 1
        king_y = 0
    return king_x, king_y, level, platforms


def press(right_memory,left_memory,  fall, stop_fall):
    j = (pyxel.frame_count % 2) == 0
    if stop_fall == True:
        if pyxel.btn(pyxel.KEY_UP):
            right_memory = 0
            left_memory = 0
            
        if (pyxel.btn(pyxel.KEY_RIGHT) and right_memory < 15 and left_memory == 0):
                right_memory = right_memory + int(j)
                fall = 'right'
        if pyxel.btn(pyxel.KEY_LEFT) and left_memory < 15 and right_memory == 0:
            left_memory = left_memory + int(j)
            fall = 'left'
            
    return right_memory, left_memory, fall, stop_fall


def jump(x, y, right_memory, left_memory, fall, stop_fall, stop_jump, platforms):
    if stop_jump == True:
        right_memory = 0
        left_memory = 0
    
    if x > 255:
        left_memory = right_memory
        fall = 'left'
        right_memory = 0
        
        
    if x < 0:
        right_memory = left_memory
        fall = 'right'
        left_memory = 0
        
    
    if (not pyxel.btn(pyxel.KEY_RIGHT) or stop_fall == False) and right_memory > 0:
        if (pyxel.frame_count % 0.5) == 0 :
            y-= 3
            x+= 2
            right_memory -= 1            
        if right_memory == 1:
            if (pyxel.frame_count % 1.5) == 0 :
                x += 3            
    if right_memory == 0 and fall == 'right' and floor(platforms) == False:        
        y+= 3
        x+= 2
            
    if (not pyxel.btn(pyxel.KEY_LEFT) or stop_fall == False) and left_memory > 0:
        if (pyxel.frame_count % 0.5) == 0 :
            y-= 3
            x-= 2
            left_memory -= 1            
        if left_memory == 1:
            if (pyxel.frame_count % 1.5) == 0 :
                x -= 3                                
    if left_memory <= 0 and fall == 'left' and floor(platforms) == False:
        y+= 3
        x-= 2   
    return x, y, right_memory,left_memory, fall, stop_fall, stop_jump, platforms



def reset(king_x, king_y, level, stop_fall):    
    if pyxel.btn(pyxel.KEY_Z):
        king_y -= 6
        stop_fall = True
    if pyxel.btn(pyxel.KEY_S):
        king_y += 6
        stop_fall = True
    if pyxel.btn(pyxel.KEY_Q):
        king_x -= 6
        stop_fall = True
    if pyxel.btn(pyxel.KEY_D):
        king_x += 6
        stop_fall = True
    if pyxel.btn(pyxel.KEY_T):
        level += 1
    if pyxel.btn(pyxel.KEY_G):
        level -= 1
        
    if (pyxel.btn(pyxel.KEY_SPACE) or king_y > 260) and level == 1 :       
        king_x = 220
        king_y = 252
    
       
    return king_x, king_y, level, stop_fall


    
def floor(platforms):    
    for i in range(len(platforms)):
        if (king_x >= platforms[i].x-2 and king_x <= (platforms[i].x+2 + platforms[i].length) and (king_y == platforms[i].y-3)):
            return True
   
    else:
        return False
    

def end(platforms, destroy):
    if (king_x >= plfinal.x-2 and king_x <= (plfinal.x+2 + plfinal.length) and (king_y == plfinal.y-3)) and level == 5:
        destroy = "On"
    return platforms, destroy


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
    global king_x, king_y, right_memory, left_memory, fall, stop_fall, stop_jump, platforms, level, destroy
    
    king_x, king_y, platforms, stop_fall = platform_move(king_x, king_y, platforms, stop_fall)
    
    stop_fall = floor(platforms)
    
        
    king_x, king_y, level, stop_fall = reset(king_x, king_y, level, stop_fall)
    king_x, king_y, level, platforms = change_level(king_x, king_y, level, platforms)
    platforms, level, destroy = all_levels(platforms, level, destroy)
    
    
    right_memory, left_memory, fall, stop_fall = press(right_memory, left_memory, fall, stop_fall)
    king_x, king_y, right_memory, left_memory, fall, stop_fall, stop_jump, platforms = jump(king_x, king_y, right_memory, left_memory, fall, stop_fall, stop_jump, platforms)
    
    platforms, destroy = end(platforms, destroy)
   
def draw():
    pyxel.cls(0)
    
    
    if level >= 4:
        pyxel.rect(0, 0, 256, 258, 1)
    else:
        pyxel.rect(0, 0, 256, 258, 5)
        
    
    
    
    
    pyxel.rect(king_x, king_y, 3, 3, 7)    
    
    if pyxel.btn(pyxel.KEY_SPACE) or (king_x < -10 or king_x >266 or king_y > 260):
        pyxel.rect(0, 0, 256, 257, 0)
        
    
    if (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_LEFT)) and stop_fall == True:
        pyxel.rect(king_x, king_y, 3, 3, 0)
    
    
    
    
    
    
    
    #platforms
    
        
    for i in range(len(platforms)):
        if platforms[i].color <= 13:
            if (pyxel.frame_count % 1) == 0 :
                pyxel.rect(platforms[i].x, platforms[i].y, platforms[i].length, 3, platforms[i].color)
                
                
        if platforms[i].color == 14:
            if (pyxel.frame_count % 20) == 0 :
                pyxel.rect(platforms[i].x, platforms[i].y, platforms[i].length, 3, 7)
            else:
                pyxel.rect(platforms[i].x, platforms[i].y, platforms[i].length, 3, 0)
        
        
        
        
        if platforms[i].color == 15:
            if (pyxel.frame_count % 15) == 0 :
                pyxel.rect(platforms[i].x, platforms[i].y, platforms[i].length, 3, 0)
            else:
                pyxel.rect(platforms[i].x, platforms[i].y, platforms[i].length, 3, 7)                
                
                        
             
     
     
    if level == 1 and destroy == "On":
        pyxel.text(90,120, "Thank for playing !" , 6)
        
        
     
    
          
    if left_memory == 0:
        pyxel.text(26,12.5, str(left_memory), 13)
    elif left_memory < 15:
        pyxel.text(26,12.5, str(left_memory), 10)
    else:
        pyxel.text(26,12.5, str(left_memory), 8)
        
    if right_memory == 0:
        pyxel.text(230,12.5, str(right_memory), 13)
    elif right_memory < 15:
        pyxel.text(230,12.5, str(right_memory), 10)
    else:
        pyxel.text(230,12.5, str(right_memory), 8)
    
    
    color = [11,3,10,2,8,  0,0,0,0,0,0,0,0]
    if level != 1 or destroy != "On":
        pyxel.text(2.5,126.5, 'level' ,color[level-1])
        pyxel.text(24.5,126.5, str(level) ,color[level-1])
        
    
pyxel.run(update, draw)

    
    

    