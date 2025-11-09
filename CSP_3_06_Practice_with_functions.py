#Herons Formula
import math

#returns the square root of the number n
def root(n):
    return math.sqrt(n)

#Takes in the 3 side lengths of a triangle as arguments and returns half of
#the perimeter of a triangle.
def semiPerimeter(a,b,c):
    s = (a + b + c) / 2
    return s
print(semiPerimeter(4,5,6))

#Modify the below function such that it takes in 4 arguments. multiply the first
#argument by the difference between itself and each individual argument. Reference herons formula for more context.
def multiplyDifferences(s,a,b,c):
    result = s * (s-a) * (s-b) * (s-c) #Heron's formula
    return result
print(multiplyDifferences(7.5,4,5,6))

#Given the 3 sides of a triangle return the area.
#use herons formula
#Use the functions above.
def semiPerimeter(a,b,c):
    s = (a+b+c)/2
    return s

def multiplyDifferences(s,a,b,c):
    result = s * (s-a) * (s-b) * (s-c)
    return result
def herons(a,b,c):
    s = semiPerimeter(a,b,c)
    area = (multiplyDifferences(s,a,b,c)) ** 0.5
    return area

#quadratic equation

#takes in a number as an argument and returns that number multiplied by 2.
def denominator(num):
    return num * 2

print(denominator(38))

#Takes in two arguments. multiply the first argument by negative 1. Then
#return the modified first argument added and subtracted by the second argument.
def plusMinus(a,b):
    a = a* -1
    return a+b, a-b
print(plusMinus(4,6))


#takes in three numbers as arguments. The first and third multiplied together then
#multiplied by 4.Then subtract that result from the second argument squared.
#Return the overall result.
def mainCalc(a,b,c):
    result = b**2 - (4*a*c) #b^2-4ac
    return result
print(mainCalc(9,2,180))

#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.

def semiPerimeter(a,b,c):
    s = (a + b + c) / 2
    return s

def multiplyDifferences(s,a,b,c):
    result = s * (s-a) * (s-b) * (s-c) #Heron's formula
    return result

def denominator(num):
    return num * 2

def plusMinus(a,b):
    a = a* -1
    return a+b, a-b

def mainCalc(a,b,c):
    result = b**2 - (4*a*c) #b^2-4ac
    return result
print(mainCalc(9,2,180))


def quadratic(a,b,c):
    disc=mainCalc(a,b,c) ** 0.5
    pos, neg = plusMinus(b, disc)
    denom = denominator(a)
    x1 = pos/denom
    x2 = neg/denom
    return x1, x2

print(quadratic(4,5,8))
