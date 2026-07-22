import random, os, time

def clearmat(A,n):
   # setze (n+2)x(n+2)-Feld A zurueck auf 0
   for i in range(n+2):
      for j in range(n+2):
         A[i][j]=0
         
def initmat(A,n):
   # initialisiere Inneres des (n+2)x(n+2)- Feldes A
   # zufaellig mit 0 oder 1
   for i in range(1,n+1):
      for j in range(1,n+1):
         A[i][j]=random.randint(0,1)
         
def printmat(A,n):
   # drucke Inneres des (n+2)x(n+2)-Feldes A, so dass  0 --> "." und 1 --> "X"
   for i in range(1,n+1):
      for j in range(1,n+1):
         if A[i][j]==0:
            print (".",end="")
         else:
            print ("X",end="")
      print()
   print()


def evalmat(A,B,n):
   # Berechne Anzahl der lebenden Nachbarzellen von A in allen
   # inneren Zellen und speichere Info in B
   for i in range(1,n+1):
      for j in range(1,n+1):
         B[i][j] = -A[i][j]
         for k in range(i-1,i+2):
            for l in range(j-1,j+2):
               B[i][j]=B[i][j]+A[k][l]

def newgen(A,B,n):
   # Zu Beginn des Programms enthaelt Feld B fuer jede Zelle die Anzahl
   # der lebenden Nachbarzellen und Feld A die aktuelle Info ueber lebende
   # und tote Zellen.
   # Das UP newgen bestimmt aus daraus eine neue
   # Zellgeneration und speichert sie im Feld A
   for i in range(1,n+1):
      for j in range(1,n+1):
         if A[i][j]==0:
            if B[i][j]==3:
            # tote Zellen erwachen zum Leben
               A[i][j]=1
         else:
            if B[i][j]<2 or B[i][j]>3:
            # lebende Zellen sterben
               A[i][j]=0
      
def comp_nl(A,n):
   # berechne Anzahl lebender Zellen
   nl = 0
   for i in range(1,n+1):
      for j in range(1,n+1):
         nl=nl+A[i][j]
   return nl

# Python-Programm zur Simulation von Conway's "Spiel des Lebens"
n=eval(input("Anzahl der Zellen in jeder Richtung: "))
ngen = eval(input("Anzahl der Generationen: "))
# Anlegen der Felder A und B
A=list(range(n+2))
B=list(range(n+2))
for i in range(n+2):
   A[i]=list(range(n+2))
   B[i]=list(range(n+2))
# jetzt gibt es alle A[i][j] und B[i][j] mit 0<=i<=n+1 und 0<=j<=n+1
# Initialisieren von Feld A  mit 0
clearmat(A,n)

# Besetze A am Anfang zufaellig mit lebenden und toten Zellen
initmat(A,n)

os.system("clear")
printmat(A,n)
for it in range(1,ngen+1):
   # setze B auf 0
   clearmat(B,n)
   # berechne Anzahl der lebenden Nachbarzellen und speichere Info in B
   evalmat(A,B,n)
   # berechne neue Generation
   newgen(A,B,n)
   # loesche Bildschirm
   os.system("clear")
   print()
   # drucke neue Generation
   printmat(A,n)
   # berechne Anzahl lebender Zellen
   nleben=comp_nl(A,n)
   print ("Anzahl lebender Zellen: ",nleben)
   # verzoegere Programm
   time.sleep(.3)
input("zum Beenden des Programms bitte Eingabe-Taste druecken")


      
