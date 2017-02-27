#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Program "Co to za słowo?"
#  rozwijający umiejętność programowania w Pythonie
#
#  slowa_01.py
#



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
    slowa = pobierzSlowa()  # wczytanie listy słów z pliku
    pokazSlowa(slowa)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
