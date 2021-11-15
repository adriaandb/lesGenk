'''
#cinema
xPers=int(input("met hoeveel personen ga je kijken"))
pPrijs=0
tPrijs=0

for i in range(0,xPers):
    naam = str(input("wat is je naam?"))
    vraag= "Hoe oud is" ,naam, "?"
    age = int(input(vraag))
    if age<12 : pPrijs=4
    elif age<18 and age>12 : pPrijs=5
    else: pPrijs=6
    lang = input("is het een lange film? j/n")
    if lang == "j": pPrijs=pPrijs+2
    else: pPrijs=pPrijs
    drieD = input("is het een 3D film? j/n")
    if drieD == "j": pPrijs = pPrijs + 2
    korting = input("heb je een kortingkaart? j/n")
    if korting == "j" and age<25: pPrijs = pPrijs - 2
    tPrijs=tPrijs+pPrijs
    print(naam, "betaalt :", pPrijs, "euro.")
    #print("persoon", i + 1, "betaalt :", pPrijs, "euro.")
print("De totaalprijs is ",tPrijs,".")



aantalPersonen=int(input("met hoeveel personen ga je kijken?"))
totaalPrijs=0

for i in range(0,aantalPersonen):
    leeftijd = int(input("geef je leeftijd in"))
    #hier wordt de prijs per leeftijd berekend
    if leeftijd < 13:prijsPersoon=4
    elif leeftijd < 19:prijsPersoon=5
    else: prijsPersoon = 6
    #hier komt de extrakost
    isDrieD = input("is het een 3D film. j/n")
    isLangeFilm = input("is het een lange film. j/n")
    if isDrieD == "j" : prijsPersoon = prijsPersoon+2
    if isLangeFilm == "j":prijsPersoon = prijsPersoon+2
    student = input("heb je een studentenkaart. j/n ")
    if student == "j" and leeftijd < 26:prijsPersoon=prijsPersoon-2

    totaalPrijs = totaalPrijs+prijsPersoon
    print("persoon",i+1,"betaalt :",prijsPersoon, "euro.")
print("de totaal prijs is:",totaalPrijs)


# CASUS2
import math
opp = float(input("wat is de oppervalkte die moet worden aangelegd?"))
klinkerAfmeting= str(input("wat is de afmeting van de klinker?"))
if klinkerAfmeting == "10x10":
    klinkerPrijs = 14
elif klinkerAfmeting == "12x12":
    klinkerPrijs = 16
elif klinkerAfmeting == "14x14":
    klinkerPrijs = 16.5
print("klinkerprijs per m²:",klinkerPrijs)

verwijderen = input("moeten oude klinkers worden verwijderd? (j/n)")
if verwijderen == "j":
    werkuren = math.ceil(opp/12) + math.ceil(opp/15)
else :
    werkuren= math.ceil(opp/12)
print("werkuren:",werkuren)

afstand=2*float(input("wat is de afstand naar plaats van de job (in km)?"))

def totPrijsVervoer(afstand):
    if afstand > 10:
        totPrijs=5+((afstand-10)*0.3)
    else:
        totPrijs=5
    return(totPrijs)
totPrijsVervoer(afstand)

totaalprijs= (werkuren*40) + totPrijsVervoer(afstand) + (klinkerPrijs*opp)
#
print("Het totale bedrag van de werken bedraagt",totaalprijs,"euro.")
'''

#schilder

prijsVerf=15
prijsArbeid=35

def opp():
    muren = int(input("hoeveel muren van 50m2"))
    opp= muren*50
    return(opp)

def totPrijsVerf():
    totPrijsVerf=float(opp*(prijsVerf/22)*2)
    return(totPrijsVerf)

def totPrijsArbeid():
    totPrijsArbeid=float(opp/18*prijsArbeid)
    return(totPrijsArbeid)

print(totPrijsVerf()+totPrijsArbeid())
