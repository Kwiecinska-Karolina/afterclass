"""Write a program that displays the results of three dice rolls and the sum of the dice rolled.
Apply a random number generator."""
import random

rzut_1 = random.randint(1,6)
rzut_2 = random.randint(1,6)
rzut_3 = random.randint(1,6)

sum = rzut_1 + rzut_2 + rzut_3

print(rzut_1)
print(rzut_2)
print(rzut_3)

print(sum)
