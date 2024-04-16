import random

print("test\ntest")
evolutionPool = [(random.uniform(-1000, 1000), random.uniform(-1000, 1000), random.uniform(-1000, 1000)) for i in range(10)]
print(evolutionPool)

listThing = [1, 2, 3, 4]
for item in listThing:
    item = 0
print(listThing)

testList = [[1, 2, 3] for i in range(3)]
print(testList.flatten())