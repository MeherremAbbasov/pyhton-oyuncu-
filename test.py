class Futbolcu():
    qacis = "Qaca Bilir"
    qabaqda = "Herzaman Qabaqda olurda"
    maasi = 5000

class Basketbolcu():
    turnik = "Turnik Edir"
    ucur = "Uca bilir"
    maasi = 4000

class Multiidmanci(Basketbolcu,Futbolcu):
    pass

Resad = Multiidmanci()

print(Resad.turnik)
print(Resad.qacis)
print(Resad.maasi)

