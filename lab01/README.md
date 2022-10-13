Author: Francesco Di Gangi, Giuseppe Atanasio, Francesco Sorrentino, Alessio Carachino
# Understanding the problem
Given a set of elements {1, 2, …, n} (called the universe) and a collection S of m sets whose union equals the universe, the set cover problem is to identify the smallest sub-collection of S whose union equals the universe. For example, consider the universe U = {1, 2, 3, 4, 5} and the collection of sets S = { {1, 2, 3}, {2, 4}, {3, 4}, {4, 5} }. Clearly the union of S is U. However, we can cover all of the elements with the following, smaller number of sets: { {1, 2, 3}, {4, 5} }. **(wikipedia.org)**

I was able to see that some solutions on the web use a greedy algorithm, and the professor gave us a solution using a greedy algorithm. 

Some examples:

- U = {1,2,3,4,5}
- S = {S1,S2,S3}
- S1 = {4,1,3},    Cost(S1) = 5
- S2 = {2,5},      Cost(S2) = 10
- S3 = {1,4,3,2},  Cost(S3) = 3

Output: Minimum cost of set cover is 13 and 
set cover is {S2, S3}

There are two possible set covers {S1, S2} with cost 15
and {S2, S3} with cost 13.

## Professor's solution
<pre><code>
import logging
logging.getLogger().setLevel(logging.DEBUG)

def greedy(N):
    goal=set(range(N))
    covered=set()
    solution=list()
    all_lists=sorted(problem(N,seed=42),key=lambda 1:len(1))
    while goal != covered:
        x=all_lists.pop(0)
        if not set(x) < covered: #sottoinsieme stretto
            solution.append(x)
            covered |= set(x) #unione fra i due set e prende gli elementi distinti
    print(f"Greedy solution: {solution}")
</code></pre>