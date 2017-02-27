#!/usr/bin/env python
# -*- coding: utf-8 -*-

def pobierzImie():
    """Funkcja pobera, sprawdza i zwraca imię użytkownika."""
    imie = raw_input("Twoje imię? ")
    if len(imie) == 0 or not imie.isalpha():
        print "Cześć nieznajomy(a)! Jestem Python!"
        imie = "nieznajomy"
    elif imie[0].islower():
        imie = imie[0].upper() + imie[1:]  # notacja wycinkowa
    return imie


def pobierzWiek(rok_teraz):
    """
    Funkcja pobiera i sprawdza wiek użytkownika oraz
    oblicza rok jego urodzenia. Zwraca wiek jako liczbę i rok urodzenia.
    @Parametry: rok_teraz – bieżący rok
    """
    wiek = raw_input("Ile masz lat? ")
    if wiek.isdigit() and int(wiek) >= 18 and int(wiek) < 80:
        rok_urodzenia = rok_teraz - int(wiek)
    else:
        print "Błędny wiek"
        rok_urodzenia = rok_teraz
    return int(wiek), rok_urodzenia


def pythonGada(imie, rok_urodzenia, rok_pythona, wiek_pythona, wiek):
    """Funkcja wyprowadza komunikaty w programie"""
    print "Cześć", imie, "Jestem Python!"
    print "Urodziłeś się w %s roku!" % rok_urodzenia
    print "Powstałem w %s roku i mam %s lat," % (rok_pythona, wiek_pythona)
    if wiek_pythona > wiek:  # instrukcja warunkowa, rzutowanie
        print "Jestem starszy!"
    elif wiek_pythona == wiek:
        print "Mamy tyle samo lat!"
    else:
        print "Jestem młodszy"


def kimJestes():
    """Rozmowa z Pythonem"""

    teraz = 2016  # aktualny rok
    rok_pythona = 1991  # rok powstania Pythona
    wiek_pythona = teraz - rok_pythona

    imie = pobierzImie()  # wywołanie funkcji
    wiek, rok_urodzenia = pobierzWiek(teraz)  # rozpakowanie wartości

    pythonGada(imie, rok_urodzenia, rok_pythona, wiek_pythona, wiek) # wywołanie funkcji


def main(args):
    kimJestes()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
