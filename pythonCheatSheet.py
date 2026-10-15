
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
