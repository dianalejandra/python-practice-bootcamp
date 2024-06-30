# Write a program that compares two numbers and prints on screen which is grater.

inputNumA = input("Insert number A: ")
numberA = float(inputNumA)
inputNumB = input("Insert number B: ")
numberB = float(inputNumB)

if numberA > numberB:
    print("Number A is grater than number B")
elif numberB > numberA:
    print("Number B is grater than number A")
else:
    print("Numbers are equal")