#Fel.1 - matrix
def createMatrix():
    matrix_1 = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]]
    print(matrix_1)
#createMatrix()

#Fel.2 - Matrix random számokkal
def createMatrix2():
    matrix_2 = []
    for i in range(4):
        temp_list = []
        for j in range(4):
            temp_list.append(j)
        matrix_2.append(temp_list)
    print(matrix_2)
createMatrix2()

#Fel.3 - Matrix elem csere
def modifyMatrix():
    matrix = [[1, True, 3, 'd', 5],
              [45.5, 2, 9, 'b', '6'],
              [99, 22, 'a', 4, 'g'],
              [5, 12, 3, 'k', 'e'],
              [0, 21, 35, False, 56]]
    print("Előtte:")
    for i in range(len(matrix)):
        print(matrix[i])
    row = -1
    while row < 0 or row > 4:
        row = int(input("Adja meg a matrix egyik sorának számát: "))
    col = -1
    while col < 0 or col > 4:
        col = int(input("Adja meg a matrix egyik oszlopának számát: "))
    change_to = input("Adja meg mire változtassa az értéket: ")
    change_type = input("Milyen típusra(str, int, bool): ")
    if change_type == 'str':
        change_to = str(change_to)
    elif change_type == 'int':
        change_to = int(change_to)
    elif change_type == 'bool':
        change_to = bool(change_to)
    else:
        print("Rossz típust adott meg")
        return
    matrix[row][col] = change_to
    print("Utána:")
    for i in range(len(matrix)):
        print(matrix[i])

#modifyMatrix()

#Fel.4 - Érték szerzés matrix-ból
data = ["Póló száma", "Név", "Kor", "Magasság", "Súly"]
team = [[1, "Dorka", 24, 176, 56],
        [2, "Jani", 32, 190, 87],
        [13, "Bea", 20, 160, 54],
        [42, "Dzsina", 23, 179, 63],
        [99, "Feri bá", 39, 188, 82]]

print(team[2]) #Harmadik sort írja ki mert 0-tól megy az indexelés
print(team[-1]) #Az utolsó sorát kapjuk meg
print(team[2][1]) #Harmadik sor, második eleme
print(team[2][-1]) #Harmadik utolsó eleme
column = []
for i in team:
    column.append(i[1]) #Második oszlop
print(column)
for i in range(len(team)): #sort számol
    for j in range(len(team[0])): #Oszlop(sorban hanyadik elemet képezi)
        print(team[i][j], end=" ") #i = sor(row), j = oszlop(col)
        print("")
for row in team:
    for item in row:
        print(item, end=" ") #Minden elemet abból a sorból a amin van

print("")

#Fel.5 - Matrix sort()
import random
def sortingMatrix():
    matrix = [] #Üres matrix
    for i in range(5):
        temp = []
        for i in range(5):
            temp.append(random.randint(0, 10))
        matrix.append(temp)
    print(matrix)

    matrix.sort()
    print(matrix)

    for item in matrix: #Bejárjuk a teljes matrixot
        item.sort()
    print(matrix)
sortingMatrix()

#Fel.6 - Órarend
def timetable():
    table = [["Tesi", "Matek", "Matek", "Angol", "Angol"], #Hétfő
            ["Tesi", "Tesi", "Matek", "Magyar", "Magyar"], #Kedd
            ["Kémia", "Kémia", "Ének", "Fizika", "Magyar"], #Szerda
            ["Angol", "Töri", "Földrajz", "Infó", "Infó"], #Csütörtök
            ["Matek", "Biosz", "Töri", "Töri", "Technika"],] #Péntek

    time_table = []
    for j in range(5):
        temp_table = []
        for i in range(int(input("Hány órád lesz ma? "))):
            lesson = input("Melyik órád lesz ma? ")
            temp_table.append(lesson)
        time_table.append(temp_table)
    days = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek"]
    ind = 0
    for t in time_table:
        print(f"{days[ind]}:{t}", end='\n')
        ind += 1
timetable()