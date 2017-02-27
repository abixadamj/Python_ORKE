#!/usr/bin/env python
# -*- coding: utf-8 -*-

teraz = 2016  # aktualny rok
rok_pythona = 1991  # rok powstania Pythona

imie = raw_input("Twoje imię? ")
if len(imie) == 0 or not imie.isalpha():
    print "Cześć nieznajomy(a)! Jestem Python!"
    imie = "nieznajomy"
elif imie[0].islower():
    imie = imie[0].upper() + imie[1:]  # notacja wycinkowa

wiek = raw_input("Ile masz lat? ")
if wiek.isdigit() and int(wiek) >= 18 and int(wiek) < 80:
    rok_urodzenia = teraz - int(wiek)
else:
    print "Błędny wiek"
    rok_urodzenia = teraz

wiek_pythona = teraz - rok_pythona

print "Cześć", imie, "Jestem Python!"
print "Urodziłeś się w %s roku!" % rok_urodzenia
print "Powstałem w %s roku i mam %s lat," % (rok_pythona, wiek_pythona)

if wiek_pythona > int(wiek):  # instrukcja warunkowa
    print "Jestem starszy!"
elif wiek_pythona == int(wiek):
    print "Mamy tyle samo lat!"
else:
    print "Jestem młodszy"
