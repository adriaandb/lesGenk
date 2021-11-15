"""

#oef som van 2 getallen
getal1 = float(input("geef getal 1 in"))
getal2 = float(input("geef getal 2 in"))
som = getal1+getal2
print(som)


#oef1 euro naar dollar
euro = float(input("geef het bedrag in euro in"))
dollar = euro*1.17
print(euro, "euro is",dollar,"dollar")

#oef gemiddelde 4 getallen
print("gemiddelde 4 getallen")
getal1 = float(input("geef getal 1 in"))
getal2 = float(input("geef getal 2 in"))
getal3 = float(input("geef getal 3 in"))
getal4 = float(input("geef getal 4 in"))
gemiddelde = (getal1+getal2+getal3+getal4)/4
print("het gemiddelde is", gemiddelde)


#oef oppervlakte cirkel
straal = float(input("wat is de straal?"))
opp = 2*straal*3.14
print("de oppervlakte van de cirkel is",opp)


#oef zevende macht
import math
getal = float(input("geef het getal in"))
macht7 = math.pow(getal,7)
print("de zevende macht van", getal, "is ",macht7)

#oef 3e vierkantswortel
getal = float(input("geef het getal in"))
res = getal**(1/3)
print(res)

#oef 3e vierkantswortel
import math
getal = float(input("geef het getal in"))
res = math.pow(getal,(1/3))
print(res)


#oef 3e vierkantswortel
import math
getal = float(input("geef het getal in"))
res = pow(getal,(1/3))
print(res)

#oef macht tussen haakjes (a+b)^2
a = float(input("geef de waarde voor a in"))
b = float(input("geef de waarde voor b in"))
res= ((a*a)+2*a*b+(b*b))
print(res)



#oef remafstand /10 kwadr /2
speed = float(input("geef de snelheid in"))
dist = ((speed/10)*(speed/10)/2)
print("de remafstand bedraagt ",dist, "meter")



#oef remafstand /10 kwadr /2
speed = float(input("geef de snelheid in"))
dist = (((speed/10)**2)/2)
print("de remafstand bedraagt ",dist, "meter")


#oef remafstand /10 kwadr /2
import math
speed = float(input("geef de snelheid in :"))
dist = (pow((speed/10), 2)/2)
print("de remafstand bedraagt ",dist, "meter")

#oef graden n-hoek
n = int(input("geef het aantal hoeken"))
graden = (n-2)*180
print("een",n,"hoek is", graden, "graden" )

#oef BMI
gewicht = float(input("geef je gewicht in (in kg)"))
lengte =  float(input("geef je lengte in (in meter)"))
print("Je BMI-index is",gewicht/(lengte*lengte))


#oef afstand
v= float(input("geef je snelheid op (km/h)"))
t= float(input("geef je tijd in (in uren)"))
print("je afgelegde afstand is", v*t,"km")


#oef gewicht maan
gewicht= float(input("geef je gewicht op (in kg):"))
print("Je weegt op de maan",gewicht*0.165,"kg.")


#oef
l=float(input("lengte balk in m ="))
b=float(input("breedte balk in m ="))
h=float(input("hoogte balk in m="))
print("De balk vullen voor 70% kost je ",l*b*h*.7*.38,"Euro.")


#oef schuine zijde
r1= float(input("geef de lengte van rechte zijde 1 in:"))
r2= float(input("geef de lengte van rechte zijde 2 in:"))
print("de schuine zijde is",(r1**2+r2**2)**(1/2) ,"lang.")

#oef opp vijfhoek
a = float(input("Geef de Apothema in:"))
s = float(input("Geef de lengte van een zijde in:"))
print("De oppervlakte van de vijfhoek is ", (a*s*5)/2,".")

#oef opp vijfhoek
import math
r = float(input("Geef de straal van de uitgeschreven cirkel van de vijfhoek in:"))
print("De oppervlakte van de vijfhoek is ", 2.5*(r**2)*math.sin(72) )

#oef opp vijfhoek
import math
s = float(input("Geef de lengte van een zijde in:"))
print("De oppervlakte van de vijfhoek is ", (5*s*s)/(4*math.tan(36)),".")
"""

