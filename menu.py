# -*- coding: utf-8 -*-
print "Pozdravljen v izdelovalcu menujev za restavracije"

cenik = {}
cenik_file = open("menu.txt", "w+")

while True:
    jed = raw_input("Prosim vnesi jed: ")
    cena = float(raw_input("Vpiši ceno jedi: "))
    cenik[jed] = round(cena, 1)
    print "Vnešena je jed: %s s ceno: %.1f €" % (jed,cena)
    nova_jed = raw_input("Bi rad vnesel še kakšno jed? (da/ne)")

    if nova_jed == "ne":
        break
print cenik
print "\nSeznam jedi: "
cenik_file.write("Končana opravila:\n")
for jed, cena in cenik.items():
    print "Jed: %s" %jed
    print "cena: %f" %cena
    cenik_file.write('- '+jed+' | cena: '+str(cena)+'€\n')
cenik_file.close()
print "\nKonec seznama"