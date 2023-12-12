Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Find the square root of real or complex numbers
>>> # Importing the complex math module
>>> 
>>> import cmath
>>> 
>>> num = 1+2j
>>> 
>>> # To take input from the user
>>> #num = eval(input('Enter a number: '))
>>> 
>>> num_sqrt = cmath.sqrt(num)
>>> print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real,num_sqrt.imag))
The square root of (1+2j) is 1.272+0.786j
>>> 
>>> 
>>> # Python program to calculate the square root
>>> 
>>> # Note: change this value for a different result
>>> 
>>> num = 125
>>> 
>>> # To take the input from the user
>>> #num = float(input('Enter a number:'))
>>> 
>>> num_sqrt = num ** 0.5
>>> print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))
The square root of 125.000 is 11.180
