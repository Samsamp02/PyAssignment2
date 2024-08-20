#nom: Samuel Prevost
#numero d'etudiant: 300355439

#Q1: (float, float)->bool
'''check si il fait assez froid et que la glace est assez eppaise'''
def patinage(cm, temp):
    if (cm >= 30) and (temp <= -10):
       check = True
    else:
        check = False

    print(check)
    return check

patinage(30, -10)
patinage(25.4, -15)
patinage(33, -15)
patinage(33, -5)

#Q2: (float)->string
'''donne une note alphabetique a partir d'une note numerique'''
def alphaNote(note):
    if note >= 90:
        alpha = "A+"
    elif 85 <= note < 90:
        alpha = "A"
    elif 80 <= note < 85:
       alpha = "A-"
    elif 75 <= note < 80:
        alpha = "B+"
    elif 70 <= note < 75:
        alpha = "B"
    elif 65 <= note < 70:
        alpha = "C+"
    elif 60 <= note < 65:
        alpha = "C"
    elif 55 <= note < 60:
        alpha = "D+"
    elif 50 <= note < 55:
        alpha = "D"
    elif 40 <= note < 50:
        alpha = "E"
    elif 0 <= note < 40:
        alpha = "F"
    

    print(alpha)
    return alpha

alphaNote(100)
alphaNote(89)
alphaNote(56)
alphaNote(30)

#Q3: () ->None
'''donne une note alphabetique a partir d'une note numerique et verifie si la note est 
entre 0 et 100 et donne un resultat de passage/faillite'''
def alphaNoteVerif():
    check = False
    while(check == False):
        note = float(input("SVP entrez la note finale (de 0 a 100): "))
        if note <= 100 and note >= 0:
            check = True

    if 90 <= note <= 100:
        alpha = "A+"
    elif 85 <= note < 90:
        alpha = "A"
    elif 80 <= note < 85:
       alpha = "A-"
    elif 75 <= note < 80:
        alpha = "B+"
    elif 70 <= note < 75:
        alpha = "B"
    elif 65 <= note < 70:
        alpha = "C+"
    elif 60 <= note < 65:
        alpha = "C"
    elif 55 <= note < 60:
        alpha = "D+"
    elif 50 <= note < 55:
        alpha = "D"
    elif 40 <= note < 50:
        alpha = "E"
    elif 0 <= note < 40:
        alpha = "F"
    else:
        print("Erreur")  
        return

    print("La note alphabetique est: " + alpha)

    if note > 40:
        print("Reussi")
    else:
        print("Echoue")

    return

alphaNoteVerif()

#Q4 (int) -> none
'''affiche les deuxiemes valeurs (n exclus si paire), ensuite les valeurs de n a 1 (i exclus si paire)'''
def boucles(n): 
    ligne1=[]
    ligne2=[]
    for x in range(1, n+1, 2):
        ligne1.append(x)
    for x in range(n, 0, -2):
        ligne2.append(x)
    print(*ligne1)
    print(*ligne2)    
    return

boucles(13)
boucles(10)

#Q5 (int) -> bool 
'''trouve et imprime tous les facteurs de N'''
def facteursDeN(N):
    i=2
    facteurs = []
    while(i<N):
        if (N%i == 0) :
            facteurs.append(i)
        i += 1
    print("Les facteurs sont: ", *facteurs)  
    i = 0
    somme = 0
    while(i < len(facteurs)):
        somme += facteurs[i]
        i += 1
    print("La somme de ses facteurs est: ", somme)
    if somme<N:
        print(True)
        return True
    print(False)
    return False

facteursDeN(12)
facteursDeN(9)
facteursDeN(5)

#Q6 (int) -> bool
'''Trouve si un nombre est un carre parfait et imprime sa racine'''
import math
def carreParfait(x):
    racine = math.sqrt(x)
    if (x % racine) == 0:
        print(x, " est un carre parfait et sa racine carree est ", racine)
        print(True)
        return True
    print(x, " n'est pas un care parfait")
    print(False)
    return False  

carreParfait(16)
carreParfait(15)

#Q7 (int)->float
'''fait le calcul de ((-1)**n)/(2*n+1)'''
def maFun1(n):
    res = ((-1)**n)/(2*n+1)
    #print(res)
    return res

print(maFun1(0))
print(maFun1(1))
print(maFun1(10))
print(maFun1(2))

#Q8 (int)->float
'''utilise la fonction de Q7 pour calculer pi'''
def maFun1_bis(n):
    i=0
    total = 0
    while(i<=n):
        res = maFun1(i)
        total += res
        i += 1
    print(total*4)
    return total
maFun1_bis(10)
maFun1_bis(100)
maFun1_bis(1000)
maFun1_bis(10000)  