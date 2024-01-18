'''
Created on 24.06.2020

@author: Robin
'''
from random import randint
import sys


    
spielfeld = [[0 for x in range(10)]for y in range(10)]  # Das Feld auf dem der Spieler seine Schiffe setzt/hat
spielfeldki2 = [[0 for x in range(10)]for y in range(10)]  # Das Feld auf dem der Spieler seine Schüsse sieht
spielfeldki = [
        #    0. 1. 2. 3. 4. 5, 6, 7, 8 ,9
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Das verdeckte Feld auf dem die Ki Schiffe fest gesetzt sind
            [0, 0, 0, 0, 4, 4, 4, 4, 0, 0], #1,4 1,5 1,6 1,7
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 3, 3, 3, 0, 0], #4,5 4,6 4,7
            [0, 0, 2, 2, 0, 0, 0, 0, 0, 0], #5,2 5,3
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 5, 5, 5, 5, 5, 0], #7,0 7,4 7,5 7,6 7,7 7,8
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def ausgabe_spielfeld(spielfeld): # ausgabe des Spielfeldes
    for x in range(len(spielfeld)):
        for y in range(len(spielfeld)):
            print(spielfeld[x][y], end=' ')
        print()

        
def ausgabe_spielki2(spielfeldki2): # ausgabe des anderen Spielfeldes
    for x in range(len(spielfeldki2)):
        for y in range(len(spielfeldki2)):
            print(spielfeldki2[x][y], end=' ')
        print()  

              
def random_reihe(spielfeld): #erstellt einen random wert 
    return randint(0, len(spielfeld) - 1)  

 
def random_spalte(spielfeld): #erstellt einen random wert
    return randint(0, len(spielfeld) - 1)


def schiffe_setzen(spielfeld): # mit dieser Fuktion werden die schiffe gesetzt
    ausgabe_spielfeld(spielfeld)
    print("Bitte setze deine Schiffe, dein Schiff steht von deinem Startpunkt immer nach rechts ! ")

    a = int(input("Schlachtschiff reihe: "))
    b = int(input("Schlachtschiff spalte: "))
    spielfeld[a][b] = 5
    spielfeld[a][b + 1] = 5 #Es wird die Anzahl der Elemente im Array geändert, die die länge des Schiffes beträgt. so werden die Schiffe in form von zahlen eintragen.
    spielfeld[a][b + 2] = 5 #so werden die Schiffe in form von Zahlen eintragen.
    spielfeld[a][b + 2] = 5
    spielfeld[a][b + 3] = 5
    spielfeld[a][b + 4] = 5
    ausgabe_spielfeld(spielfeld)
    
    c = int(input("Kreuzer reihe: "))
    d = int(input("Kreuzer spalte: "))
    spielfeld[c][d] = 4
    spielfeld[c][d+1] = 4
    spielfeld[c][d+2] = 4
    spielfeld[c][d+3] = 4
    ausgabe_spielfeld(spielfeld)
    
    e = int(input("Zerstörer reihe: "))
    f = int(input("Zerstörer spalte: "))
    spielfeld[e][f] = 3
    spielfeld[e][f+1] = 3
    spielfeld[e][f+2] = 3
    ausgabe_spielfeld(spielfeld)
    
    g = int(input("U-Boot reihe: "))
    h = int(input("U-Boot spalte: "))
    spielfeld[g][h] = 2
    spielfeld[g][h+1] = 2
    ausgabe_spielfeld(spielfeld)
    
    i = int(input("Nussschale reihe: "))
    j = int(input("Nusschale spalte: "))
    spielfeld[i][j]= 1
    ausgabe_spielfeld(spielfeld)
    x = input("Um zu beginnen: S Um aufzuhören: beliebige eingabe") # der Spieler kann entscheiden ob ihm seine Schiffe so passen und wenn nicht das Spiel beenden
    if x == "S":
        mensch_zug()
    else:
        sys.exit("Schade")

    
    
    
def mensch_zug():  #diese Funktion frägt den Spieler welche Spalte und Reihe er beschießen möchte und gibt diese Werte,
        ausgabe_spielki2(spielfeldki2)# falls diese korrekt sind weiter an die Mechanik funktion
        print("Du bist an der Reihe!")      
        tip_spalte = int(input("Schuss auf Spalte: "))
        tip_reihe = int(input("Schuss auf Reihe: "))
        if tip_reihe >= len(spielfeldki2) or tip_spalte >= len(spielfeldki2):
            print("Das ist nicht auf dem Spielfeld")
            mensch_zug()
        mechanik_spieler(tip_reihe, tip_spalte)

        
def Ki_zug(): #Das selbe wie bei Mensch zug nur umgedreht
        tip_spalte = random_spalte(spielfeld)
        tip_reihe = random_reihe(spielfeld)
        if tip_reihe > len(spielfeldki2) or tip_spalte > len(spielfeldki2):
            Ki_zug()
        mechanik_ki(tip_reihe, tip_spalte)

