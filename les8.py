'''

sex= input("geslacht m/f")
run=int(input("aantal km rennen"))
swim=int(input("aantal km zwemmen"))
bike=int(input("aantal km fietsen"))

if (sex=="m" and run>15 and swim>3 and bike>40) or (sex=="f" and run>12 and swim>2 and bike>30):
    print("je bent toegelaten!")
else:
    print("helaas, train nog even verder")


sex= input("geslacht m/f/x")
run=int(input("aantal km rennen"))
swim=float(input("aantal km zwemmen"))
bike=int(input("aantal km fietsen"))

#if sex=="x":
#    sex="f"

if (sex=="m" and run>14 and swim>2 and bike>39) or ((sex=="f" or sex=="x") and run>11 and swim>1 and bike>29):
    gevorderd=1
else:
    gevorderd =0
if (gevorderd==1 and sex=="m" and run>19 and swim>4 and bike>79) or (gevorderd==1 and (sex=="f" or sex=="x") and run>14 and swim>3.4 and bike>69) :
    print("je bent toegelaten bij de experten!")
elif (gevorderd==1 and sex=="m" and run<20 and swim<5 and bike<80) or (gevorderd==1 and (sex=="f" or sex=="x") and run<15 and swim<3.5 and bike<70) :
    print("je bent toegelaten bij de gevorderden!")
elif gevorderd==0 and (sex=="m" or sex=="f" or sex=="x"):
    print("helaas, train nog even verder")
else:
    print("begin opnieuw aub")
'''

#deze voert maar 2x uit?
aantal=int(input("hoeveel personen"))

def magikdoor(aantal):
    for i in range (1,(aantal+1)):
        sex = input("geslacht m/f")
        run = int(input("aantal km rennen"))
        swim = int(input("aantal km zwemmen"))
        bike = int(input("aantal km fietsen"))

        if (sex == "m" and run > 15 and swim > 3 and bike > 40) or (sex == "f" and run > 12 and swim > 2 and bike > 30):
            print("je bent toegelaten!")
        else:
            print("helaas, train nog even verder")

magikdoor(aantal)
