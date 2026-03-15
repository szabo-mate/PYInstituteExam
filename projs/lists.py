#Fel.1 - Lista alapok
names = ["Ármin", "Bence", "Zalán", 2, 3, True, "True", ]
print(names)
print(type(names))
print(names[0]) #Lista indexei 0-tól kezdődnek
print(names[-3])#lista[-szám] => lista hátulról számolva

#Fel.2 - len() függvény használata
print("A names lista hossza " + str(len(names)))

#Fel.3 - lista indexek
print(names[0]) #lista legelső indexű eleme
print(names[-1]) #lista legutolsó indexű eleme
print(names[3])
db = 2
print(names[db])
ans = int(input("Hányadik indexű elemét szeretnéd a listának? "))
print(names[ans])

#Fel.4 - list intervallum
print(names[0:3])
print(names[:2])
print(names[3:-1])
print(names[3:])

#Fel.5 - minden elem kiírása while-el
i = 0
while i < len(names):
    print(names[i])
    i += 1

#Fel.6 - első 50 szám lista feltöltés
numbers = []
i = 1
while i <= 50:
    numbers.append(i) #appned =y listához hozzáadjuk a ()-be írt értéket
    i += 1
print(numbers)

#Fel.7 - páros és páratlan számok
odd_numbers = []    #Páratlan
even_numbers = []   #Páros
i = 0
while i < 20:
    if i % 2 == 1:  #Ha az éppen adott számot elosztjuk 2-vel és az 1-et ad vissza maradékul
        odd_numbers.append(i)   #Minden szám ami 2-vel osztva 1-et ad maradékként az páratlan
    else:
        even_numbers.append(i) #Minden szám ami 2-vel osztva 0-t ad maradékként az páros
    i += 1
print("A páratlan számok: " + str(odd_numbers))
print("A páros számok: " + str(even_numbers))

#Fel.8 - Lista elemek cseréje
list_1 = [1, 2, 3, 4, 5]
list_2 = [11, 22, 33, 44, 55]
print("")
print("list_1 a csere előtt: ", list_1)
print("list_2 a csere előtt: ", list_2)
print("")
i = 0
while i < 5:    #5-1 = 4 viszont a listában 5db elem van. Az 5 azért jó mert a listát 0-tól számoljuk => 0, 1, 2, 3, 4 ==> 5db szám
    temp = list_1[i]    #temp(temporary azaz ideiglenes) cseréknél használjuk, ő ugymond kispad
    list_1[i] = list_2[i]
    list_2[i] = temp
    i += 1
#i = 0 => list_1[0] = 1 | list_2[0] = 11
#temp = list_1[0]       => temp = 1                         Most: temp = 1 | list_1[0] = 1 | list_2[0] = 11
#list_1[i] = list_2[i]  => list_1[0] = 11                   Most: temp = 1 | list_1[0] = 11 | list_2[0] = 11
#list_2[i] = temp       => list_2[0] = 1                    Most: temp = 1 | list_1[0] = 11 | list_2[0] = 1

print("list_1 a csere után: ", list_1)
print("list_2 a csere után: ", list_2)

#Fel.9 - Listához hozzáaadás
insertlist = []
insertlist.insert(0, "Logiscool")   #az első az index, a második az érték amit be akarunk szúrni
insertlist.insert(1, "vicces")   #az első az index, a második az érték amit be akarunk szúrni
insertlist.insert(1, "egy")   #az első az index, a második az érték amit be akarunk szúrni
insertlist.insert(3, "és")   #az első az index, a második az érték amit be akarunk szúrni
insertlist.insert(5, "hasznos")   #az első az index, a második az érték amit be akarunk szúrni
insertlist.insert(5, "hely")   #az első az index, a második az érték amit be akarunk szúrni
print("")
print(insertlist)

#Fel.10 - Listából törlés
cats = ["Frici", "Pamut", "Sanyi", "Gombolyag", "Zuzu"]
dogs = ["Szemi", "Szofi", "Hercegnő", "Szimat", "Roti"]
print(cats)
print(dogs)
cats.pop(2)         #A pop a listából index alapján töröl, azaz most kitörli a második indexű elemet
dogs.remove("Roti") #A remove megkeresi az elemet a listából és kitörli
print(cats)
print(dogs)

#Fel.11 - Lista összegzés
#numbers, odd_numbers, even_numbers
i = 0
j = 0
numbers_sum = 0 #numbers lista összege
even_sum = 0    #even_numbers lista összege
odd_sum = 0     #odd_numbers lista összege
while i < len(numbers):
    numbers_sum += numbers[i]
    i += 1
while j < len(even_numbers):
    even_sum += even_numbers[j]
    odd_sum += odd_numbers[j]
    j += 1
print("")
print(f"A numbers lista számainak összege: {numbers_sum}")
print(f"A even_numbers lista számainak összege: {even_sum}")
print(f"A odd_numbers lista számainak összege: {odd_sum}")