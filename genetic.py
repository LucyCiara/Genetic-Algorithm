# Libraries
import random

goalNumber = 25
generationRangeMax = 1000
generationRangeMin = 0
amount1 = 10000
amount2 = 100
mutation = 0.01

def goal(x: int, y: int, z: int) -> int:
    return 6*x**3+9*y**2+90*z - goalNumber

def grader(x: int, y: int, z: int) -> int:
    answer = goal(x, y, z)

    if answer == 0:
        return 99999
    else:
        return abs(1/answer)

evolutionPool = [(random.uniform(generationRangeMin, generationRangeMax), random.uniform(generationRangeMin, generationRangeMax), random.uniform(generationRangeMin, generationRangeMax)) for i in range(amount1)]
fittest = sorted([(grader(candidate[0], candidate[1], candidate[2]), candidate) for candidate in evolutionPool], reverse=True)

i = 0
run = True
while run:
    # elements = []
    # for best in fittest[:amount2]:
    #     for i in range(3):
    #         elements.append[best[1][i]]
    evolutionPool = [(random.choice(fittest[:amount2])[1][0]*random.uniform(1-mutation, 1+mutation), random.choice(fittest[:amount2])[1][1]*random.uniform(1-mutation, 1+mutation), random.choice(fittest[:amount2])[1][2]*random.uniform(1-mutation, 1+mutation)) for i in range(amount1)]
    fittest = sorted([(grader(candidate[0], candidate[1], candidate[2]), candidate) for candidate in evolutionPool], reverse=True)

    if fittest[0][0] > 999:
        run = False

    print(f"Generation {i} results\n{fittest[0]}")
    i+=1

