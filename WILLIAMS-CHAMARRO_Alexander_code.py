import numpy
import os
import time

clear=""
if os.name=='nt': #pour windows
    clear="cls"
else:   #pour mac et linux
    clear="clear"

dot="."
for i in range(20):
    print(dot)
    time.sleep(0.25)
    os.system(clear)
    dot+="."
os.system(clear)

print('Chargement terminé')
time.sleep(3)
os.system(clear)
time.sleep(2)
print('______ _____ _____ _   _ _   _ _____ _   _ _   _ _____ ')
time.sleep(0.5)
print('| ___ \_   _|  ___| \ | | | | |  ___| \ | | | | |  ___|')
time.sleep(0.5)     
print('| |_/ / | | | |__ |  \| | | | | |__ |  \| | | | | |__  ')
time.sleep(0.5)
print('| ___ \ | | |  __|| . ` | | | |  __|| . ` | | | |  __| ')
time.sleep(0.5)
print('| |_/ /_| |_| |___| |\  \ \_/ / |___| |\  | |_| | |___ ')
time.sleep(0.5)
print('\____/ \___/\____/\_| \_/\___/\____/\_| \_/\___/\____/ ')
time.sleep(5)
os.system(clear)
time.sleep(2)


grid=[]
ligne_actuelle=1
print("Veuillez introduire maintenant, ligne par ligne, un soduko de 9 colonnes et de 9 lignes\n\n")
time.sleep(1)
for i in range(9):
    print("Introduisez la ligne numéro",ligne_actuelle,"avec chaque valeur séparée par un espace\n")
    something=input("==>")
    ligne=list(map(int, something.split()))
    grid.append(ligne)
    ligne_actuelle+=1
    os.system(clear)

os.system(clear)
time.sleep(2)
print(numpy.matrix(grid))
time.sleep(2)

point=''
for i in range(4):
    point=''
    for i in range(4):
        print('En cours de résolution'+point)
        time.sleep(0.25)
        os.system(clear)
        time.sleep(0.25)
        point+='.'


def possible(row, column, number):
    global grid
    #verification dans la ligne
    for i in range(0,9):
        if grid[row][i] == number:
            return False

    #verification dans la colonne
    for i in range(0,9):
        if grid[i][column] == number:
            return False
    
    #verification dans le carré
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False

    return True

def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0
                #retour du sudoku résolu
                return
      
    #affichage du sudoku retourné 
    print(numpy.matrix(grid))


print('Voici le sudoku résolu :\n')

solve()