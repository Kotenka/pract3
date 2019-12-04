import random
import matplotlib.pyplot as plt

def calc_max_fitness(board_size):
    i = board_size-1
    max_fitness = 0
    while i > 0:
        max_fitness += i
        i -= 1
    return max_fitness



def random_individual(board_size):
    return [random.randint(1, board_size) for _ in range(board_size)]


def fitness(individual):
    horizontal_colission = sum([individual.count(queen)-1 for queen in individual]) /2
    diagonal_collisions = 0

    n = len(individual)
    left_diagonal = [0]*2*n
    right_diagonal = [0]*2*n

    for i in range(n):
        left_diagonal[1+individual[i]-1] += 1
        right_diagonal[len(individual)-i+individual[i]-2] += 1

    for i in range(2*n-1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i]-1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i]-1

        diagonal_collisions += counter/(n-abs(i-n+1))

        m_fitness = calc_max_fitness(len(individual))
    return int(m_fitness-(horizontal_colission+diagonal_collisions))




def probability(individual, fitness):
    return fitness(individual)/calc_max_fitness(len(individual))

def random_pick (population, brobabilities):
    populationWithProb = zip(population, brobabilities)
    total = sum(w for c, w in populationWithProb)
    r = random.uniform(0, total)

    upto = 0
    for c, w in zip(population, brobabilities):
        if upto+w >= r:
            return c
        upto += w
    else:
        upto += w

def reproduce(x,y):
    n = len(x)
    c = random.randint(0, n-1)
    return x[0:c]+y[c:n]

def mutation(x):
    n = len(x)
    c = random.randint(0, n-1)
    m = random.randint(1, n)
    x[c] = m
    return x

def genetic_queen (population, fitness):
    new_population = []
    probabilities = [probability(n, fitness) for n in population]
    for i in range(len(population)):
        x = random_pick(population, probabilities)
        y = random_pick(population, probabilities)
        child = reproduce(x, y)
        if random.random() < mutation.probabilities:
            if random.random() < 0.02:
                child=mutation(child)
        new_population.append(child)
        if fitness(child) == calc_max_fitness(len(child)): break

    return new_population

def mean_fitness_in_generation(population):
    sum = 0
    n = len(population)
    for i in range(n):
        sum += fitness(population[i])
    return sum/n

def print_individual(x):
    print("{}, fitness={}".format(str(x), fitness(x)))

if __name__ == "__main__":
    board_size = 8
    #KOLVO osobey
    max_pop = 250
    mutation.probabilities = 0.001
    max_fitness = calc_max_fitness(board_size)
    population = [random_individual(board_size) for __ in range(max_pop)]
    generation = 1

    X = []
    Y = []

    while not max_fitness in [fitness(x) for x in population]:
        X.append(generation)
        population = genetic_queen(population, fitness)
        m = mean_fitness_in_generation(population)
        Y.append(m)
        print("population= " + str(generation), "mean fitness= ", m)
        generation += 1
    print("solution find in generation: "+str(generation-1))
    for x in population:
        if fitness(x) == max_fitness:
            print_individual(x)

    plt.plot(X, Y)
    plt.show()



