#Fel.1 - while ciklus
"""
number = 1
while True:
    print(number)
    number += 1
"""

#Fel.2 - Első 10 szám
number = 1
sum = 0
while number < 11:
    print(number, end=", ")
    sum += number
    number += 1
print("")
print(sum)

#Fel.3 - Számjegyek száma
num = 975482        #975482 / 10 = 97548,2 --> 0,975482
num2 = 975482        #975482 / 10 = 97548,2 --> 0,975482
count = 0
while num2 != 0:
    num2 //= 10
    count += 1
print(f"{num} számjegyeinek száma: {count}db")
print(num, "számjegyeinke száma:", count, "db")
print(str(num) + " számjegyeinek száma: " + str(count) + "db")

#Fel.4 - Gondoltam egy számra
print("\n")
print("Gondoltam egy számra!")
n = 42
guessnum = int(input("Hány próbálkozásod legyen? "))
guess = 0
while guessnum > 0 and guess != n:
    guess = int(input("Tippelj egy számot "))
    if guess > n:
        print("Kisebb számra gondoltam")
    elif guess < n:
        print("Nagyobb számra gondoltam")
    guessnum -= 1
    print(f"Még {guessnum}db próbálkozásod van")
if guess == n:
    print(f"Gratulálok a szám {guess} volt.")
else:
    print(f"Ez most nem jött össze. A szám {n} volt.")

#Fel.5 - Fibonacci sorozat
counter = 10
num1 = 0
num2 = 1
print("Fibonacci sorozat első 10 eleme")
while counter > 0:
    print(str(num1) + "\n")
    temp = num1 + num2
    num1 = num2
    num2 = temp
    counter -= 1

#Fel.6 - Prímszámok 1-től 100-ig
prime_num = 2
count = 2
isPrime = True
while prime_num < 100:
    count = 2
    isPrime = True
    while count < prime_num:
        if prime_num % count == 0:
            isPrime = False
        count += 1
    if isPrime:
        print(prime_num)
    prime_num += 1

print("")

#Fel.7 - Szó ism
word = input("Mit mondjak? ")
times = int(input("Hányszor ismételjem? "))
i = 0
while i < times:
    print(word)
    i += 1

print("")

#Fel.8 - Szám fordított kiírás
original = int(input("Adjon meg egy sámot: "))
o_num = original
reverse = 0
while original > 0:
    ln = original % 10 #Itt a maradékot kapja meg pl.: Ha az original 123 % 10 -> 12,3 => ln = 3
    reverse = reverse * 10 + ln
    original //= 10
print("A számod visszafelé: ", reverse)

#Fel.9 - Faktoriális számolás
fact = int(input("Adjon meg egy számot: "))
ori = fact
factorial = 1

while fact > 0:
    factorial *= fact
    fact -= 1
    #pl.: fact = 5, factorial = 1 -> 1 * 5 => factorial = 5, 5 - 1(fact -= 1) => fact = 4
print(f"{ori}! = {factorial}")