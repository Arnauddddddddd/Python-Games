numero = '    1      2      3      4      5      6      7      8      9      10'
L = [
    ['|     ','|     ','|     ','|     ','|     ','|     ','|     ','|     ','|     ','|     '],
    ['|     ','|     ','|     ','|     ','|     ','|     ','|     ','|     ','|     ','|     '],
    ['|     ','|     ','|     ','|     ','|     ','|     ','|     ','|     ','|     ','|     '],
    ['|     ','|     ','|     ','|     ','|     ','|     ','|     ','|     ','|     ','|     '],
    ['|     ','|     ','|     ','|     ','|     ','|     ','|     ','|     ','|     ','|     '],
    ['|     ','|     ','|     ','|     ','|     ','|     ','|     ','|     ','|     ','|     ']
    ]

fin = ['oui', 'non']
player1 = True
pion = 0
print(" Il faut jouer avec la police de console nommé 'OCR A Extended' \n ")

def afficher():
    for i in range(len(L)):
        print(L[i][0],L[i][1],L[i][2],L[i][3],L[i][4],L[i][5],L[i][6],L[i][7],L[i][8],L[i][9])
        print()
    return ''
    
    

def puissance4(player1, fin, pion):
    
    
    #vertical
    for i in range(len(L)):
        for j in range(len(L[0])-3):
            if (L[i][j] == pion) and (L[i][j+1] == pion) \
                and (L[i][j+2] == pion) and (L[i][j+3] == pion):
                    fin = 'oui'
                
    
    #horizontale
    for i in range(len(L)-3):
        for j in range(len(L[0])):
            if (L[i][j] == pion) and (L[i+1][j] == pion) \
                and (L[i+2][j] == pion) and (L[i+3][j] == pion):
                    fin = 'oui'
     
    
    for i in range(3, len(L)):
        for j in range(len(L[0])-3):
            if (L[i][j] == pion) and (L[i-1][j+1] == pion) \
                and (L[i-2][j+2] == pion) and (L[i-3][j+3] == pion):
                    fin = 'oui'
    
            
    for i in range(3, len(L)):
        for j in range(3, len(L[0])):
            if (L[i][j] == pion) and (L[i-1][j-1] == pion) \
                and (L[i-2][j-2] == pion) and (L[i-3][j-3] == pion):
                    fin = 'oui'
    
    return fin



def jouer(player1, fin):
    pion = 0
    fin = 'non'
    if player1 == False:
        pion = '|   O '
        numero_joueur = 2
        adverse = '|   X '
        
    if player1 == True:
        pion = '|   X '
        numero_joueur = 1
        adverse = '|   O '

    a = int(input(f'Tour du joueur {numero_joueur}'))
    if a > len(L[0]) or a < 1:
        print('Vous ne pouvez pas utiliser cet emplacement')
        return jouer(player1, fin)
    j = 1
    ajout = True
    while ajout == True:
        if j > (len(L)):
            print('Vous ne pouvez pas jouer à cet emplacement')
            return jouer(player1, fin)
        if (L[-j][a-1] == '|     ' and (L[-j][a-1] != adverse)) and fin == 'non':
           L[-j][a-1] = pion
           ajout = False
           fin = puissance4(player1, fin, pion)
        j += 1 
    print(numero)
    print(afficher())
    if fin == 'non' :
        player1 = not(player1)
        return jouer(player1, fin)
    else:
        print('Victoire du joueur', numero_joueur)
    

print(numero)
afficher()    
jouer(player1, fin)
