from functions import *
from chromosome import *

# #MAIN
# already_in = input("Do you want to add new values? Y/N")
# if(already_in == "Y"):
#     population_size = int(input("Population size: "))
#     domain_start = int(input("Domain start: "))
#     domain_end = int(input("Domain end: "))
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = int(input("c: "))
#     precision = int(input("Precision: "))
#     crossover_probability = int(input("Crossover probability: "))
#     mutation_probability = int(input("Mutation probability: "))
#     generation_number = int(input("Generation number: "))
#     output_file = input("Output file: ")
# else:
#     population_size = 20
#     domain_start = -1
#     domain_end = 2
#     a = -1
#     b = 1
#     c = 2
#     precision = 6
#     crossover_probability = 25
#     mutation_probability = 1
#     generation_number = 50
#     output_file = "Evolutie.txt"

def start(population_size,
    domain_start,
    domain_end,
    a,
    b,
    c,
    precision,
    crossover_probability,
    mutation_probability,
    generation_number):


    output_file = "Evolutie.txt"
    file_output = open(output_file, "w")

    file(file_output)

    result = 1

    elitist_chromosome = Chromosome(0, 0 ,0)

    #generate the initial population
    population = generate_population(population_size, domain_start, domain_end, a, b, c, precision)

    #print the initial population
    print_population(population)

    #start the generation loop
    for generation in range(generation_number):
        max_fitness = -1
        fitness_sum = 0
        for chromosome in population:
            fitness_sum += chromosome.fitness

        max_fitness = max([chromosome.fitness for chromosome in population])
        index_max_fitness = [chromosome.fitness for chromosome in population].index(max_fitness)

        elitist_chromosome.fitness = population[index_max_fitness].fitness
        elitist_chromosome.real_value =population[index_max_fitness].real_value
        elitist_chromosome.binary = population[index_max_fitness].binary

        if(fitness_sum == 0):
            print("Total fitness = 0 Total Disaster", file = file_output)
            break

        partial_sum = []
        partial_sum.append(0)
        partial_value = 0.0

        for j in range(1, population_size + 1):
            partial_value += population[j-1].fitness
            partial_sum.append(partial_value / fitness_sum)

        partial_sum.append(1)

        if generation == 0: #checks if we are in the first generation
            print("Selection probabilities for the first generation: ", file = file_output)
            for j in range(1, population_size + 1):
                probability = partial_sum[j] - partial_sum[j-1]
                print("Chromosome: " + str(j) + " with probability: " + str(probability) , file = file_output)
            print("Possible selection intervals: " , file = file_output)
            for j in range(population_size + 1):
                print(partial_sum[j] , end=" " , file = file_output)
                if j % 3 == 0:
                 print( file = file_output)

        next_population = []
        for j in range(population_size):
            rand = randomFloat(0, 1)
            left = 0
            right = population_size - 1
            while left < right:
                mid = left + (right - left) // 2
                if rand <= partial_sum[mid]:
                    right = mid
                else:
                    left = mid + 1
            if generation == 0:
                print("u = " + str(rand) + " chromozone: " + str(left), file = file_output)
            next_population.append(population[left - 1])

        if generation == 0:
            print("After selection: ", file = file_output)
            print_population(next_population)

        crossover_population = []
        for j in range(population_size):
            rand = randomFloat(0, 100)
            if generation == 0:
                print("Chromosome " + str(j) + " u: " + str(rand) + " binary: " + next_population[j].binary, end =" ", file = file_output)
            if rand <= crossover_probability:
                if generation == 0:
                    print("Selected with the probability: " + str(rand), file = file_output)
                crossover_population.append(next_population[j])
            else:
                if generation == 0:
                    print(file = file_output)

        if len(crossover_population) % 2 != 0: #ignore the last one if the crossover population isn't even
            crossover_population = crossover_population[:-1]

        for j in range(0, len(crossover_population), 2):
            chromosome1 = crossover_population[j]
            chromosome2 = crossover_population[j + 1]

            if generation == 0 :
                print("Chromosomes: ", file = file_output)
                print("1) " + chromosome1.binary, file = file_output)
                print("2) " +  chromosome2.binary, file = file_output)

            chromosome1.binary, chromosome2.binary = crossover(chromosome1.binary, chromosome2.binary, generation)
            chromosome1.real_value = bits_to_float(chromosome1.binary)
            chromosome2.real_value = bits_to_float(chromosome2.binary)
            chromosome1.fitness = evaluate_fitness(chromosome1.real_value, a, b, c)
            chromosome2.fitness = evaluate_fitness(chromosome2.real_value, a, b, c)

            if generation == 0:
                print("After crossover: ", file = file_output)
                print_chromosome(chromosome1, 1)
                print_chromosome(chromosome2, 2)

        if generation == 0:
            print("After crossover: ", file = file_output)
            print_population(next_population)
            print( file = file_output)
            print("Mutation with the chance: " + str(mutation_probability) + " % for each chromosome", file = file_output)

        nex_population = mutation_for_all_chromosomes(next_population, mutation_probability, a, b, c, generation)
        if generation == 0 :
            print_population(next_population)

        print("Average fitness for generation: " + str(generation)
              +" is: " + str(round(sum([chromosometemp.fitness for chromosometemp in next_population]) / len(next_population), precision))
              + " and the max fitness is: " + str(max_fitness), file = file_output)
        result = max_fitness

    return "The max value of the given function is: " + str(round(result,precision))