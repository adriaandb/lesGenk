#Maak een array met 100 veelvouden van 7
'''
tabel=[]
for i in range (1,101):
    tabel.append(i*7)
print(tabel)


tabel=[]
for i in range (1,101):
    tabel.append(i*7)
for j in range (0,len(tabel)):
    print(tabel[j])



even=[]
oneven=[]
for i in range (1,11):
    getal = int(input("geef een getal in"))
    if(getal%2 ==0):
        even.append(getal)
    else :
        oneven.append(getal)
print(even)
print(oneven)



#Maak een array waarin elke letter van een ingegeven woord wordt opgeslagen


woord = input("geef een woord in")
lijstTeken=[]

print(woord)



#Maak een functie 3e macht die de 3e macht van een ingegeven getal terug geeft

def derdemacht(getal):
    print(getal**3)

derdemacht(7)


#Maak een functie euroDollar die euro omzet naar dollar met 2 cijfers achter de komma

def euroDollar(x):
    print(round(x*1.16,2))

euroDollar(37)



#hoger lager
import random
for i in range(1,10):
    getal1=random.randint(1, 12)
        if print(i) = print(i-1):
            print(random.randint(1,12))
    print(getal1)

'''
import random

def HogerLager(x):
    score = 0
    while score < x and not score == -1:
        i = random.randint(1, 12)
        j = random.randint(1, 12)
        if i == j:
            j = random.randint(1, 12)
        print(i)
        #print(j)

        Antw = input("hoger of lager")
        if i > j:
            if Antw == "lager":
                score = score + 1
                print("juist!, het getal was",j,", je score is ",score)
            elif Antw == "hoger":
                score = score -1
                print("fout!,het getal was",j,", je score is ", score)
        elif i < j:
            if Antw == "hoger":
                score = score + 1
                print("juist!,het getal was",j,", je score is ",score)
            elif Antw == "lager":
                score = score - 1
                print("fout!,het getal was",j,", je score is ", score)
        else:
            print("vul het woord 'hoger' of 'lager in.")

    if score>=x:
       # score = score-1
        print("Je wint!: je eindscore is ",score)
    elif score == -1 :
        print("GAME OVER")

HogerLager(3)


