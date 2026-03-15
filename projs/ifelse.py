#Fel.1 - Változó típusok
num = 2
word = "cat"
logical = False

#Fel.2 - if else
if num:
    print("Ez egy szam")
if word:
    print("Ez egy szöveg")
if logical: #Ilyenkor mindig igaz értéket vizsgálunk
    print("Ez igaz értéken van")
else:
    print("Ez hamis értéken van")

#Fel.3 - if else és operátorok
num1 = 8
num2 = 23
if num1 > num2:
    print("Az első szám nagyobb")
else:
    print("A második szám nagyobb")
    if num2 % 2 == 0: #Minden szám 2-vel osztva maradékosan( % ) és megeggyezik 0-val akkor az páros
        print("Ez a szám páros")
    else:
        num2 = num2 + 1
        print(f"{num2-1} + 1 = {num2}")
        if num2 % 2 == 0:
            print("Mostmár páros")

#Fel.4 - elif | ==
number1 = int(input("Adjon meg számot: "))
number2 = int(input("Adjon meg még egy számot: "))
if number1 == number2: #Ha a kettő szám megeggyezik
    print("A két szám egyenlő")
elif number1 > number2:
    print("Az első szám a nagyobb")
else:
    print("A második szám a nagyobb")

if number1 <= 10:
    print("Az első szám 11-nél kevesebb")
else:
    print("Az első szám 10-nél több")

#Fel.5 - Osztályozó rendszer
name = input("Adja meg a tanuló nevét: ")
point = int(input("Adja meg a " + name + " pontját: "))
if point >= 90:
    print(name + " jegye  ötös")
elif point >= 80:
    print(name + " jegye négyes")
elif point >= 60:
    print(name + " jegye hármas")
elif point >= 40:
    print(name + " jegye kettes")
else:
    print(name + " jegye egyes")

#Fel.6 - Önálló gyakorlás
#Feladat:
# - bekérünk egy nevet
# - bekérjük a megadott név korát
# - Ha 18 vagy feletti a kor akkor írja ki, hogy nev felnőttkorú
# - Ha 18 alatti a kor akkor írja ki, hogy nev fiatalkorú
person_name = input("Adja meg a személy nevét: ")
person_age = int(input("Adja meg " + person_name + " korát: "))
if person_age >= 18:
    print(person_name + " felnőttkorú")
else:
    print(person_name + " kiskorú")