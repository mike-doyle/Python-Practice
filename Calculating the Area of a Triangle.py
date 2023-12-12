Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Python Program to find the area of a triangle
>>> 
>>> a = 5
>>> b = 6
>>> c = 7
>>> 
>>> # Uncomment below to take inputs from the user
>>> 
>>> # a = float(input('Enter first side:'))
>>> # b = float(input('Enter second side:'))
>>> # c = float(input('Enter third side:'))
>>> 
>>> # Calculate the semi-perimeter
>>> s = (a + b + c ) / 2
>>> 
>>> # Calculate the area
>>> area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
>>> print('The area of the triangle is %0.2f' %area)
The area of the triangle is 14.70
