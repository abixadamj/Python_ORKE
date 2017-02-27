#!/usr/bin/env python
# -*- coding: utf-8 -*-

teraz = 2016  # aktualny rok
rok_pythona = 1991  # rok powstania Pythona

imie = raw_input("Twoje imię? ")
wiek = raw_input("Ile masz lat? ")

rok_urodzenia = teraz - int(wiek)  # konwersja na int
wiek_pythona = teraz - rok_pythona

print "Cześć", imie, "Jestem Python!"
print "Urodziłeś się w %s roku!" % rok_urodzenia
print "Powstałem w %s roku i mam %s lat," % (rok_pythona, wiek_pythona)

if wiek_pythona > int(wiek):  # instrukcja warunkowa
    print "Jestem starszy!"
else:
    print "Jestem młodszy"