schiffki_a = 5
schiffki_b = 4
schiffki_c = 3
schiffki_d = 2
schiffki_e = 1

   
def mechanik_spieler(tip_reihe, tip_spalte): #Das kernstück des Spiels in der abgefragt wird welche schiffe getroffen wurden oder ob nichts getroffen wurde.
    global schiffki_a# globale Variablen damit sie sich nicht immer wieder zurücksetzen
    global schiffki_b
    global schiffki_c
    global schiffki_d
    global schiffki_e
    print("Dein Feld")
    
    if (spielfeldki[tip_reihe][tip_spalte]==5):
        spielfeldki2[tip_reihe][tip_spalte] = "T"  # T für Treffer 
        ausgabe_spielki2(spielfeldki2)
        print("gegnerisches Schlachtschiff getroffen")
        schiffki_a -= 1
        if schiffki_a == 0: # wenn das Schiff den wert 0 hat gilt es als versenkt
            print("gegnerisches Schlachtschiff versenkt")
            schiffki_a = 9 # damit sich die ausgabe "versenkt" nicht wiederholt

        
    elif (spielfeldki[tip_reihe][tip_spalte] == 4):
        spielfeldki2[tip_reihe][tip_spalte] = "T"  
        ausgabe_spielki2(spielfeldki2)
        print("gegnerischen Kreuzer getroffen")
        schiffki_b -= 1
        if schiffki_b == 0:
            print("gegnerischen Kreuzer versenkt")
            schiffki_b = 9
 
              
    elif (spielfeldki[tip_reihe][tip_spalte]==3):
        spielfeldki2[tip_reihe][tip_spalte] = "T" 
        ausgabe_spielki2(spielfeldki2)
        print("gegnerischer Zerstörer getroffen")
        schiffki_c -= 1
        if schiffki_c == 0:
            print("gegnerischen Zerstörer versenkt")
            schiffki_c = 9
 
    elif (spielfeldki[tip_reihe][tip_spalte]==2):
        spielfeldki2[tip_reihe][tip_spalte] = "T"  
        ausgabe_spielki2(spielfeldki2)
        print("gegnerisches U-Boot getroffen")
        schiffki_d -= 1
        if schiffki_d == 0:
            print("gegnerisches U-Boot zerstört")
            schiffki_d = 9
          
    elif (spielfeldki[tip_reihe][tip_spalte]==1):
        spielfeldki2[tip_reihe][tip_spalte] = "T"  
        ausgabe_spielki2(spielfeldki2)
        print("gegnerische Nussschale getroffen")
        schiffki_e -= 1
        if schiffki_e == 0:
            print("gegnerische Nussschale versenkt")
            schiffki_e = 9
        
    
    else: 
        if (spielfeldki[tip_reihe][tip_spalte]==0): # Es wird überprüft ob ein Feld mit dem Wert 0 getroffen wurde, falls ja ist die Ki am Zug
            print("Kein Schiff getroffen")
            spielfeldki2[tip_reihe][tip_spalte] = "X" # wasser treffer werden mit "X" markiert.
            ausgabe_spielki2(spielfeldki2)
            Ki_zug()   
    if(schiffki_a== 9 and schiffki_b ==9 and schiffki_c==9 and schiffki_d==9 and schiffki_e==9): # haben alle Schiffe den wert "9" gilt das SPiel als gewonnen
        ausgabe_spielfeld(spielfeldki)
        print("Wir konnten diese Schlacht für uns entscheiden GG")
    else:
        mensch_zug()
        
    



schiff_a = 5
schiff_b = 4
schiff_c = 3
schiff_d = 2
schiff_e = 1
def mechanik_ki(tip_reihe, tip_spalte): #Im Prinzip die selben Funktionen wie bei mechanik_mensch nur eben umgekehrt.
    global schiff_a
    global schiff_b
    global schiff_c
    global schiff_d
    global schiff_e

    print("Dein Feld")
    
    if (spielfeld[tip_reihe][tip_spalte]==5):
        spielfeld[tip_reihe][tip_spalte] = "T" 
        ausgabe_spielfeld(spielfeld)
        print("Unser Schlachtschiff wurde getroffen")
        schiff_a -= 1
        if schiff_a == 0:
            print("Unser Schlachtschiff wurde versenkt")
            schiff_a = 9
       
        
    elif (spielfeld[tip_reihe][tip_spalte]==4):
        spielfeld[tip_reihe][tip_spalte] = "T"
        ausgabe_spielfeld(spielfeld)
        print("Unser Kreuzer wurde getroffen")
        schiff_b -= 1
        if schiff_b == 0:
            print("Unser Kreuzer wurde versenkt")
            schiff_b = 9 
        Ki_zug()
          
    elif (spielfeld[tip_reihe][tip_spalte]==3):
        spielfeld[tip_reihe][tip_spalte] = "T" 
        ausgabe_spielfeld(spielfeld)
        print("Unser Zerstörer wurde getroffen")
        schiff_c -= 1
        if schiff_c == 0:
            print("Unser Zerstörer wurde versenkt")
            schiff_c = 9
       
        
    elif (spielfeld[tip_reihe][tip_spalte]==2):
        spielfeld[tip_reihe][tip_spalte] = "T" 
        ausgabe_spielfeld(spielfeld)
        print("Unser U-Boot wurde getroffen")
        schiff_d = -1
        if schiff_d == 0:
            print("Unser U-Boot wurde zerstört")
            schiff_d = 9
        
   
    elif (spielfeld[tip_reihe][tip_spalte]==1):
        spielfeld[tip_reihe][tip_spalte] = "T" 
        ausgabe_spielfeld(spielfeld)
        print("Unsere Nussschale wurde getroffen")
        schiff_e = -1
        if schiff_e == 0:
            print("Unsere Nussschale wurde versenkt")
            schiff_e = 9

    elif (spielfeld[tip_reihe][tip_spalte]==0):
        spielfeld[tip_reihe][tip_spalte] = "X"
        ausgabe_spielfeld(spielfeld)
        print()
        mensch_zug()

    elif spielfeldki2[tip_reihe][tip_spalte] == "X":
        Ki_zug()

        
   
    if(schiff_a== 9 and schiff_b ==9 and schiff_c==9 and schiff_d==9 and schiff_e==9):
        print(ausgabe_spielfeld(spielfeldki))
        print("Diese Schlacht ist verloren, Rückzug!")
    else:
        Ki_zug()
        

schiffe_setzen(spielfeld) # Der start des Spiels indem die Funktion "setze" aufgerufen wird.
