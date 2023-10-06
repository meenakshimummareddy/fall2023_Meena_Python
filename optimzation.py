from deap import base, creator, tools, algorithms
import random

# Subheading 1: Define the optimization problem
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, 0, 10)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=5)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Subheading 2: Define the evaluation function
def evaluate(individual):
    return sum(individual),

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Subheading 3: Create and run the genetic algorithm
population = toolbox.population(n=50)
algorithms.eaMuPlusLambda(population, toolbox, mu=50, lambda_=100, cxpb=0.7, mutpb=0.2, ngen=100, stats=None, halloffame=None)

# Subheading 4: Analyze and display the optimized solution
best_individual = tools.selBest(population, k=1)[0]
print("Best Individual:", best_individual)
print("Best Fitness Value:", best_individual.fitness.values[0])
