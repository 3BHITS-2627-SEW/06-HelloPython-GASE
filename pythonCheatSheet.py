
#int eineZahl = 43;
eineVariable = 13
print("eineVariable:", eineVariable)
eineVariable = "blablabla"
print("eineVariable:", eineVariable)

# Typisierung in Python: Ducktyping

# Daher: bitte immer nach Moeglichkeit typisieren
eineZweitevariable : int = 14
print("eineZweiteVariable", eineZweitevariable ** 3)
eineZweitevariable = "Text"
# print("eineZweiteVariable", eineZweitevariable ** 3)


datenTyp = type(eineVariable)
print("DatenTyp von eineVariable:", datenTyp)
eineVariable = 13

datenTyp = type(eineVariable)
print("DatenTyp von eineVariable:", datenTyp)

# C: printf("Zahl: %i \n", eineVariable)

einText = f"Zahl lautet {eineVariable} \n und ist Cool!"
print("zahl lautet:", (eineVariable**2))
# Typ Umwandlung
# Type-Conversion
einString = str(eineVariable**2)# wandle zahl in text um
alternativText = "Zahl lautet "+einString+" \n und ist Cool!"
print(einText)
print("Alternativtext:", alternativText)

#int i = 0;
#printf("Bitte geben Sie eine Zahl ein: \n");
#scanf(&i);
eingeleseneZahl = int(input("Bitte geben Sie eine Zahl ein: \n"))
print("Zahl eingelesen vom Typ:", type(eingeleseneZahl))
