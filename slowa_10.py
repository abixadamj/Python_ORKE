#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Program "Co to za słowo?"
#  rozwijający umiejętność programowania w Pythonie
#
#  slowa_09.py
#


import json
import os
from random import randint


def wczytajDane():
    """Funkcja wczytuje listę w formacie json z podanego pliku"""
    dane = []
    nazwa = raw_input("Podaj nazwę pliku lub naciśnij ENTER dla nowej listy: ")
    if os.path.isfile(nazwa):
        plik = open(nazwa, "r")
        dane = json.load(plik)
    elif nazwa:
        print "Plik nie istnieje."

    return dane


def zapiszDane(dane, plik):
    """Funkcja zapisuje podaną listę w podanym pliku w formacie json"""
    plik = open(plik, "w")
    json.dump(dane, plik)
    plik.close()


def pobierzSlowa():
    """Funkcja pobiera kolejne słowa i dodaje do listy"""
    slowa = []  # pusta lista
    ile = int(raw_input("Ile słów podasz? "))
    for i in range(ile):
        slowo = ""
        while not slowo.isalpha() and slowo not in slowa:
            slowo = raw_input("Podaj słowo: ").decode("utf-8")
        slowa.append(slowo.lower().strip())
        print slowa

    return slowa


def pokazSlowa(dane):
    for s in dane:
        print s,
    print


def losujSlowo(slowa):
    """Funkcja losuje słowo z podanej listy."""
    i = randint(0, len(slowa) - 1)
    return slowa[i]


def wezWyraz(slowo, ilepustych):
    """Funkcja zwraca wyraz z zadaną ilością pustych miejsc."""
    indeksy = []  # lista losowanych indeksów
    while True:
        indeks = randint(0, len(slowo) - 1)
        if indeks not in indeksy:
            indeksy.append(indeks)
            ilepustych -= 1
            if ilepustych == 0:
                break
    odgadnij = []
    for i in range(len(slowo)):
        if i in indeksy:
            odgadnij.append("_")
        else:
            odgadnij.append(slowo[i])
    return "".join(odgadnij)


def main(args):
    slowa = wczytajDane()
    if not slowa:
        slowa = pobierzSlowa()  # pobranie listy słów od użytkownika
        zapiszDane(slowa, "slowa.txt")
    pokazSlowa(slowa)

    punkty = 0
    for i in range(len(slowa)):
        slowo = losujSlowo(slowa)  # losowanie słowa z listy
        slowa.remove(slowo)  # usunięcie wylosowanego słowa z listy

        while True:
            ilepustych = raw_input("Ile liter odgadniesz (max %s)? " % len(slowo))
            if ilepustych.isdigit() and int(ilepustych) <= len(slowo):
                break
        odgadnij = wezWyraz(slowo, int(ilepustych))  # słowo do odgadnięcia
        print "Co to za słowo? ", odgadnij

        odp = raw_input("Twój typ: ")
        punkty += int(ilepustych)
        while odp.decode("utf-8").lower() != slowo:
            print "Nie zgadłeś!"
            odgadnij = wezWyraz(slowo, int(ilepustych))  # słowo do odgadnięcia
            print "Co to za słowo? ", odgadnij
            punkty -= 1
            while True:
                odp = raw_input("Twój typ: ")
                if odp.decode("utf-8").isalpha():
                    break
        print "Zgadłeś!"

        print "Punktów: %s" % punkty

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
