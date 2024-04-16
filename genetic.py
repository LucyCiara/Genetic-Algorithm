# Libraries
import random

# Variables for keeping track of the settings of the program
GOALNUMBER = 25
GENERATIONRANGEMAX = 1000
GENERATIONRANGEMIN = 0
AMOUNT1 = 10000
AMOUNT2 = 100
MUTATION = 0.01

# The closer to 0, the closer to the goalnumber it is
def goal(x: int, y: int, z: int) -> int:
    return 6*x**3+9*y**2+90*z - GOALNUMBER

# Assigns points to candidate values based on how close it is to the goal number
def grader(x: int, y: int, z: int) -> int:
    answer = goal(x, y, z)
    if answer == 0:
        return 99999
    else:
        return abs(1/answer)

# Generates an evolution pool, and creates a ranked list based on how high a score they get from the grader(x,y,z) function
evolutionPool = [(random.uniform(GENERATIONRANGEMIN, GENERATIONRANGEMAX), random.uniform(GENERATIONRANGEMIN, GENERATIONRANGEMAX), random.uniform(GENERATIONRANGEMIN, GENERATIONRANGEMAX)) for i in range(AMOUNT1)]
fittest = sorted([(grader(candidate[0], candidate[1], candidate[2]), candidate) for candidate in evolutionPool], reverse=True)

# The game loop
i = 0
run = True
while run:
    # This is how you might start with doing things if you want to mix all the elements instead of keeping them separate
    # elements = []
    # for best in fittest[:AMOUNT2]:
    #     for i in range(3):
    #         elements.append[best[1][i]]

    # Generates an evolution pool which picks traits randomly from the candidates with the top 100 highest points and mutates them
    evolutionPool = [(random.choice(fittest[:AMOUNT2])[1][0]*random.uniform(1-MUTATION, 1+MUTATION), random.choice(fittest[:AMOUNT2])[1][1]*random.uniform(1-MUTATION, 1+MUTATION), random.choice(fittest[:AMOUNT2])[1][2]*random.uniform(1-MUTATION, 1+MUTATION)) for i in range(AMOUNT1)]
    fittest = sorted([(grader(candidate[0], candidate[1], candidate[2]), candidate) for candidate in evolutionPool], reverse=True)

    # Disables the game loop if the results are good enough
    if fittest[0][0] > 999:
        run = False

    # Prints the fittest candidate as well as incrementing i by 1
    print(f"Generation {i} results\n{fittest[0]}")
    i+=1

