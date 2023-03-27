import random

n = int(input("Enter an integer n: "))

list = []

for i in range(n):
list.append(random.randint(0,100))


print(list)