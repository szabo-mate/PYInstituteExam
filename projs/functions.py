#Függvények
def nev(parameter):      #def függvényneve(paramétere)
    print(parameter)

nev("MATE")             #Meghíváskor a függvény neve(esetleges paraméter ha van)

def iras():
    print("Hello World")
iras()

#Fel.2 - prímszám function
def primeNumber():
    number = int(input("Adjon meg egy számot: "))
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    if prime:
        print("A ", number, "Egy prímszám")
    else:
        print("A ", number, "Nem egy prímszám")
primeNumber()

#Fel.3 - prímszám function paraméterrel

number = int(input("Adjon meg egy számot: "))
def primeNumPar(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    if prime:
        print("A ", num, " egy prímszám")
    else:
        print("A ", num, " nem egy prímszám")

primeNumPar(number)
primeNumPar(12)


#Fel.4 - parameter
def parameter(par):
    print(par)

parameter("Hello World")
parameter(3 + 4)

#Fel.5 - 3szög-e?
def triangle(a, b, c):
    if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
        print("Ez egy 3szög")
    else:
        print("Ez nem egy 3szög")
triangle(3, 4, 5)#<- Ez egy 3szög
triangle(3, 4, 6)#<- Ez nem egy 3szög

#Fel.6, 7 - return magyarázat
def funcX():
    x = 10
    print(x)

x = 20
print(x)#<- x = 20
funcX() #<- x = 10
print(x)#<- x = 20

def func_return(p):
    if p >= 0:  #Ha a p értéke nagyobb vagy megegyezik 0-val akkor megkapjuk a p értékét
        return p
    else:
        return -p #Ellenkező esetben a p értékét - értékké alakítjuk és adjuk vissza
                    #Minden minusz szám pozitív les mert minusz * minusz = plusz
print(func_return(6))
print(func_return(-5))

#Fel.8 - fuggvény lezárás return-el
def exitFunc():
    for i in range(1, 10):
        if i > 5:
            return "Vége a függvénynek"
        print(i)

print(exitFunc())

#Fel.9 - return számolás
def returnGyak():
    num1 = int(input("Adjon meg egy számot: "))
    num2 = int(input("Adjon meg egy számot: "))
    if num1 > 0 and num2 > 0:
        if num1 > num2:
            return num1 / num2
            #Amikor return művelet akkor a function értéke a művelet eredménye lesz
            #Azaz pl.: return 10 / 5 akkor a return miatt 2-t kapok vissza
            #Tehát a returnGyak() értéke 2
        else:
            return "Ez rossz"

var = returnGyak()  #var(variable azaz változó)-ban eltárolom a function érétkét
print(var)  #Majd hogy lássuk kiírjuk azt

if var < 10:    #Aztán eldöntjük kisebb vagy nagyobb mint 10
    print("Az eredmény kisebb 10-nél")
else:
    print(var)

#Fel.7 - break, cotinue
def is_prime(p):
    prime = True
    for i in range(2, p):
        if p % i == 0:
            prime = False
            break
    return prime

n = int(input("Adjon meg egy szám imitet: "))
primeList = []
i = 2
while True:
    if is_prime(i):
        primeList.append(i)
    i += 1
    if i == n:
        break
print("A prímszámok listája: ", primeList)

#Fel.8 - For-else
basket = {'alma': 20, 'banánt': 30, 'narancs': 10}
fruit = input("Adjon meg egy gyümölcöt: ")
index = 0
for item in basket:
    if item == fruit:
        print("A kosárban", basket[item], " ", item, "van.")
        break
else:
    quantity = int(input(f"Adja meg a(z) {fruit} darabszámát: "))
    basket[fruit] = quantity
    for item in basket:
        print(item, ": ", basket[item], sep="")

