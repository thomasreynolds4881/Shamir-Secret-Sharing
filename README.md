# ShamirSecretSharing
An implementation of Shamir's Secret Sharing that uses a linear function to encrypt a password.

# How it works
Create.py asks for an input password and makes the word into numeric values (using ASCII). This newly generated number is now the y-intercept of a linear function with a randomly generated slope. Using this slope, the program outputs a specified amount of random points on the function. By using at least two of these points, one is able to calculate the y-intercept (which can then be converted from ASCII into the actual password).

# More info on the ASCII conversion
In order to allow any character, an ASCII value that is only two digits will be written with a leading zero (i.e. 050 instead of 50). For example, something like PaSsWoRd would convert to 080097083115087111082100.

# Precision issues
Unfourtunately, this method of encryption creates some very large numbers, and causes problems in Python when trying to make a decoder. I attempted to make something that should work in theory, but precision issues make it only work with passwords under four digits or so.
