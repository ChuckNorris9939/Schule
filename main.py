import sys
import random


def schaltjahr():
    jahr = int(input("Geben Sie ein Schaltjahr an: "))

    if jahr % 400 == 0:
        print("Es ist ein Schaltjahr")
    elif jahr % 100 == 0:
        print("Es ist kein Schaltjahr")
    elif jahr % 4 == 0:
        print("Es ist ein Schaltjahr")
    elif jahr == 0:
        sys.exit()
    else:
        print("Es ist kein Schaltjahr")

    schaltjahr()


def hundejahre():
    # Landläufig rechnet man Hundejahre in Menschenjahre um, indem man das Alter des Hundes mit 7 multipliziert. Je nach Hundegröße und Rasse sieht die Umrechnung jedoch etwas komplizierter aus, z.B.:
    # Ein einjähriger Hund entspricht in etwa einem 14-jährigen Menschen.
    # 2 Jahre eines Hundes entsprechen 22 Jahre eines Menschen.
    # Ab dann entspricht ein Hundejahr jeweils 5 Menschenjahren.

    jahr = int(input("Geben Sie ein Hundejahr an: "))

    ergebnis = ""
    if jahr == 1:
        ergebnis = 14
    elif jahr == 2:
        ergebnis = 22
    elif jahr == 3:
        ergebnis = jahr * 5

    print("Der Hund ist " + ergebnis + " Jahre als")

    hundejahre()


def forschleife():
    endzahl = int(input("Geben Sie Ein Zahl zwischen 1 - 100 "))

    summe = 0
    for i in range(1, endzahl):
        summe = summe + i
        print("summe:" + str(summe) + "i:" + str(i))
    print(summe)

    forschleife()


def mrandom():
    randomNumber = random.randint(1, 20)

    userInput = int(input("Rate die Nummer zwischen 1 und 20: "))
    versuche = 5
    while True:
        if versuche == 0:
            print("Du hast keine Versuche mehr!")
            break
        else:
            if userInput != randomNumber:
                print("Falsch!. Nocheinmal")
                userInput = int(input("Noch einmal! Du hast noch " + str(versuche) + " Versuche "))
                versuche = versuche - 1
                pass
            else:
                print("Richtig")
                break


def mrandom2():
    randomNumber = random.randint(1, 20)
    print(randomNumber)

    userInput = int(input("Rate die Nummer zwischen 1 und 20: "))
    versuche = 5
    while versuche != 0:
        if userInput != randomNumber:
            print("Falsch!. Nocheinmal")
            userInput = int(input("Noch einmal! Du hast noch " + str(versuche) + " Versuche "))
            versuche = versuche - 1
            pass
        else:
            print("Richtig")
            break
    print("Du hast keine Versuche mehr!")


## Aufgabe 3
def matheaufgaben():
    versuche = 5
    fehler = 0
    while versuche != 0:
        rnr1 = random.randint(1, 10)
        rnr2 = random.randint(1, 10)
        ergebnis = rnr1 + rnr2
        while True:
            try:
                userInput = int(input("Was ist das Ergebnis von " + str(rnr1) + " + " + str(rnr2) + ": "))
                break
            except:
                print("Bitte eine Zahl eingeben!")
                pass
        if userInput == ergebnis:
            print("Antwort ist korrekt!")
            versuche = versuche - 1
            pass
        else:
            print(str(userInput) + "ist Falsch!")
            fehler = fehler + 1
    else:
        print("Du hast " + str(fehler) + " Fehler gemacht!")


if __name__ == '__main__':
    matheaufgaben()
