print("ASD, 112121313asasda")
print("alma")
print("")
print("korte")

print("A" + "l" + "m" + "a")

print("""A fák lombaji zöldek
Az alma piros               ak
A banán sárga\t\t\t\tszínű
az ég kék""")
#Ha egy szövegben olyat írunk \t = tabulátor

print("Nagyon szeretem a finomságokat pl \nnyalóka\ncsoki\ncukorka")
#\n az egy szövegben írva új sort jelent

"""
print(input("Hello World "))

print(input("Adjon meg egy szöveget: ").replace("a", "e")) #replace("mit cserélünk", mire cseréljük")

print(input("Adjon meg mégegy szöveget: ").upper()) #.upper mindent nagybetűre vált

print(input("Adjon meg mégegy szöveget: ").lower()) #.lower mindent kisbetűre vált

print(input("Adjon meg mégegy szöveget: ").title()) #.title az első betűt minden szóban váltja nagybetűre

print(input("Adjon meg mégegy szöveget: ").capitalize()) #.capitalize a szövegben az első betűt váltja nagybetűre

"""

print(input("Adjon meg egy verset: ").lower().capitalize().replace("a", "e"))

#Fel.1 - Szöveg hossza
print(input("Adjon meg bármilyen szöveget: ").__len__())

#Fel.2 - Szöveg darabolás
print(input("Adjon meg egy szöveget: ").split(' ')) #Tagol szóközök mentén
print(input("Adjon meg egy szöveget: ").lower().split('a')) #Tagol a betűk mentén

#Fel.3 - Szöveg elem számolás
print(input("Adjon meg egy szöveget: ").count('a')) #count(ertek) megszámolja a megadott szövegben vagy változóban a megadott értéket

#Fel.4 - Szövegből elem keresés
print(input("Adjon meg egy szöveget: ").find('a'))
print(input("Adjon meg egy szöveget: ").find('fa'))
#Visszatért egy indexel. A megadott érték legelső eőfordulásának indexével

#Fel.5 - Szövg eleje és vége
print(input("Adjon meg egy szöveget: ").startswith("A"))
print(input("Adjon meg egy szöveget: ").endswith("a"))

#Fel.6 - szöveg típusa
print(input("Adjon meg egy szöveget: ").isdecimal())    #Decimális típus
print(input("Adjon meg egy szöveget: ").isnumeric())    #Szám típusú
print(input("Adjon meg egy szöveget: ").isalpha())      #betűs(alfabetikus)
print(input("Adjon meg egy szöveget: ").isupper())      #Nagybetűs
print(input("Adjon meg egy szöveget: ").islower())      #Kisbetűs
