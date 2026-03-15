#Fel.1 - Változók
#Személy:
vez_nev = "Szabo"
ker_nev = "Mate"
kor = 8
nem = "férfi"
orsz = "Magyar"
suly =  72

print(vez_nev, ker_nev)
print("Életkora " + str(kor) + " éves") #Számot szöveghez ha + jel karakterrel fűzünk akkor hibát kapunk mert szöveget nem enged számhoz adni
                    #str(változó) szöveg karakterré alakítja a változó értékét (a gépnek)
print("Neme: " + nem) #Ide nem kell az str() mert ez alapból szöveg
print("Jelenlegi ország: ", orsz)
print("Testsúlya", suly) #Ilyenkor felsorolásnak veszi a progrm és nem ad hibát

tort = 42.2
print("TÖRT VÁLTOZÓ: ", tort)

#Fel.2 - Változó típusok
egesz = 20
nemEgesz = 22.2
szov = "banán"
log = True #A logikai értékeket pythonban True / False. c#-ban true / false
print(type(egesz))
print(type(nemEgesz))
print(type(szov))
print(type(log))

#Fel.3 - Típus konvertálás
eletkor = 33
print(float(eletkor))

kerulet = 23.8
print(int(kerulet)) #a flot azaz a lebegő pontos számnál lefel kerekítünk ha konvertáljuk egész számmá az értékét

munka = "oktató"
#print(int(munka)) #<- erre hibát fogunk kapni

#Fel.4 - Változó értéke szövegre válaszból
valasz = input("Mi legyen a változó értéke: ") #Válaszként kapott érték mindig stringként van eltárolva
print(valasz)
print(type(valasz))
#print(int(valasz) + 2)

#Fel.5 - int változó értéke string-ből
magas = int(input("Adja meg a magasságát: "))
print(magas)
print(type(magas))

#Extra.fel.1 - end=''
print("alma", end='') #end='' A sor lezárását adja meg
print("fa") #A print alapból új sorba tolja a következőt
print("asd")

print("asd2")
print('asd1')

#Fel.6 - változó kiírás szövegben
my_name = "Mate"
print("Az én nevem " + my_name, end=" ")
my_age = 20
print("Én " + str(my_age) + " éves vagyok.")

#Fel.7 - változó kiírás szövegben v2
print("Az én nevem %s" %my_name)
print("")
print("Az én nevem %s és %d éves vagyok" %(my_name, my_age))

#Fel.8 - Fogalmazás írás v1 VS v2
"""
thing1 = input("Adjon meg egy tárgyat: ")
thing2 = input("Adjon meg egy tárgyat: ")
adjective = input("Adjon meg egy melléknevet: ")
verb = input("Adjon meg egy igét: ")
place = input("Adjon meg egy helyet: ")
food = input("Adjon meg egy ételt: ")
person = input("Adjon meg egy személyt: ")

print(
%s parti volt %s-nél.
Nagyon %s éreztem magam.
Én %s-t és %s-t vittem ajándékba.
Levezetésként, hogy edolgozzuk az ételt a mozgás %s volt.
Aztán elmentem a %s-ba/be.
%(food, person, adjective, thing1, thing2, verb, place))

print("")

print(f{food} parti volt {person}-nél.
Nagyon {adjective} éreztem magam.
Én {thing1}-t és {thing2}-t vittem ajándékba.
Levezetésként, hogy edolgozzuk az ételt a mozgás {verb} volt.
Aztán elmentem a {place}-ba/be.)
#Ahhoz hogy egy szövegben változót megjelenítsünk a "" jel elé egy f betűt teszünk
#Majd a változót {} közé írjuk
#pl.: print(f"asd {változó} asd")
#Ez a számot aumomatikusan str állapotban írja ki

"""

#Fel.9 - Változó típusok
num = 2
word = "cat"
logical = False

#Fel.5 - if else
if num:
    print("Ez egy szam")
if word:
    print("Ez egy szöveg")
if logical: #Ilyenkor mindig igaz értéket vizsgálunk
    print("Ez igaz értéken van")
else:
    print("Ez hamis értéken van")

#Fel.6 - if else és operátorok
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

#Fel.7 - elif | ==
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

#Fel.8 - Osztályozó rendszer
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

#Fel.9 - Önálló gyakorlás
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