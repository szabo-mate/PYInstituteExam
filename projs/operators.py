#Fel.1 - aritmetikai operátorok
print(5 + 5)
print(6 - 4)
print(10 * 2)
print(3 ** 2) #Négyzetre emelés
print(100 / 20)
print(100 // 33) #// osztás, itt az eredmény lefelé kerekítjük
print(9 % 2) #Maradékos osztás, itt az eredmény a maradék lesz
print("\n")

#Fel.2 - hozzárendelő operátorok
num = 8
print(num)
num += 7
print(num)
num -= 6
print(num)
num *= 5
print(num)
num /= 5
print(num)
num **= 2
print(num)
print("\n")

#Fel.3 - összehasonlító operátorok
print(5 < 4)
print(32 > 9)
print(9 * 5 == 45)
print(9 == 45)
print("\n")

#Fel.4 - Indentity operator
print( 5 is 5)
print(8 is 9)
print(6 is "alma")

x1 = 5
x2 = 5
x3 = 8
y1 = "alma"
y2 = "barack"
print(x1 is x2)
print(x1 is x3)
print(x1 is y1)
print(y1 is y1)
print(y1 is y2)
print("\n")

#Fel.5 - membership operator
z1 = 'a'
z2 = 'b'
z3 = 'world'
word = "Hello world"
print(z1 in word)
print(z2 in word)
print(z3 in word)
print("\n")

#Fel.6 - operátorok if-ben
a1 = 4
a2 = 7
if a1 > a2:
    print(str(a1) + " nagyobb mint " + str(a2))
else:
    print(f"{a1} kisebb mint {a2}")
#Mind2 kiírás helyes

if a1 ** a2 == a2**a1:
    print(f"Az {a1}^{a2} az ugyanaz mint a {a2}^{a1}")
if a1 ** a2 != a2**a1:
    print(f"Az {a1}^{a2} az nem ugyanaz mint a {a2}^{a1}")
print("\n")

#Fel.7 - email validálás
email = "myemail@gmail.com"
if "@" in email and (email.endswith(".com") or email.endswith(".hu")):
    print("Ez helyes emailcím")
else:
    print("Ez helytelen emailcím")

#Fel.8 - szám pozitív vagí negatív
number = float(input("Adjon meg bármilyen számot: "))
if number == 0:
    print("A szám nulla.")
elif number > 0:
    print("A szám pozitív")
else:
    print("A szám negatív")

print("\n")

#Fel.9 - Gondoltam egy állatra
animal_leg = int(input("2 vagy 4 lábú állat? "))
animal_fly = input("Tud e repülni? ")
animal_swim = input("Tud e úszni? ")
if animal_leg == 2:
    if animal_fly.lower == "igen":
        if animal_swim.lower() == "igen":
            print("Ez egy kacsa")
        else:
            print("Ez egy galamb")
    elif animal_fly.lower() == "nem":
        if animal_swim.lower() == "igen":
            print("Ez egy pingvin")
        else:
            print("Ez egy kiwi")
elif animal_leg == 4:
    if animal_fly.lower == "igen":
        if animal_swim.lower() == "igen":
            print("Ez egy pegazus (szárnyas unikornis)")
        else:
            print("Egy egy pillangó")
    elif animal_fly.lower() == "nem":
        if animal_swim.lower() == "igen":
            print("Ez egy ló")
        else:
            print("Ez egy teve")

#Fel.10 - Legnagyobb szám
a = int(input("Adja meg az első számot: "))
b = int(input("Adja meg a második számot: "))
c = int(input("Adja meg a harmadikat számot: "))
if a > b:
    if a > c:
        print(f"{a} a legnagyobb szám")
        if b > c:
            print(f"{b} a második legnagyobb")
            print(f"{c} a harmadik legnagyobb")
        else:
            print(f"{c} a második legnagyobb")
            print(f"{b} a harmadik legnagyobb")
    else:
        print(f"{c} a legnagyobb szám")
        print(f"{a} a második legnagyobb")
        print(f"{b} a harmadik legnagyobb")
elif b > c:
    print(f"{b} a legnagyobb szám")
    if a > c:
        print(f"{a} a második legnagyobb")
        print(f"{c} a harmadik legnagyobb")
    else:
        print(f"{c} a második legnagyobb")
        print(f"{a} a harmadik legnagyobb")
else:
    print(f"{c} a legnagyobb szám")
    print(f"{b} a második legnagyobb")
    print(f"{a} a harmadik legnagyobb")
