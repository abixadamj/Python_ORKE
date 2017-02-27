#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Program "Co to za słowo?"
#  rozwijający umiejętność programowania w Pythonie
#
#  slowa_02.py
#


import json


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


def main(args):
    slowa = pobierzSlowa()  # pobranie listy słów od użytkownika
    zapiszDane(slowa, "slowa.txt")
    pokazSlowa(slowa)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
