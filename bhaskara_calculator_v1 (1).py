# -*- coding: utf-8 -*-
"""Bhaskara_Calculator_v1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vz2a8KKNRGrVT_c1eYBJd4v_KP7CyZb_
"""

print("Bháskara's Calculator. (ax^2 + bx + c = 0)")

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
print()

Discriminante = (b**2 - 4*a*c)
print("Δ:", Discriminante)
print() 
X1 = ((-b + (Discriminante**0.5)) / 2*a)
X2 = ((-b - (Discriminante**0.5)) / 2*a)
if Discriminante < 0:
  print("Negative Δ, so imaginary roots don't have values ​​in the real numbers.")
else:
  print('Positive Δ, so real roots have values ​​in real numbers.')
  print()
  print("X': ", X1)
  print("X'': ", X2)
print()

#By TeteuRyan