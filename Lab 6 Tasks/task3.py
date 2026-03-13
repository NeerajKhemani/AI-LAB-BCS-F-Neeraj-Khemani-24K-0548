import random

POPULATION_SIZE = 6
GENERATIONS = 15
MUTATION_RATE = 0.01
CHROMOSOME_LENGTH = 5  

def f(x):
    return x**2 + 2*x

def to_decimal(bits):
    return int("".join(map(str, bits)), 2)

def random_chromosome():
    return [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]

def fitness(chromosome):
    x = to_decimal(chromosome)
    return f(x)

def selection(population):
    total_fit = sum(fitness(c) for c in population)
    pick = random.uniform(0, total_fit)
    running = 0
    for chromosome in population:
        running += fitness(chromosome)
        if running >= pick:
            return chromosome
    return population[-1]

def crossover(mom, dad):
    point = random.randint(1, CHROMOSOME_LENGTH - 1)
    kid1 = mom[:point] + dad[point:]
    kid2 = dad[:point] + mom[point:]
    return kid1, kid2

def mutate(chromosome):
    return [bit ^ 1 if random.random() < MUTATION_RATE else bit for bit in chromosome]

population = [random_chromosome() for _ in range(POPULATION_SIZE)]

print("=" * 55)
print("       GENETIC ALGORITHM — Maximize f(x) = x² + 2x")
print("=" * 55)

overall_best = None
overall_best_fitness = -1

for gen in range(1, GENERATIONS + 1):
    population.sort(key=fitness, reverse=True)

    best_in_gen = population[0]
    best_x = to_decimal(best_in_gen)
    best_fit = fitness(best_in_gen)

    if best_fit > overall_best_fitness:
        overall_best = best_in_gen[:]
        overall_best_fitness = best_fit

    print(f"\nGeneration {gen:02d}")
    print(f"  Best chromosome : {''.join(map(str, best_in_gen))}")
    print(f"  Best x          : {best_x}")
    print(f"  Best fitness    : {best_fit}")

    next_gen = population[:2]  

    while len(next_gen) < POPULATION_SIZE:
        mom = selection(population)
        dad = selection(population)
        kid1, kid2 = crossover(mom, dad)
        next_gen.append(mutate(kid1))
        if len(next_gen) < POPULATION_SIZE:
            next_gen.append(mutate(kid2))

    population = next_gen

print("\n" + "=" * 55)
print("              FINAL RESULT AFTER 15 GENERATIONS")
print("=" * 55)
print(f"  Best Chromosome : {''.join(map(str, overall_best))}")
print(f"  Best x value    : {to_decimal(overall_best)}")
print(f"  Best fitness    : {overall_best_fitness}")
print("=" * 55)
