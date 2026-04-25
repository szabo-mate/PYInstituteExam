#Tuple hasonlóan működik mit egy lista
#Viszont a tuple értéke nem változtatható meg
#Az első létrehozás után az értékek 
#Nem cserélehtők, nem adhatunk hozzá értéke, nem törölhetünk belőle
#létrehozás: tuple_neve = ()
#A tuple jele ()

#Fel.1 - Tuple készítés
empty_tuple = ()
tuple1 = (1, 2, 3, 4)
tuple2 = (1, "asd", True, [1, 2, 3], tuple1)
print(empty_tuple)
print(tuple1)
print(tuple2)
tuple3 = (1)
print(type(tuple3))
tuple4 = (4,)
print(type(tuple4))
tuple5 = 1, 10, 20
print(tuple5)
tuple6 = tuple((1, 2, 3))
print(tuple6)

#Fel.2 - Lista vs Tuple
list1 = [1, 2, 3]
print(type(list1))
tuple1 = tuple(list1)
print(type(tuple1))
list2 = list(tuple1)
print(type(list2))

#Fel.3 - tuple-ből törlés
list1 = [1, 2, 3]
tuple1 = (1, 2, 3)
list1.append(4)
del list1[3]
list1.insert(1, 10)
list1[2] = 20
print(list1)

tuple1.append(4)
del tuple1[3]
tuple1.insert(1, 10)
tuple1[2] = 20

del tuple1

#Fel.4 - indexelés
list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 2, 3, 4, 5)
print(list1[1], tuple1[1])
print(list1[:2], tuple1[:2])
print(list1[-3:-1], tuple1[-3:-1])
print(list1[3:], tuple1[3:])
print(len(list1), len(tuple1))



#Fel.5 - Páros vagy páratlan
import random

list1 = [random.randint(1, 100) for i in range(10)]
tuple1 = tuple(random.randint(1, 100) for j in range(10))
even_list = []
odd_list = []
even_tuple = []
odd_tuple = []
for i in range(len(list1)):
    if list1[i] % 2 == 0:
        even_list.append(list1[i])
    else:
        odd_list.append(list1[i])
    if tuple1[i] % 2 == 0:
        even_tuple.append(tuple1[i])
    else:
        odd_tuple.append(tuple1[i])
print(list1, even_list, odd_list)
print(tuple1, even_tuple, odd_tuple)



#Fel.6 - Tuple-höz hozzáadás és szorzás
import random

tuple1 = tuple(random.randint(1, 10) for i in range(5))
tuple2 = tuple(random.randint(1, 10) for j in range(5))
print(tuple1, tuple2)
print(tuple1 + tuple2)
print(3 * tuple1)
print(5 * tuple2)



#Fel.7 - Elemenként szorzás
import random

tuple1 = tuple(random.randint(1, 10) for i in range(5))
print(tuple1)
for i in tuple1:
    print(i * 3, end=" ")

#Fel.8 - 2db 1 hósszú tuple összeadása
tuple2 = (1, )
tuple3 = (1, )
tuple4 = tuple2 + tuple3
print(tuple4)
#Ilyenkor a 2 elemet egymás után veszi,
#mintha csak egymás után kiiratnánk a tuple-t


#Fel.9 - tuple értékváltás
tup1 = (1, 2, 3)
tup2 = (3, 4, 5)
tup3 = 1, 4, 5
print(tup1, tup2, tup3)
tup1, tup2, tup3 = tup3, tup2, tup1
print(tup1, tup2, tup3)

tup2 = (1, 2, 3, 4)
print(tup2)
tup2 = tup2[::-1] #Visszafelé kiírás
print(tup2)
print(tup2)
tup2 = tup2[::-1] #Visszafelé kiírás
print(tup2)

#Fel.10 - Osztályzatok
#a - Jegy generálás
list1 = []
for i in range(5):
    list1.append(int(input("Adjon meg gy pontszámot")))
tuple_list = []
for i in list1:
    if i >= 85:
        tuple_list.append(tuple((i, 5)))
    elif i >= 70:
        tuple_list.append(tuple((i, 4)))
    elif i >= 50:
        tuple_list.append(tuple((i, 3)))
    elif i >= 40:
        tuple_list.append(tuple((i, 2)))
    else:
        tuple_list.append(tuple((i, 1)))
tuple_list = tuple(tuple_list)
print(tuple_list)

#b - min és max pont
minimum = 101
maximum = -10
for i in tuple_list:
    if i[0] > maximum:
        maximum = i[0]
    if i[0] < minimum:
        minimum = i[0]
print(f"Max pont: {maximum}, és a min pont: {minimum}")

#c - Átlag pontok és jegyek
sum_points = 0
sum_grades = 0
for i in tuple_list:
    sum_points += i[0]
    sum_grades += i[1]
print(f"Az átlag pont: {sum_points / len(tuple_list)},"
      f" és az átlag jegy: {sum_grades / len(tuple_list)}")

#d - Hány jegy van
list_grades = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]
for i in range(1, 6):
    for j in tuple_list:
        if j[1] == i:
            list_grades[i - 1][1] += 1
print(list_grades)
