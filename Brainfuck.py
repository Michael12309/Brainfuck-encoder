import math
from sys import stdout

def factors(number):
    divide = 1
    count = 0
    mid = 0
    lst = []
    for counter in range(0, number):
        number2 = number/divide
        if number % divide == 0:
            number2 = int(number2)
            number2 = str(number2)
            divide = str(divide)
            lst.append((number2, divide))
            number2 = float(number2)
            divide = int(divide)
            count += 1
        root = float(math.sqrt(number2))
        if math.sqrt(number2) % 1 == 0:
            number2 = int(number2)
            number2 = str(number2)
        number2 = float(number2)
        divide += 1
    return(lst[int(count/2)])
    
def multiply(a, b):
    return "<" + "+"*a + "[>" + "+"*b + "<-]>."

def divide(a, b):
    return "<" + "+"*a + "[>" + "-"*b + "<-]>."

def encode(string):
    last = " "
    stdout.write("++++[>++++++++<-]>")
    for loop in string:
        if ord(last) < ord(loop):
            a, b = factors(ord(loop) - ord(last))
            a, b = int(a), int(b)
            if(a*b < a+b+5):
                stdout.write((a*b)*"+" + ".")
            else:
                stdout.write(multiply(a, b))
        elif ord(last) > ord(loop):
            a, b = factors(ord(last) - ord(loop))
            a, b = int(a), int(b)
            if(a*b < a+b+5):
                stdout.write((a*b)*"-" + ".")
            else:
                stdout.write(divide(a, b))
        else:
            stdout.write(".")
        last = loop

encode("any text")
