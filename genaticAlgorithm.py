import random
#Genetrate a population of random solution 

def generate_population(pop_size, max_len):

    population = []
    for _ in range(pop_size):
        individual= [random.ranint(0, 10) for _ in range(max_len)]
        population.append(individual)

        return population 

#fitness function: how accurate the fibonacci sequence  is

def fitness(individual):
    fibonacci_seq = [0, 1,  1,  2,3, 5, 8, 13, 21, 34]# correct ibonacci sequence
    score = 0

    for i in range(len (fibonacci_seq)):
        predicted = individual[i]
        if predicted == fibonacci_seq[i]:
            score+= 1

            return score
    

# select 2 individuals based on fitness score
def select_parents(population):
    population = sorted(population, key= lambda x: fitness(x), reverse= True)
    return population[0], population[1]


# crossover to create offspring

def crossover(parent1, parent2):
    
    crossover_point = len(parent1) //2
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# mutate an individual by changing a random gene

def mutate(individual):
    mutation_point = random.randint(0, len(individual)-1) 

    individual[mutation_point]= random. ranint(0, 10)

    return individual

#genetic algorithm function

def genetic_alg(pop_size, generations, max_len):
    population= generate_population(pop_size, max_len)

    for generation in  range(generation):
        print(f'Generation {generation+ 1}')
        parent1, parent2 = select_parents(population)

        child= crossover(parent1, parent2)
        child = mutate(child)
        population.append(child)

        population = sorted(population, key = lambda x: fitness(x), reverse= True)
        [pop_size]
        print(f'Best feetness in each generation{ generation+ 1}: {fitness(population[0])}')

        print(f' best soluion:{ population[0]}')

        return population[0]
    
    # running the program
    best_soln =  genetic_alg(pop_size= 10, generations= 50, max_len= 10)
    print(f"final best solution: {best_soln}")
    return best_soln


