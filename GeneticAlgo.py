import math
import random

def fitness_function(x):
    return int(math.pow(x, 2))

def Genetic(length):
    population_size = 10
    chromosome_length = length
    mutation_rate = 0.1
    generations = 100
    
    population = []
    for _ in range(population_size):
        chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
        population.append(chromosome)
#         print(f"{population}\n")
        
    
    for generation in range(generations):
        # General Fitness Function
        fitness_scores = []
        for chromosome in population:
            x = int(''.join(map(str, chromosome)), 2)
            fitness = fitness_function(x)
            fitness_scores.append(fitness)
            
        parents = []
        for _ in range(population_size):
            total_fitness = sum(fitness_scores)
            selection_point = random.uniform(0, total_fitness)
            cumulative_fitness = 0
            for i, score in enumerate(fitness_scores):
                cumulative_fitness += score
                if cumulative_fitness >= selection_point:
                    parents.append(population[i])
                    break
            
        # Crossover and Mutation
        new_population = []
        for i in range(0, population_size, 2):
            parent1, parent2 = parents[i], parents[i+1]
            crossover_point = random.randint(1, chromosome_length -1)
            child1 = parent1[:crossover_point] + parent2[crossover_point:]    
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            
            for j in range(population_size):
                if random.random() < mutation_rate:
                    child1[j] ^= 1
                if random.random() > mutation_rate:
                    child2[j] ^= 1
            
            new_population.append(child1)
            new_population.append(child2)
            
        population = new_population
        
    best_chromosome = population[0]
    best_fitness = fitness_scores[0]
    for i in range(population_size):
        if fitness_scores[i] > best_fitness:
            best_chromosome = population[i]
            best_fitness = fitness_scores[i]
                
    best_x = int(''.join(map(str, best_chromosome)), 2)
        
    print('Best Chromosome:',best_chromosome)
    print('Best Fitness:',best_fitness)
    print('Best X:',best_x)

length = int(input("Enter the length of chromosomes: "))
Genetic(length)