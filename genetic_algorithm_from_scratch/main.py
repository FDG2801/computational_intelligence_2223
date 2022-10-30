from collections import namedtuple
from functools import partial
from random import choices, randint, randrange, random
from typing import List, Optional, Callable, Tuple

Genome=List[int]    #list of 1 on 0 - 1: included, 0: not included
Population=List[Genome] #the population is a list of genome
#---- Callable for evolution ------
FitnessFunc=Callable[[Genome],int]
PopulateFunc=Callable[[],Population]
SelectFunc=Callable[[Population,FitnessFunc], Tuple[Genome,Genome]]
CrossoverFunc=Callable[[Genome, Genome], Tuple[Genome,Genome]]
MutationFunc=Callable[[Genome],Genome]
#------------------------------------
Thing = namedtuple('Thing', ['name', 'value', 'weight'])

things= [
    Thing('Laptop',500,2200),
    Thing('Headphones',150,160),
    Thing('Coffemug',60,350),
    Thing('Notepad',40,333),
    Thing('Water bottle',30,192),
]

more_things = [
    Thing('Mint',5,25),
    Thing('Socks',10,38),
    Thing('Tissues',15,80),
    Thing('Phone',500,200),
    Thing('Baseball cap',100,70),
] + things

#genetic representation of the solution
def generate_genome(length:int) -> Genome:  #randomly select 1 or 0 in the Genome list
    return choices([0,1], k=length)

#function to generate new solutions
def generate_population(size:int, genome_length:int)->Population:
    return [generate_genome(genome_length) for _ in range(size)]

#fitness function: takes genome, list of things and weights and returns a fitness value
def fitness(genome: Genome, things: [Thing],weight_limit:int)->int:
    if len(genome) != len(things):
        return ValueError("genome and things must be of the same length")
    
    weight=0
    value=0

    for i, thing in enumerate(things):
        if genome[i]==1:
            weight+=thing.weight
            value+=thing.value

            if weight>weight_limit:
                return 0 #maximum weight exceeded, return 0
    return value

#select function to move to the next generation, selecting a pair (parents)
#we use a different function for fitness because the first one is used only for the generation 0
def selection_pair(population:Population, fitness_func:FitnessFunc)->Population:
    #solutions with the highest value should be selected
    return choices(
        population=population,
        weights=[fitness_func(genome) for genome in population],
        k=2 #states that we want to get a pair
    )

#now we need the crossover function
#two genomes as a parameter and return two genometer
def single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
    if len(a) != len(b):
        raise ValueError("genomes a and b must be of some length")

    length=len(a)
    if length<2:
        return a,b
    
    #this is random.
    p=randint(1,length-1)
    return a[0:p]+b[p:],b[0:p]+a[p:]

#now the mutation step
#takes a genome n with a certain probability, change 1 to 0 and 0 to 1
def mutation(genome:Genome,num:int=1,probability:float=0.5)->Genome:
    for _ in range(num):
        index=randrange(len(genome))
        genome[index] = genome[index] if random() > probability else abs(genome[index] - 1)
    return genome

#Now we need the actual evolution
def run_evolution(
    populate_func:PopulateFunc,
    fitness_func:FitnessFunc,
    fitness_limit: int, #done if exceed this limit.
    selection_func:SelectFunc=selection_pair,
    crossover_func:CrossoverFunc=single_point_crossover,
    mutation_func:MutationFunc=mutation,
    generation_limit: int = 100 #maximum number of generations to run if we dont'reach the goal
)->Tuple[Population,int]:
    population=populate_func()

    #generation limit times
    for i in range(generation_limit):
        #sort so the best is in [0]
        population=sorted(
            population,
            key=lambda genome: fitness_func(genome),
            reverse=True
        )

        #check if already reach the fitness limit
        if fitness_func(population[0])>=fitness_limit:
            break
        
        #else new gen, we get two parents and two solution every time
        next_generation=population[0:2]

        #generate all the new solutions for the new generation
        for j in range(int(len(population)/2)-1): #since we already select two, we can avoid to look at part of it
            parents=selection_func(population,fitness_func) #select parents
            offspring_a,offspring_b=crossover_func(parents[0],parents[1]) #children solutions
            offspring_a=mutation_func(offspring_a) #apply mutation
            offspring_b=mutation_func(offspring_b)
            next_generation+=[offspring_a,offspring_b] #add to the new generation
        
        population=next_generation

    population=sorted(
        population,
        key=lambda genome: fitness_func(genome),
        reverse=True
    )
    return population,i 
    
population,generations=run_evolution(
    populate_func=partial(
        generate_population,size=10,genome_length=len(things)
    ),
    fitness_func=partial(
        fitness, things=things,weight_limit=3000
    ),
    fitness_limit=740,
    generation_limit=100
)

def genome_to_things(genome:Genome,things: [Thing])->[Thing]:
    result=[]
    for i, thing in enumerate(things):
        if genome[i]==1:
            result+=[thing.name]
    return result

print(f"Number of generations: {generations}")
print(f"Best solution: {genome_to_things(population[0],things)}")
