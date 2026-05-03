import random
from deap import base, creator, tools, algorithms

# Step 1: Define fitness (maximize)
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# Step 2: Define gene (random number)
toolbox.register("attr_float", random.uniform, -10, 10)

# Step 3: Create individual & population
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attr_float, n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Step 4: Fitness function
def eval_func(individual):
    x = individual[0]
    return (x**2,)   # must return tuple

toolbox.register("evaluate", eval_func)

# Step 5: Genetic operators
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Step 6: Run algorithm
population = toolbox.population(n=10)

algorithms.eaSimple(population, toolbox,
                    cxpb=0.5, mutpb=0.2,
                    ngen=5, verbose=True)

# Step 7: Best result
best = tools.selBest(population, k=1)[0]
print("Best solution:", best, "Fitness:", best.fitness.values)