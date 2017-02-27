#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Program "Co to za słowo?"
#  rozwijający umiejętność programowania w Pythonie
#
#  slowa_04.py
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
        slowo = raw_input("Podaj słowo: ")
        slowa.append(slowo.lower().strip())

    return slowa


def pokazSlowa(dane):
    for s in dane:
        print s,
    print


def losujSlowo(slowa):
    """Funkcja losuje słowo z podanej listy."""
    i = randint(0, len(slowa) - 1)
    return slowa[i]


def main(args):
    slowa = wczytajDane()
    if not slowa:
        slowa = pobierzSlowa()  # pobranie listy słów od użytkownika
        zapiszDane(slowa, "slowa.txt")
    pokazSlowa(slowa)
    slowo = losujSlowo(slowa)  # losowanie słowa z listy
    slowa.remove(slowo)  # usunięcie wylosowanego słowa z listy
    pokazSlowa(slowa)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
