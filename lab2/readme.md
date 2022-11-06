# Set covering problem with genetic algorithm
## The Problem

The description of the Set Covering Problem can be found here: https://github.com/FDG2801/computational_intelligence_2223/tree/main/lab1

Meanwhile a description of what a Genetic Algorithm is, can be found here: https://github.com/FDG2801/computational_intelligence_2223/blob/main/genetic_algorithm_from_scratch/Genetic_Algorithm.pdf

# The implementation

In the first part of the code I just use some functions to initialize the universe and the subsets. I use `N` and `num_of_subset` to understand how many subsets I have to create, and I use a check function to understand if the cover is guaranteed or not.

Pseudocode:
```
create universe
create subsets
create weights //all 1s

is covered guaranteed? 
    yes: go on
    no: test new subsets
```

The second part of the code is the actual Genetic Algorithm. From the theory, I use the first population as a vector of `1` and `0`, to understand which set is selected as solution and not. 

The function `check` is a function used to see if the cover is guaranteed (same as the one described in the first part). 

The function `fitness` is inspired to a video that explains the genetic algorithm.

`nog` indicates the number of generations and `changes` indicates the number of changes in the generations.

Pseudocode:
```
create first population

nog == max_gen?
    yes: stop
    no:
        save the older copy of the population
        select two individuals by tournament selection
            here i select the solutions with the highest value of fitness
            choose parents where I use a random threshold
        create the new generation
        calculate the probabilities 
            having the probabilities, I choose the parents with the highest value of fitness*probability
        mutation step:
            initialize a probability vector with random values of 1 and 0
            with a formula I decide which one I have to mutate
        starting the evolution
            R -> set of all, included the element covered
            M -> all uncovered elements
            w -> number of subsets that contains the element
            searching for the element in the universe that are in the single subset
            K -> contains the element that we find in the subset AND that belong to the universe too
            var -> how many times
            var_list -> list of var that are found
        replacing the individual in a population
            if the element is greatest than the average, I change
        preparing the new era
        verify that cover is guaranteed
```

To write this code I followed some tutorials found on YouTube that explains the genetic algorithm and how to code it. It is possible to see something in the repository linked at the beginning.