"""
      All of these logics have been created as for te solution to homeworks from python.
      Course Intro to It.


      Solved by @Davlatbek_Kobiljonov.  -> Telegram Username.
      Student of Inha University in Tashkent.

      04.02.23
"""

'''----------------------Lab 8--------------------'''

# The function below is for defining the simple numbers. like 1, 2, 3, 5, 7, that are only dividable by 1 and itself.
n = int(input("Enter a number. "))
print("The list of numbers that are only dividable by 1 and itself. ")
while n < 1000:
    isSimple = True
    i = 2
    while i < n / 2:  # to shorten the process of checking, we just check until half of n
        if n % i == 0:
            isSimple = False
            break
        i += 1
    if isSimple:
        print(n)
    # else:
    #     print(n, "is not a simple number.")
    n += 1


# Program to find a first duplicate in a given array/list. (doesn't really matter)
def duplicate(nums):
    num_set = set()
    # when there is no any duplicate elements in array, then function is going to return -1
    no_duplicate = -1
    no_dub = True

    for i in range(len(nums)):

        if nums[i] in num_set:
            no_dub = False
            return nums[i]
        else:
            num_set.add(nums[i])
    if no_dub == True:
        return no_duplicate


print(duplicate([1, 2, 3, 4, 4, 5, 6]))
print(duplicate([5, 0, 4, 3, 9]))
print(duplicate([2, 3, 3, 4, 8]))

l = []


def sum_elements_of_list(list1: list):
    s = int(0)
    # first off we will flatten all the elements of passed list6, storing them is list named "l"
    for num in list1:
        if type(num) is list:
            sum_elements_of_list(num)
        elif type(num) is type(s):
            l.append(num)

    # secondly we will aum all elements of flattened list, finally getting the sum, which we needed earlier
    for i in l:
        s = s + i
    return s


# even if you pass the list in this form below, the function sum_elements_of_list will work regardless.
list6 = [1, 2, [3, 4], [5, 6], [[[[[[[3]]]]]]]]
print(sum_elements_of_list(list1=list6))

'''---------------Lab 9---------------'''
# in order to create a vector class. we simply can use numpy package where all the properties related to vectors are in

# Firstly let's just try to find simple additions and cross products of 2 vectors
import numpy as np

vector1, vector2 = np.array([1, 2, 3]), np.array([3, 2, 1])
print(np.add(vector1, vector2))  # vector addition
print(np.cross(vector1, vector2))  # cross product
print(np.dot(vector1, vector2))  # dot product


# Now let's create a class where we will create a functions that takes 3 arguments of vector, that is x, y and z.
class VectorArrayInterface(object):
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __array__(self, dtype=None):
        if dtype:
            return np.array([self.x, self.y, self.z], dtype=dtype)
        else:
            return np.array([self.x, self.y, self.z])


vector1, vector2 = VectorArrayInterface(1, 2, 3), VectorArrayInterface(3, 2, 1)
# the rest is the same as shown above
print(np.add(vector1, vector2))  # vector addition
print(np.cross(vector1, vector2))  # cross product
print(np.dot(vector1, vector2))  # dot product


def Euclidian_alg(a, b):
    if b == 0:
        return a
    elif a > b:
        return Euclidian_alg(b, a % b)
    elif b > a:
        return Euclidian_alg(b, a)


# Representing real fractions
class Fraction:
    def __init__(self, numerator, denominator):
        if numerator == denominator:
            self.top = numerator // denominator
            self.bottom = denominator // numerator
        else:
            gcd = Euclidian_alg(numerator, denominator)
            self.top = numerator // gcd
            self.bottom = denominator // gcd

    # __string__ function returns the top and bottom of fraction in the form of the string
    def __str__(self):
        if self.bottom == 1:
            return str(self.top)
        else:
            return str(self.top) + "/" + str(self.bottom)

    # Algorithm for adding
    def __add__(self, other):  # addition of fraction
        if self.bottom != other.bottom:
            self.new_top = self.top * other.top + other.bottom * self.top
            self.new_bottom = self.bottom * other.bottom
            return Fraction(self.new_top, self.new_bottom)
        elif self.bottom == other.bottom:
            self.new_top = self.top + other.top
            return Fraction(self.new_top, other.bottom)

    # Algorithm for subtracting
    def __sub__(self, other):  # subtraction of fractions
        if self.bottom == other.bottom:
            self.new_top = self.top - other.top
            return Fraction(self.new_top, other.bottom)
        else:
            self.new_top = other.bottom * self.top - self.bottom * other.top
            self.new_bottom = self.bottom * other.bottom
            return Fraction(self.new_top, self.new_bottom)

    # Algorithm for multiplication
    def __mul__(self, other):  # multiplication of fractions
        self.new_top = self.top * other.top
        self.new_bottom = self.bottom * other.bottom
        return Fraction(self.new_top, self.new_bottom)

    # Algorithm for dividing
    def __divmod__(self, other):  # division of fractions
        self.new_top = self.top * other.bottom
        self.new_bottom = self.bottom * other.top
        return Fraction(self.new_top, self.new_bottom)

    # Algorithm for float dividing
    def __floordiv__(self, other):
        self.new_top = self.top * other.bottom
        self.new_bottom = self.bottom * other.top
        return Fraction(self.new_top, self.new_bottom)


# These print operations shows the different operations with fractions
print(Fraction(5, 3).__add__(Fraction(1, 3)))  # addition
print(Fraction(5, 3).__sub__(Fraction(1, 3)))  # subtraction
print(Fraction(22, 11).__mul__(Fraction(1, 2)))  # multiplication
print(Fraction(22, 3).__divmod__(Fraction(22, 2)))  # division
# You can write is as shown below
print(Fraction(5, 3) + (Fraction(1, 3)))
print(Fraction(5, 3) - (Fraction(1, 3)))
print(Fraction(5, 3) * (Fraction(1, 3)))
print(Fraction(22, 3) // (Fraction(22, 2)))

'''------------------Lab 10--------------------'''
# I will update soon
