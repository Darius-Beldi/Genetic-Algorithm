import random
import struct

from chromosome import Chromosome

file_output = ""

def file(file):
    global file_output
    file_output = file

def randomFloat(a, b):
    return random.uniform(a, b)

def randomInt(a, b):
    return random.randint(a, b)

def mutation(cromozom):
    cromozom = list(cromozom)
    mutation_mask = [str(randomInt(0,1)) for x in range(len(cromozom))]
    for i in range(len(cromozom)):
        if mutation_mask[i] == "1":
            if cromozom[i] == "1":
                cromozom[i] = "0"
            else:
                cromozom[i] = "1"
    return "".join(cromozom)

def crossover(cromozom1, cromozom2, _generation):
    cromozom1 = list(cromozom1)
    cromozom2 = list(cromozom2)

    crossover_index = randomInt(0, len(cromozom1)-1)
    if _generation == 0:
        print("The slicing is made after the " + str(crossover_index) + " bit", file = file_output)
    for i in range(crossover_index):
        cromozom1[i], cromozom2[i] = cromozom2[i], cromozom1[i]

    return "".join(cromozom1), "".join(cromozom2)


def evaluate_fitness(x, a, b, c):
    return a * x * x + b * x + c

def float_to_bits(num):
    return ''.join(format(byte, '08b') for byte in struct.pack('>f', num))


def mutation_for_all_chromosomes(_population, _mutation_probability, _a, _b, _c, generation):
    for i in range(len(_population)):
        rand = randomInt(0,100)
        if rand <= _mutation_probability:
            _population[i].binary = mutation(_population[i].binary)
            _population[i].real_value = bits_to_float(_population[i].binary)
            _population[i].fitness = evaluate_fitness(_population[i].real_value, _a, _b, _c)

    return _population


def bits_to_float(bits):

    if len(bits) < 32:
        bits = bits.zfill(32)
    elif len(bits) > 32:
        bits = bits[-32:]

    bytes_data = bytearray()
    for i in range(0, 32, 8):
        byte = bits[i:i + 8]
        bytes_data.append(int(byte, 2))


    return struct.unpack('>f', bytes_data)[0]


def generate_chromosome(_domain_start, _domain_end, _a,_b,_c, _precision):
    float_value = round(randomFloat(_domain_start, _domain_end), _precision)
    fitness_value = evaluate_fitness(float_value, _a, _b, _c)
    return Chromosome(float_to_bits(float_value), float_value, fitness_value)

def generate_population(population_size, domain_start, domain_end, a, b, c, precision):
    population = []
    for i in range(population_size):
        population.append(generate_chromosome(domain_start, domain_end, a, b, c, precision))
    return population

def print_chromosome(chromosome, _index):
    print("Chromosome "+ str(_index) +" Float value: " + str(chromosome.real_value) + " Binary value: " + str(chromosome.binary) + " Fitness: " + str(chromosome.fitness), file = file_output)

def print_population(population):
    for index in range(len(population)):
        print_chromosome(population[index], index)