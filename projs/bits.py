#Fel.1 - Bites operátorok
def bitwiseOp():
    #Bit 0 vagy 1
    print(bin(14))  #1110
    print(bin(6))   #110
    print(14 & 6)
    #Magyarázat:
    #1110 = 14
    #110  = 6
    #110
    #Akkor lesz 1 ha mindegyik számban ugyanazon helyen 1-es áll
    print(14 | 6)
    #Magyarázat:
    #1110 = 14
    #110  = 6
    #1110
    #Akkor lesz 1 ha legalább az egyik szám 1-es
    print(14 ^ 6)
    print(bin(14 ^ 6))
    #Magyarázat:
    #1110 = 14
    #110  = 6
    #1000
    #Akkor lesz 1 ha a két szám valamelyikében 1 de nem mindkettőben
    print(~14)
    #-(1110 + 1) = -1111 = -15

    #Bit eltolás
    print(14 >> 2) #Eltolom 14-et jobbra 2-vel: 1110 -> 11 = 3
    print(bin(14 >> 2)) #Eltolom 14 jobbra 2-vel: 1110 -> 11 = 3

    print(14 << 2) # Eltolom 14-et balra 2-vel: 1110 -> 111000 = 56
    print(bin(14 << 2)) # Eltolom 14-et balra 2-vel: 1110 -> 111000 = 56

bitwiseOp()

#Fel.2 - Bites operátorok vs aritmetikai operátorok
def comparison():
    if 6 % 2 == 0:
        print("I")
    if 6 & 1 == 0:
        #110
        #001
        #000 Mivel egyik sem 1-es így a 000 = 0-val
        print("I")
comparison()

#Fel.3 - Bites eltolás aritmetikai operátorokkal
def aritmeticBit(n):
    n <<= 1 #Megszorozzuk 2-vel
    print(n)
    n <<= 3 #Megszorozzuk 8-al (n itt már 4 => 4 * 8 = 32)
    print(n)
    n >>= 2 #Elosztjuk 4-el
    print(n)

    #Megnézzük, hogy az eredmény páros, vagy páratlan
    if n & 1 == 0:
        print("Páros")
    else:
        print("Páratlan")

aritmeticBit(2)

#Fel.4 - Számrendszerben való váltások
def numSystemSwap():
    num = int(input("Adjon meg egy átváltandó számot: "))
    con = int(input("Adjon meg egy számrendszert(bináris(2), octal(8) hexa(16): "))
    converted_num = 0
    if con == 2:
        converted_num = bin(num).replace("0b", "")
    elif con == 8:
        converted_num = oct(num).replace("0o", "")
    elif con == 16:
        converted_num = hex(num).replace("0x", "")
    else:
        print("Rossz számrendszert adott meg")

    print(converted_num)

numSystemSwap()

#Fel.5 - A bit szám 2 hatványa e
def powerOfTwo(num):
    a = num
    if a > 0 and (a & (a - 1)) == 0:
        print("Ez a 2 hatványa")
    else:
        print("Ez nem a 2 hatványa")

powerOfTwo(26)

#Fel.6 - Bináris -> decimális
test = (1, 1, 0, 1, 0, 0, 1)
print("Az eredeti tuple: " + str(test))

decimal = 0
for i in test:
    #Eltoljuk balra 2^1 értékével azaz 2-vel és vagy operátort hagynálunk
    decimal = (decimal << 1) | i

print("A decimális szám: " + str(decimal))