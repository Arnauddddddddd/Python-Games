import pyxel
from random import randint

def collision(p1_x, p1_y, p1_longueur, p1_hauteur, p2_x, p2_y, p2_longueur, p2_hauteur):
    '''
entrée:
coordonnées et tailles de deux zones
sortie:
True si les eux zones se touchent
    '''
    if p1_x < p2_x + p2_longueur and p1_x + p1_longueur > p2_x and p1_y < p2_y + p2_hauteur and p1_y + p1_hauteur > p2_y:
        return True
    return False

class Plateforme:
    #objets plateforme
    def __init__(self, x, y, longueur, hauteur, couleur, couleur_bordure, deplacement):
        self.x = x
        self.y = y
        self.longueur = longueur
        self.hauteur = hauteur
        self.couleur = couleur
        self.couleur_bordure = couleur_bordure
        self.deplacement = deplacement
            
    
    def mouvement(self):
        #déplace la palteforme
        self.x += self.deplacement[0]
        self.y += self.deplacement[1]
        
    
    def teleportation(self, x, y):
        #place a des coordonnées (x,y) la plateforme
        self.x = x
        self.y = y



class Projectile:
    def __init__(self, x, y, couleur, mouvement, taille=[2,2]):
        self.x = x
        self.y = y
        self.longueur = taille[0]
        self.hauteur = taille[1]
        self.couleur = couleur
        self.mouvement = mouvement
        
    def deplace(self):
        self.x += self.mouvement[0]
        self.y += self.mouvement[1]
        
    def affiche(self):
        #affiche le projectile
        pyxel.rect(self.x, self.y, self.longueur, self.hauteur, self.couleur)


