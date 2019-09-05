import time
from datetime import date
import math


def uppg1(): #1.7
    t = int(input("How many seconds?"))
    if t < 60:
        print("that is " + str(t) + " seconds")
    elif t < 3600:
        print("that is " + str(t // 60) + " minutes and " + str(t % 60) + " seconds")
    elif t < 86400:
        print("that is " + str(t // 3600) + " hours, " + str(t // 60) + " minutes and " + str(t % 60) + " seconds")
    else: 
        print("that\'s more than a day atleast")

def uppg2(): #1.4
    print("Converts km/h to mph")
    print(float(input("How many km/h?")) / 1.609)

def uppg3(): #1.5
    print("This adds 2 numbers")
    n1 = input("the first number")
    n2 = input("the second number")
    print("The sum of the previous numbers is " + str(int(n1) + int(n2)))

def uppg4():#1.6
    today = date.today()
    year = today.year
    birthYear = int(input("What year were you born?"))
    birthMonth = input("what month is your birthday?")
    birthDay = int(input("What date is your birthday?"))
    print("You will become " + str(year - birthYear + 1) + " years old on " + birthMonth + " " + str(birthDay))

def unit(number):
    return number[len(number) - 1]

def ten(number):
    if len(number) < 2:
        return "0"
    else:
        return number[len(number) - 2]

def uppg5(): #1.15
    number = input("Write a number")
    print("The single unit number is " + unit(number) + " and the 10th unit number is " + ten(number))

def swap(): #Jag vet att detta är det jobbigaste sättet du kan göra detta på
    #men jag hade redan börjat på det innan jag fick veta att man inte kan ändra strings
    number = input("Write a number that's grater than 10")
    first = number[len(number) - 1]
    tenth = number[len(number) - 2]
    number = float(number)
    number /= 100
    number = math.floor(number)
    number = str(int(number))
    if number != "0":
        string = number + first + tenth
    else:
        string = first + tenth
    return string

def uppg6(): #1.16
    print(swap())

def max(list):
    while True:
        for i in range(len(list)):
            if i < len(list) - 1:
                if list[i] < list[i + 1]:
                    temp = list[i]
                    list[i] = list[i + 1]
                    list[i + 1] = temp
                    break
            else:
                return list
        continue

def uppg7():#1.20
    list = []
    while True:
        number = input('Write a number or "end"')
        if number == "end":
            break
        else:
            list.append(int(number))
    max(list)
    string = ""
    for i in range(len(list)):
        string += str(list[i]) + ", "
    print(string)

def uppg8():
    number = input("Write a number")
    if int(number)%2 == 1:
        print("Thats an odd number")
    else:
        print("thats an even number")

def isIsosceles(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return False
    elif x == y:
        return True
    elif x == z:
        return True
    elif y == z:
        return True
    else:
        return False

def uppg9():
    isIso = isIsosceles(float(input("Write the length of one of the sides of a triangle")), float(input("The second side")), float(input("The third side")))
    if isIso:
        print("Your triangle is isosceles")
    else:
        print("Your triangle is not isosceles")

def isLeapyear(x):
    if x % 4 != 0:
        return False
    elif x % 100 != 0:
        return True
    elif x % 400 == 0:
        return True
    else: return False

def uppg10():
    if isLeapyear(int(input("Write a year"))):
        print("Your year is a leap year")
    else:
        print("Your year isn't a leap year")

def introduce(name, age=""):
    if age == "":
        print("Hello, my name is " + name + " and my age is a secret")
    else:
        print("Hello, my name is " + name + " and I'm " + age + " years old")

def uppg11():
    name = input("Write your name")
    age = input("If you want to, write your age. Otherwise, just hit enter")
    if age == "":
        introduce(name)
    else:
        introduce(name, age)
    

def uppg12():
    sub = input("a-e")
    if sub == "a":
        for i in range(26):
            print(str(i))
    elif sub == "b":
        for i in range(26):
            print(str(-i + 25))
    elif sub == "c":
        for i in range(0, 31, 2):
            print(str(i))
    elif sub == "d":
        a = 0
        for i in range(37, 149):
            a += int(i)
        print(int(a))
    elif sub == "e":
        a = int(input("first number in the interval"))
        b = int(input("last number in the interval"))
        c = 0
        for i in range(a, b + 1):
            c += i
        print("the sum of all the numbers in the interval is " + str(c))
    else: 
        print("no")

def isPrime(num):
    if num <= 3:
        return True

    if num % 2 == 0:
        return False

    i = 1
    while i < int(num / 2 - 1):
        if num % (2 * i + 1) == 0:
            return False
        i += 1

    return True

def uppg13():
    print(str(isPrime(int(input("Write a number, I will check if its a prime")))))

def fibNum(num):
    n = 1
    fn = 0
    f_1 = 1
    f_2 = 1
    while n < num + 1:
        if n == 1:
            fn = 1
            n +=1
            continue
        if n == 2:
            n += 1
            continue
        temp = f_1
        f_1 = fn
        f_2 = temp
        fn = f_1 + f_2
        n += 1
    print(fn)

def fibNumPrint(num):
    n = 1
    fn = 0
    f_1 = 1
    f_2 = 1
    while n < num + 1:
        if n == 1:
            fn = 1
            print("F(" + str(n) + ") = " + str(fn))
            n +=1
            continue
        if n == 2:
            print("F(" + str(n) + ") = " + str(fn))
            n +=1
            continue
        temp = f_1
        f_1 = fn
        f_2 = temp
        fn = f_1 + f_2
        print("F(" + str(n) + ") = " + str(fn))
        n +=1

def approxPi(num):
    n = 0
    pi = 0
    while n < num:
        pi += (-1) ** n / (2 * n + 1)
        n += 1
    pi *= 4
    print(pi)


def approxPiRaman(num):
    n = 0
    pi = 0
    while n < num:
        pi += (math.factorial(4 * n) * (1103 + 26390 * n)) / ((math.factorial(n)) ** 4 * 396 ** (4 * n))
        n += 1
    pi *= (2 * math.sqrt(2) / 9801)
    pi = pi ** -1
    print(pi)



uip = input("Välj uppgift (1-20)")
if uip == "1": 
    uppg1()
elif uip == "2":
    uppg2()
elif uip == "3":
    uppg3()
elif uip == "4":
    uppg4()
elif uip == "5":
    uppg5()
elif uip == "6":
    uppg6()
elif uip == "7":
    uppg7()
elif uip == "8":
    uppg8()
elif uip == "9":
    uppg9()
elif uip == "10":
    uppg10()
elif uip == "11":
    uppg11()
elif uip == "12":
    uppg12()
elif uip == "13":
    uppg13()

