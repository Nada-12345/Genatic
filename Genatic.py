import random

# Define the fitness function
def fitness(x):
    return x ** 2  # Maximizing x^2

# Create an initial population of random individuals (chromosomes)
def create_population(pop_size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(pop_size)]

# Tournament selection: Pick two parents based on fitness
def select_parents(population):
    parent1 = max(random.sample(population, 2), key=fitness)
    parent2 = max(random.sample(population, 2), key=fitness)
    return parent1, parent2

# Crossover: Combine two parents to produce an offspring
def crossover(parent1, parent2):
    return (parent1 + parent2) // 2  # Simple averaging crossover

# Mutation: Randomly mutate an offspring
def mutate(offspring, lower_bound, upper_bound, mutation_rate):
    if random.random() < mutation_rate:
        return random.randint(lower_bound, upper_bound)
    return offspring

# Main genetic algorithm function
def genetic_algorithm(pop_size, generations, lower_bound, upper_bound, mutation_rate):
    population = create_population(pop_size, lower_bound, upper_bound)
    
    for gen in range(generations):
        # Selection, Crossover, and Mutation
        new_population = []
        for _ in range(pop_size // 2):  # Make pairs of parents
            parent1, parent2 = select_parents(population)
            offspring1 = crossover(parent1, parent2)
            offspring2 = crossover(parent2, parent1)
            new_population.append(mutate(offspring1, lower_bound, upper_bound, mutation_rate))
            new_population.append(mutate(offspring2, lower_bound, upper_bound, mutation_rate))
        
        # Replace old population with the new population
        population = new_population

        # Find the best solution in this generation
        best_solution = max(population, key=fitness)
        print(f"Generation {gen + 1}: Best Solution = {best_solution}, Fitness = {fitness(best_solution)}")
        
    return max(population, key=fitness)

# Parameters for the genetic algorithm
population_size = 10
generations = 20
lower_bound = -10
upper_bound = 10
mutation_rate = 0.1

# Run the genetic algorithm
best_solution = genetic_algorithm(population_size, generations, lower_bound, upper_bound, mutation_rate)
print(f"Best Solution found: {best_solution}, Fitness = {fitness(best_solution)}")
