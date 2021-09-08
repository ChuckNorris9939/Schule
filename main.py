import sys
import random
import re


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


def format_roman(case, counter):
    ones = [ 'i', 'x', 'c', 'm' ]
    fives = [ 'v', 'l', 'd' ]
    label, index = '', 0
    # This will die of IndexError when counter is too big
    while counter > 0:
        counter, x = divmod(counter, 10)
        if x == 9:
            label = ones[ index ] + ones[ index + 1 ] + label
        elif x == 4:
            label = ones[ index ] + fives[ index ] + label
        else:
            if x >= 5:
                s = fives[ index ]
                x = x - 5
            else:
                s = ''
            s = s + ones[ index ] * x
            label = s + label
        index = index + 1
    if case == 'I':
        return label.upper()
    return label
    #
    # for i in range(20):
    #     print(format_roman("I", i))


def roemischeZahlen1():
    zahlen = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    userInput = "aaa"

    while len(userInput) <= 3:
        print("Bitte nur 3 Zahlen eingeben")
        break
    else:
        userInput = str(input("Gebe eine Römische zahl ein: "))
        pass

    for i in zahlen:
        print(i)


def roemischeZahlen2():
    # romZiff = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    # romWert = [1, 5, 10, 50, 100, 500, 1000]
    #
    # def rom_in_zahl(i):
    #     for j in range(0, len(romZiff)):
    #         if i == romZiff[j]:
    #             return romWert[j]
    #
    # while True:  # Endlosschleife
    #     i = input('Geben Sie eine roemische Ziffer ein: ')
    #
    #     if i not in romZiff:
    #         print('Das ist keine roemische Ziffer!')
    #     else:
    #         print('Der Dezimalwert der Eingabe ist:    ', rom_in_zahl(i))
    rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    while True:

        dec = input("Geben Sie eine roemische Ziffer ein: ")

        for i in dec:
            print(i)
            print(rom.get(i))

        if dec is None:
            print("Diese Zahl ist kein vorgeschriebener Wert! Abbruch Danke!")
            break
        print(f"Der Dezimalwert der Eingabe ist: {dec}")


def scream(input):
    print("UserInput=   ", input)
    print("Capitalized= ", input.upper())


def CollatzFolge():
    zahl = 0
    while True:
        try:
            userInput = int(input("Geben Sie eine Nummer ein "))
            zahl = collatz(userInput)
            break
        except ValueError:
            print("Bitte eine Zahl eingeben!")
            pass

    while True:
        ans = collatz(zahl)
        if zahl == 1:
            print("1. Ende")
            break
        else:
            print(zahl)
            zahl = ans
            continue


def collatz(number):
    if number % 2 == 0:
        #print("True")
        return number // 2
    else:
        #print("False")
        return number * 3 + 1


if __name__ == '__main__':
    CollatzFolge()