class Jeu:
    #objet du jeu
    def __init__(self, niveau=None):
        #initialisation des variables du joueur
       self.perso_x = 30
       self.perso_y = 30
       self.perso_anim = 0
       self.perso_dg = 1
       
       self.tomber = True
       self.memoire_saut = 0
       
       #initialisation listes
       self.plateformes = []
       self.liste_explosions = []
       self.liste_projectiles = []
       self.type_projectiles = []
       
       #initialisation quelques variables
       self.chrono = 0
       self.game_over = 0
       
       #initialisations des variables spécifiques au niveau
       self.niveau = niveau
       self.clefs = [k for k in niveau.keys()]
       for p in self.niveau['init']['plateformes']:
           self.plateformes.append(Plateforme(p[0], p[1], p[2], p[3], p[4], p[5], p[6]))
       self.perso_x = self.niveau['init']['perso'][0]
       self.perso_y = self.niveau['init']['perso'][1]
       self.temps = int(self.clefs[-1]) // 3
       self.couleur_fond = self.niveau['init']['fond']
        
       
       
    def saut(self):
        #gère la physique du perso
        for plat in self.plateformes:
            if self.perso_x + 7 > plat.x and self.perso_x < plat.x + plat.longueur and self.perso_y == plat.y - 8:
                self.tomber = False
                if pyxel.btn(pyxel.KEY_SPACE):
                    self.memoire_saut = 10
                    
        if self.tomber == True and self.memoire_saut == 0:
            self.perso_y += 2
                     
        if self.memoire_saut > 0 and self.tomber == False:
            self.perso_y -= 2
            self.memoire_saut -= 1               
        else:
            self.tomber = True
            
    def animation_perso(self):
        #gère vitesse animation perso
        if pyxel.frame_count % 25 == 0:
            self.perso_anim += 1
            if self.perso_anim >= 2:
                self.perso_anim = 0
            
        
    def deplacement_perso(self):
        #déplace le personnage
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.perso_x += 2
            self.perso_dg = 1
        if pyxel.btn(pyxel.KEY_LEFT):
            self.perso_x -= 2
            self.perso_dg = 0
            
    def evenement(self):
        #lance les divers évènements du niveau par rapport au chrono
        if str(self.chrono) in self.clefs:
            e = self.niveau[str(self.chrono)]
            if e[-1]:
                for i in range(len(e)-1):
                    #conditions action...
                    if e[i][0] == 'd':
                        self.plateformes[e[i][1]].deplacement = e[i][2]
                    elif e[i][0] == 't':
                        self.plateformes[e[i][1]].x = e[i][2]
                        self.plateformes[e[i][1]].y = e[i][3]
                    elif e[i][0] == 'c':
                        self.plateformes[e[i][1]].couleur = e[i][2]
                    elif e[i][0] == 'tpc':
                        self.type_projectiles.append(e[i][1])
                    elif e[i][0] == 'tpf':
                        self.type_projectiles.remove(e[i][1])
                    elif e[i][0] == 'fin':
                        self.game_over = 2 #2 -> victoire
                    e[-1] = False #on met False pour que l'évènement ne se répète pas
            
    
    def rafraichissement(self):
        #mise a jour du jeux
        self.deplacement_perso()
        self.saut()
        self.animation_perso()
        
        #gère vitesse jeux
        if pyxel.frame_count % 10 == 0:
            self.chrono += 1
        if pyxel.frame_count % 30 == 0:
            self.temps -= 1
        
        #lance les évènements du niveau
        self.evenement()
            
        #création projectiles
        if pyxel.frame_count % 2 == 0:
            for t in self.type_projectiles:
                self.liste_projectiles.append(Projectile(randint(t[0], t[1]), randint(t[2], t[3]), t[4], t[5], t[6]))
        for p in self.liste_projectiles:
            p.deplace()
        for plat in self.plateformes:
            plat.mouvement()

        #collisions projectiles
        for project in self.liste_projectiles:
            for plat in self.plateformes:
                if collision(plat.x, plat.y, plat.longueur, plat.hauteur, project.x, project.y, project.longueur, project.hauteur):
                    self.liste_projectiles.remove(project)
                    self.liste_explosions.append([project.x, project.y, 0, 3, 8])
            if project.x < -50 or project.x > 160 or project.y < -50 or project.y > 160:
                self.liste_projectiles.remove(project)
            if collision(self.perso_x, self.perso_y, 8, 5, project.x, project.y, project.longueur, project.hauteur):
                self.game_over = 1
                if project in self.liste_projectiles:
                    self.liste_projectiles.remove(project)
        if self.perso_y >= 129:
            self.game_over = 1
            
        #animation explosions
        if pyxel.frame_count % 10:
            for exp in self.liste_explosions:
                exp[2] += 1
                if exp[2] > exp[3]:
                    self.liste_explosions.remove(exp)
        
        
    def affiche(self):
        #affiche les éléments de l'écran du jeux
        #fond (dépend du niveau)
        pyxel.rect(0, 0, 128, 128, self.couleur_fond)
        #joueur
        if (self.memoire_saut > 0):
            pyxel.blt(self.perso_x, self.perso_y, 0, 40, 8 * self.perso_dg, 8, 8, 2)
        else:
            pyxel.blt(self.perso_x, self.perso_y, 0, 24 + 8 * self.perso_anim, 8 * self.perso_dg, 8, 8, 2)
        
        #platefromes
        for plat in self.plateformes:
            pyxel.rect(plat.x, plat.y, plat.longueur, plat.hauteur, plat.couleur_bordure)
            pyxel.rect(plat.x+1, plat.y+1, plat.longueur-2, plat.hauteur-2, plat.couleur)
        
        #projectiles
        for proj in self.liste_projectiles:
            proj.affiche()
        
        #explosions
        for exp in self.liste_explosions:
            pyxel.circb(exp[0], exp[1], exp[2], exp[4])
        
        #temps
        pyxel.rect(108, 8, 10, 10, 7)
        pyxel.text(110, 10, str(self.temps), 0)
        pyxel.rectb(107, 7, 12, 11, 0)
            



