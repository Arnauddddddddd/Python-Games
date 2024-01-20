import pyxel, random

pyxel.init(128, 128, title = "La nuit du c0de")

lutin_x = 60
lutin_y = 60
vie = 10
score = 0

invisibility = False
reverse = False
speed = 2.5
type = ['Soin', 'Venemeux', 'Point','Vitesse','Mort','Invisible']
liste_champi = []

def deplacement_lutin(x, y, reverse, speed):
    
    
    if pyxel.btn(pyxel.KEY_DOWN):
        if y < 119:
            y += speed
    if pyxel.btn(pyxel.KEY_UP):
        if y > 0:
            y -= speed
    if pyxel.btn(pyxel.KEY_RIGHT):
        if x < 119: 
            x += speed
    if pyxel.btn(pyxel.KEY_LEFT):
        if x > 0:
            x -= speed
            
        
    return x, y



def aleatoire_champi(liste_champi, score):
    if score <= 50:
        return random.choice(['Point','Soin'])
    elif score <= 100:
        return random.choice(['Point','Soin','Venemeux'])
    elif score <= 150:
        return random.choice(['Point','Soin','Venemeux', 'Invisible'])
    elif score <= 250:
        return random.choice(['Point','Mort','Mort','Venemeux', 'Invisible'])
    
    else:
        return random.choice(['Point','Mort','Mort','Mort','Mort','Mort','Soin','Venemeux', 'Invisible'])
    

def creation_champi(liste_champi):
    if (pyxel.frame_count % 10 == 0):
        liste_champi.append([random.randint(0, 127), random.randint(0,35), aleatoire_champi(liste_champi, score)])
    
    return liste_champi


def deplacement_champi(liste_champi, score):
    for champi in liste_champi:
        champi[1] += 0.80
        if score >= 50:
            for champi in liste_champi:
               champi[1] += 0.15
        
    if (pyxel.frame_count % 25 == 0):
        for champi in liste_champi:
             champi[0] += 0
    return liste_champi, score

def suppression_champi(vie, score, speed, invisibility):
    for champi in liste_champi:
        if (abs(champi[0] - lutin_x) < 8 and abs(champi[1] - lutin_y) < 8) and (abs((champi[0]-6) - lutin_x) < 8 and abs((champi[1]-6) - lutin_y) < 8):
            liste_champi.remove(champi)
            if champi[2] == 'Soin' and vie < 10:
                    vie = 1 + vie
            elif champi[2] == 'Venemeux':
                    vie = vie - 5  
            elif champi[2] == 'Point':
                    score = score + 5
            elif champi[2] == 'Vitesse':
                    speed = speed + 0.2
            elif champi[2] == 'Mort':
                    vie = 0
            elif champi[2] == 'Invisible' and invisibility == True:
                invisibility = False
            elif champi[2] == 'Invisible' and invisibility == False:
                invisibility = True
              
            
               
            
        if champi[1] > 128:
            liste_champi.remove(champi)
    return vie, score, speed, invisibility
    



def update():
    
    global lutin_x, lutin_y, reverse, speed, liste_champi, champi, vie, score, invisibility
    liste_champi = creation_champi(liste_champi)
    liste_champi, score = deplacement_champi(liste_champi, score)
    lutin_x, lutin_y = deplacement_lutin(lutin_x, lutin_y, reverse, speed)
    vie, score, speed, invisibility = suppression_champi(vie, score, speed, invisibility)

def draw():
    pyxel.cls(0)
    pyxel.rect(0,0,128,128,1)
    pyxel.rect(lutin_x, lutin_y, 8, 8, 7)
    
    if invisibility == True:
        pyxel.rect(lutin_x, lutin_y, 8, 8, 1)
        
    if vie > 0 :
        pyxel.text(5,12.5, 'VIES:' + str(vie), 13)
        pyxel.text(5,5,'SCORE:' + str(score) ,13)
        pyxel.text(75,5,'OBJECTIF:500' ,1)
    else:
        
        pyxel.rect(0,0,128,128,0)
        pyxel.text(50,64, 'GAME OVER', 7)
        
    for champi in liste_champi:
        if champi[2] == 'Soin':
            pyxel.rect(champi[0], champi[1] ,2,2,11)
        elif champi[2] == 'Venemeux':
            pyxel.rect(champi[0], champi[1] ,2,2,8)
        elif champi[2] == 'Point':
            pyxel.rect(champi[0], champi[1] ,2,2,10)
        elif champi[2] == 'Vitesse':
            pyxel.rect(champi[0], champi[1] ,2,2,13)
        elif champi[2] == 'Mort':
            pyxel.rect(champi[0], champi[1] ,2,2,0)
        elif champi[2] == 'Invisible':
            pyxel.rect(champi[0], champi[1] ,2,2,14)
          
        
            
                      
        
            
pyxel.run(update, draw)
    
            
    
    

