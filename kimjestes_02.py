#!/usr/bin/env python
# -*- coding: utf-8 -*-

imie = raw_input("Twoje imię? ")
print "Cześć", imie, "Jestem Python!"  
wiek = raw_input("Ile masz lat? ")
teraz = 2016
rok_urodzenia = teraz - int(wiek)  # konwersja na int
print "Urodziłeś się w %s roku!" % (rok_urodzenia)
rok_pythona = 1991
wiek_pythona = teraz - rok_pythona
print "Powstałem w %s roku i mam %s lat," % (rok_pythona, wiek_pythona)
