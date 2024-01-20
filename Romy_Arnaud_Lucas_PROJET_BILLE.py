from tkinter import *
from random import *


class Carré:
    '''
    création de de la classe "carré" qui permettra de faire disparaître les billes au contact des carrés
    '''
    def __init__(self, x, y, x_final, y_final, couleur, taille):
        self.x = x      
        self.y = y
        self.x_final = x_final
        self.y_final = y_final
        canvas.create_rectangle(x, y, x_final, y_final, fill=couleur, width=taille) #Crée les carrés des coins selon les coordonnées définies au dessus


tk = Tk() #Initialisation de la fenêtre
tk.geometry("900x500+10+10") #Crée la fenêtre ou se trouve le canevas selon les dimensiosn données
canvas = Canvas(tk, width=800, height=400, bg="beige") #Crée le canevas où les billes se déplacent selon les dimensions données
tk.title("Bille") #Titre de la fenêtre
canvas.pack() #Initialisation du canevas
billes = [] #Liste où sont stockées les valeurs des billes
bille_gagnante = [] # Liste vide, on y mettra la dernière bille encore présente sur la fenêtre

#création des carrés
carré1 = Carré(0, 0, 40, 40, "blue", 0) #Création du carré du coin haut gauche
carré2 = Carré(760, 0, 800, 40, "yellow", 0) #Création du carré du coin haut droit
carré3 = Carré(0, 360, 40, 400, "red", 0) #Création du carré du coin bas gauche
carré4 = Carré(760, 360, 800, 400, "green", 0) #Création du carré du coin bas droit


class Bille:
    '''
    création de la classe "Bille", pour que chaque bille ait une position, une vitesse et une couleur différente
    '''
    def __init__(self, x, y, x_final, y_final, couleur, speedx, speedy):
        self.speedx = speedx #Vitesse de la bille dans l'axe des abcisses
        self.speedy = speedy #Vitesse de la bille dans l'axe des ordonnées
        self.y = y 
        self.x = x 
        self.x_final = x_final 
        self.y_final = y_final 
        self.couleur = couleur #Couleur de la bille
        self.bille = canvas.create_oval(x, y, x_final, y_final, fill=couleur, outline = couleur) #Crée les billes rondes selon les coordonnées définies au dessus
        self.movement() #Permet au billes de se déplacer
        self.collision_carré() #Crée la collision entre les billes et les carrés aux coins
      

    def movement(self): #Crée le mouvement des billes
        '''
        fonction de la classe bille qui permet à chaque bille de se déplacer, elle permet également la collision avec les côtés
        de la fenêtre. 
        '''
        canvas.move(self.bille, self.speedx, self.speedy) #Fait se déplacer une bille à la vitesse donnée 
        if self in billes: #si la bille est présente:
            pos = canvas.coords(self.bille) #Crée une liste qui enregistre la position de la bille en temps réel
            self.x, self.y, self.x_final, self.y_final = pos[0], pos[1], pos[2], pos[3]
            #on modifie les coordonnés de la bille pour qu'elles soient correct
        
        if self.x_final >= 800 or self.x <= 0:
            self.speedx *= -1 #On multiplie la vitesse par -1 pour que la bille reparte en arrière lorqu'elle atteind les bords du canevas
        if self.y_final >= 400 or self.y <= 0:
            self.speedy *= -1 #Idem       
        
        tk.after(12, self.movement) #Actualisation de la fenêtre
        
        
    def collision_carré(self):
        '''
        la fonction permet de réaliser les événements lorsqu'une bille disparaît et lorsque la dernière bille disparaît
        '''
        if (
            ((self.x > carré1.x-15) and (self.y > carré1.y-15) and (self.x_final < carré1.x_final+15) and (self.y_final < carré1.y_final+15)) or
            ((self.x > carré2.x-15) and (self.y > carré2.y-15) and (self.x_final < carré2.x_final+15) and (self.y_final < carré2.y_final+15)) or
            ((self.x > carré3.x-15) and (self.y > carré3.y-15) and (self.x_final < carré3.x_final+15) and (self.y_final < carré3.y_final+15)) or
            ((self.x > carré4.x-15) and (self.y > carré4.y-15) and (self.x_final < carré4.x_final+15) and (self.y_final < carré4.y_final+15))
            ): #Vérifie si la bille est dans l'un des carrés            
            
            canvas.delete(self.bille) #Supprime la bille du canevas
            if len(billes) > 1:
                self.x, self.y = -100, -100 #La place en dehors du canevas
            billes.remove(self) #Supprime la bille de la classe Bille
            if len(billes) == 1: #si il n'y a plus qu'une bille:
                bille_gagnante.append(billes[0])  #alors elle sera la bille gagnante
            if len(billes) == 0: #si toutes les billes ont disparu, on affiche les informations de la bille gagnante
                print("la boule gagnante est:")
                print("couleur hex:", bille_gagnante[0].couleur) #Affiche la couleur en hexadécimal de la dernière bille
                c = rgb(bille_gagnante[0].couleur)
                print("couleur rgb: IntegerRGB(red =", str(c[0]), ",green =",  str(c[1]), ",blue =", str(c[-1]),")")              
                print("en position x:", int(bille_gagnante[0].x), "et y:", int(bille_gagnante[0].y)) #Affiche les coordonnées de la dernière bille
                tk.destroy() #ferme la fenêtre
                quit() #arrète le programme 
                
        tk.after(10, self.collision_carré) #Actualisation de la fenêtre
        



def billes_create(nbr):
    '''
    permet de créer un nombre définit de bille en leur donnant des coordonnés aléatoires, une couleur aléatoire, ainsi qu'une
    vitesse aléatoire. Elles sont crées puis ajouter à la liste "billes".
    '''
    for i in range(nbr):
        couleur = "#" + ''.join([choice('ABCDEF0123456789') for i in range(6)]) #Couleur aléatoire de la bille
        x2 = randint(100, 700) # Donne l'abscisse de la bille de façon aléatoire
        y2 = randint(50, 350) # Donne l'ordonnée de la bille de façon aléatoire
        vitesse_x = randint(-5,5) # Donne une vitesse dans l'axe des abscisses à la bille de façon aléatoire
        vitesse_y = randint(-5,5) # Donne une vitesse dans l'axe des ordonnées à la bille de façon aléatoire
        while vitesse_x == 0:
            vitesse_x = randint(-5,5) #Au cas où 0 est généré
        while vitesse_y == 0:
            vitesse_y = randint(-5,5)#Au cas où 0 est généré
        billes.append(Bille(x2, y2, x2 + 20, y2 + 20, couleur, vitesse_x, vitesse_y)) #Ajoute les valeurs de la bille à la liste Billes
    

def rgb(hexa):
    '''
    Entrée : une chaîne de caractère d'un code couleur en hexadécimal
    Traitement : conversion
    Sortie : un tuple d'un code couleur en rgb    
    '''
    hexa = hexa.lstrip('#')
    return tuple(int(hexa[i:i+2], 16) for i in (0,2,4))


billes_create(10) #Crée les billes 
tk.mainloop()
