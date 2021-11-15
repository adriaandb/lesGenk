"""
naam='Adriaan De Belder'
print(naam[5:13])


naam='Adriaan De Belder'
print(naam[-3:3])


#afkorting naam
voornaam="Adriaan"
naam='De Belder'
print(voornaam[0:2]+naam[0:2])


#afronden na komma
import math
euro= float(input("geef het aantal euro in"))
print(euro," euro is ", round(euro*1.30,2), "dollar")



#lengte 2 stukken tekst
voornaam="Adriaan"
naam='De Belder'
print(len(voornaam)+len(naam))


#deelbaar door2?
getal = float(input("geef het getal in"))
rest = getal%2
print("de rest na deling door 2 is ",rest)


#deelbaar door2?
getal = float(input("geef het getal in"))
rest = getal%2
if rest>0 :
#if getal%2 == 0 :
    print("nee")
else:
    print("ja")

#hoeveel betaal je voor samson
age= int(input("hoe oud ben je?"))
if age<18 :
    print("je betaalt 10 euro")
else :
    print("je betaalt 15 euro")



#aanspreken naar geslacht
geslacht = input("geef geslacht")
if(geslacht == "vrouw"):
    print("dag mevrouw")
elif(geslacht == "man"):
    print("dag meneer")
else:
    print("dag beste")

"""

#dollar of pond conv
amount = float(input("geef het te converteren bedrag in"))
val = input("typ e voor euro, d voor dollar")
if val=="e" :
    print(amount, "dollar is ", amount*0.87 , "euro.")
if val == "d":
    print(amount, "euro is ", amount*1.17 , "dollar.")

"""

#BMI feedback
lengte =  float(input("geef je lengte in (in meter)"))
gewicht = float(input("geef je gewicht in (in kg)"))
bmi=gewicht/(lengte*lengte)
if bmi<18.5 :
    print("je BMI valt onder 'ondergewicht'.")
if 18.5<bmi<25 :
    print("je BMI valt onder 'gezond gewicht'.")
if 25<bmi<30 :
    print("je BMI valt onder 'overgewicht'.")
if 30 < bmi :
    print("je BMI valt onder 'obesitas'.")



# kostprijs vervoer
import math
km = float(input("geef het aantal km in"))
if km<25 :
    print("de kostprijs is", km*0.25)
else :
    print("de kostprijs is ", 6.25+((km-25)*0.15))


km = float(input("geef het aantal km in"))
if (km<25) :
    prijs= km*0.25
else :
    prijs = 6.25+((km-25)*0.15)

print("de kostprijs is ", prijs)

getal = round(random.uniform(1,10),2)


#211004

#willekeurige getallen optellen
import random
print(random.randint(100,200)+random.randint(100,200))


#even getal tss 10 en 30
import random
getal = random.randint(10,30)
even = getal/2
if even%2 == 0 :
    print(even)
else :
    print("niet even helaas")


import random
print(random.randint(5,15)*2)


#deelbaar door 2 en 3
import random
getal = random.randint(0,100)
if (getal%2 == 0 and getal%3 == 0) :
    print(getal,"is wel deelbaar door 2 en 3")
else :
    print(getal, "is niet deelbaar door 2 en 3")

import random
getal = random.randint(0,100)
if (getal%6 == 0) :
    print(getal,"is wel deelbaar door 2 en 3")
else :
    print(getal, "is niet deelbaar door 2 en 3")

#Neem grootste getal van 3 willekeurige getallen tussen 1 en 1000

import random
a = random.randint(1,1000)
b = random.randint(1,1000)
c = random.randint(1,1000)
print ( a, b, c)
if a>b>c :
    print(a)
elif b>a>c :
    print(b)
else :
    print(c)



#CASUS1 de verver

#even getallen tot 256
getal = 0

while (getal<256) :
    getal = getal+2
    print(getal)



#Schrijf een programma dat het dubbel van een ingegeven getal geeft tot 1000.

getal = 1

while getal<500 :
    getal=getal*2
    print(getal)


#Schrijf een programma dat het gemiddelde geeft van alle ingevoerde getallen ,
# de invoer stopt bij stop, pas invoercontrole toe.



invoer = ""
teller = -1
som = 0

while (not invoer == "stop") :
    invoer=input()
    teller=teller+1

    try:
        invoer=int(invoer)
        som = (som) + invoer
    except:
        print("geef een getal of stop in")

print("het gemiddelde is: ",som/teller)

# 211011 loops

#tafel tot 100

getal= int(input("geef een getal in om te vermenigvuldigen"))
for i in range(1,101):
    print(getal, "x", i,"is", getal*i)

import math
for i in range(1,11):
    print(2**i)



#som 5 ingegeven getallen

for i in range(1,6):
    getal= int(input())
    som= som + getal
print(som)

teller=0
while(teller<5):
    getal=
    som=
    teller=
print(som)

#het grootste ingegeven getal van 10 getallen

grootste=0
for i in range(1,11):
    getal=int(input())
    if(getal>grootste):
        grootste=getal
print(grootste)


getal=int(input())
kleinste=getal
for i in range(1,10):
    getal=int(input())
    if(getal<kleinste):
        kleinste=getal
print(kleinste)



#alle vermenigvuldigingen van een ingegeven getal geeft dat kleiner is dan 1000
getal=int(input())
teller=1
maal=0
while maal < 1000:
    maal=getal*teller
    teller=teller+1
    if maal<1000:
        print(maal)

#Pas het programma aan dat je een eindgetal ingeeft.
#Geef een melding als het eindpunt kleiner is dan het vermenigvuldig getal

getal=int(input("getal="))
eind=int(input("max="))
teller=1
maal=0

if(eind>getal):
    while maal < eind:
        maal=getal*teller

        teller=teller+1
        if maal<eind:
            print(maal)
else:
    print("geef een grotere max in")


#Schrijf een programma dat je naam spelt.

naam= str(input("geef je naam in"))
for i in range(0,len(naam)):
    print(naam[i:i+1])

naam= str(input("geef je naam in"))
for i in range(len(naam),0,-1):
    print(naam[i-1:i])

#Schrijf een programma dat een tafelkaart maakt van alle tafelen tot 20 en 20 keer
for i in range (1,21): #rijen
    for j in range(1,21): #kolommen
        print(i*j,end="\t")
    print("")

from datetime import date

f_date = date(2021, 10, 11)
l_date = date(2021, 12, 25)
delta = l_date - f_date
print(delta.days)


# import the time module
import time

# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')


# input time in seconds
t = int(input("Enter the time in seconds: "))
countdown(t)


# function call
countdown(int(t))


import time

def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        time.sleep(1)
        print(min_sec_format, end=' ')

        num_of_secs -= 1

    print('Countdown finished.')


inp = input('Input number of seconds to countdown: ')
countdown(inp)



#if (antwoord=="parijs"):

"""