class Menu:
    def __init__(self):
        pyxel.init(128, 128)
        pyxel.load('2.pyxres')
        
        #liste niveaux réussis
        self.liste_reussi = []
        #gère l'état du jeux (menu, encours...)
        self.etat = 'menu'
        #liste des niveaux
        self.niveaux = [
            {'init' : {'perso' : [30, 30], 'fond' : 1, 'plateformes' : [[20, 80, 20, 3, 9, 13, [0, 0]], [85, 80, 20, 3, 9, 13, [0, 0]],
                                                            [53, 70, 20, 3, 9, 13, [0, 0]], [-60, 40, 30, 3, 11, 13, [0.5, 0]]]
            },
            '8' : [['tpc', [-49, 25, -1, 0, 8, [1, 1], [2, 2]]], True],
            '20' : [['tpf', [-49, 25, -1, 0, 8, [1, 1], [2, 2]]], True],
            '45' : [['d', 3, [-3, 0]], True],
            '50' : [['d', 3, [0, 0]], True],
            '56' : [['tpc', [0, 128, -1, 0, 8, [0, 1.5], [2, 2]]], True],
            '65' : [['tpf', [0, 128, -1, 0, 8, [0, 1.5], [2, 2]]], True],
            '68' : [['d', 3, [0, -2]], True],
            '70' : [['t', 3, 48, 130], ['d', 3, [0, -2]], True],
            '72' : [['d', 3, [0, 0]], ['d', 2, [0, -1.5]], True],
            '75' : [['tpc', [0, 128, 128, 129, 8, [0, -1.5], [2, 2]]], True],
            '84' : [['tpf', [0, 128, 128, 129, 8, [0, -1.5], [2, 2]]], True],
            '96' : [['fin'], True]
            },
            
            {'init' : {'perso' : [30, 30], 'fond' : 1, 'plateformes' : [[20, 80, 20, 3, 9, 13, [0, 0]], [85, 80, 20, 3, 9, 13, [0, 0]],
                                                                [53, 70, 20, 3, 9, 13, [0, 0]], [-60, 40, 30, 3, 11, 13, [0, 0]]]
            },
             '5' : [['tpc', [0, 50, 0, 1, 8, [0, 1], [2, 2]]], ['tpc', [80, 128, 0, 1, 8, [0, 1], [2, 2]]], True],
             '15' : [['tpf', [0, 50, 0, 1, 8, [0, 1], [2, 2]]], ['tpf', [80, 128, 0, 1, 8, [0, 1], [2, 2]]], True],
             '25' : [['c', 2, 8], True],
             '30' : [['d', 2, [0, -2]], ['c', 1, 8], True],
             '35' : [['d', 1, [-1, 1]], True],
             '38' : [['d', 1, [0, 0]], ['c', 1, 9], ['tpc', [128, 129, 50, 100, 8, [-1, 0], [2, 2]]], True],
             '45' : [['tpf', [128, 129, 50, 100, 8, [-1, 0], [2, 2]]], True],
             '60' : [['t', 0, 53, 90], ['t', 2, 50, 70], ['d', 2, [0, 0]], ['c', 2, 9], True],
             '65' : [['c', 1, 8], True],
             '70' : [['c', 0, 8], ['t', 1, 129, 129], True],
             '75' : [['c', 2, 11], ['t', 0, 129, 129], True],
             '81' : [['fin'], True]
            },
            
            {'init' : {'perso' : [64, 4], 'fond' : 1, 'plateformes' : [
                                                            [20, 80, 20, 3, 1, 6, [0, 0]], [85,  80,  20, 3, 1, 6, [0, 0]],
                                                            [53, 20, 20, 3, 1, 6, [0, 0]], [53, 100, 20, 3, 1, 6, [0, 0]],
                                                            [20, 40, 20, 3, 1, 6, [0, 0]], [85,  40,  20, 3, 1, 6, [0, 0]],
                                                            [53, 60, 20, 3, 1, 6, [0, 0]], [3, 2, 4, 30, 1, 12, [0, 0]]
                                                            ]
            },
             
            '2' : [['tpc', [-5, 0, 0, 128, 8, [1, 0], [2, 2]]], True],
            '4' : [['d', 7, [0, 0.5]], True],
            '16' : [['d', 7, [0, -0.5]], True],
            '28' : [['d', 7, [0, 0.5]], True],
            '45' : [['tpf', [-5, 0, 0, 128, 8, [1, 0], [2, 2]]], True],
            '54' : [['t', 7, 120, -40], True],
            '59' : [['tpc', [128, 129, 0, 128, 8, [-1, 0], [2, 2]]], True],
            '80' : [['tpf', [128, 129, 0, 128, 8, [-1, 0], [2, 2]]], True],
            '90' : [['fin'], True]
            
            },
            
            {'init' : {'perso' : [30, 30], 'fond' : 1, 'plateformes' : [[20, 80, 20, 3, 11, 3 , [0, 0]],
                                                                        [100, 120, 20, 3, 11, 3, [0, 0]],
                                                                        [-30, 70, 20, 3, 9, 10, [0, 0]],
                                                                        [120, -40, 3, 30, 9, 13, [0, 0]],
                                                                        [-45, 100, 40, 3, 9, 10 , [0, 0]],
                                                                        [120, -30, 4, 30, 9, 10 , [0, 0]],
                                                                        [-35, 120, 30, 3, 12, 0, [0, 0]],
                                                                        ]
            },
             '3': [['d', 2, [1, 0]], True],
             '8' : [['tpc', [-2, 2, 0, 110, 8, [1, 0], [2, 2]]], True],
             '15' : [['tpf', [-2, 2, 0, 110, 8, [1, 0], [2, 2]]], True],
             '20' : [['d', 4, [1, 0]], True],
             '21' : [['d', 5, [0, 1]], True],
             '26' : [['tpc', [128, 130, 0, 130, 8, [-1, 0], [2, 2]]], True],
             '30' : [['tpf', [128, 130, 0, 130, 8, [-1, 0], [2, 2]]], True],
             '35' : [['d', 6, [1, 0]], True],
             '36' : [['tpc', [-2, 72, -1, 0, 8, [0, 1], [2, 2]]], True],
             '53' : [['tpf', [-2, 72, -1, 0, 8, [0, 1], [2, 2]]], True],   
             '72' : [['fin'], True]
            }
            ]
        
        #indique niveau sélectioné
        self.indexe = 0
        
        #il faut le niveau sélectionné en paramètre
        self.jeu = None
        
        pyxel.run(self.rafraichissement, self.affiche)
        
    def rafraichissement(self):
        if self.etat == 'menu':
            if pyxel.btnr(pyxel.KEY_SPACE): #lance le jeu
                self.etat = 'jeu'
                #initialise le jeux
                self.jeu = Jeu(self.niveaux[self.indexe])
            #déplace la sélection du niveau
            if pyxel.btnr(pyxel.KEY_UP):
                self.indexe -= 6
            elif pyxel.btnr(pyxel.KEY_DOWN):
                self.indexe += 6
            elif pyxel.btnr(pyxel.KEY_RIGHT):
                self.indexe += 1
            elif pyxel.btnr(pyxel.KEY_LEFT):
                self.indexe -= 1
            #vérification d'être bien sur la liste des niveaux
            if self.indexe >= len(self.niveaux):
                    self.indexe = len(self.niveaux) - 1
            elif self.indexe <= 0:
                self.indexe = 0

        if self.etat == 'jeu':
            #fait tourner le jeux
            self.jeu.rafraichissement()
            
            #vérifie conditions victoire/défaite
            if self.jeu.game_over == 2: #victoire
                self.etat = 'menu'
                pyxel.play(0, 0)
                for k in self.jeu.clefs:
                    if k != 'init': self.niveaux[self.indexe][k][-1] = True
                self.liste_reussi.append(self.indexe)
            elif self.jeu.game_over == 1: #défaite
                self.etat = 'menu'
                for k in self.jeu.clefs:
                    if k != 'init': self.niveaux[self.indexe][k][-1] = True
    
    def affiche(self):
        #affiche tout
        pyxel.cls(1)
        if self.etat == 'menu':
            pyxel.text(50, 20, "JUMPER!", 10)
            pyxel.blt(55, 30, 0, 24, 32, 16, 8, 2)
            pyxel.blt(59, 40, 0, 24, 24, 8, 8, 2)
            #affichage menu
            i = 0
            j = 0
            for n in self.niveaux:
                pyxel.rect(30 + 20 * i, 75 + 20 * j, 10, 10, 0)
                if self.indexe == self.niveaux.index(n):
                    pyxel.text(33 + 20 * i, 78 + 20 * j, str(self.niveaux.index(n) + 1), 11)
                else:
                    pyxel.text(33 + 20 * i, 78 + 20 * j, str(self.niveaux.index(n) + 1), 8)
                if self.niveaux.index(n) in self.liste_reussi:
                    pyxel.rectb(30 + 20 * i, 75 + 20 * j, 10, 10, 3)
                    pyxel.rectb(28 + 20 * i, 73 + 20 * j, 14, 14, 3)
                else:
                    pyxel.rectb(30 + 20 * i, 75 + 20 * j, 10, 10, 8)
                i += 1
                if i >= 6:
                    i = 0
                    j += 1
            pyxel.text(30, 100, 'appuyez sur espace', 7)
        if self.etat == 'jeu':
            #affichage jeux
            self.jeu.affiche()
        
Menu()