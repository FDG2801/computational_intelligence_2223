# Lab 3 - Francesco Di Gangi

You can find the solution in the `taskN_lib` for each task.

## **Problem**

Create four different agents for the game `Nim`, you can find the full description in `lab3_nim.ipynb`

## **Task 3.1**

The hardcoded strategy tries to exploit the number of object we could take depending on the number of `active_rows` left. 
It is more of a late game oriented and it can easily loses versus early game strategy (check `nim-sum` based strategies).

Here is the workflow of the algorithm:
```
    if number of rows is odd:
        take all objects from a random row
    else if the number of rows is even and the longest row has more than one object:
        take objects-1 from a random row with more than one object
    else:
        take all objects from a random row
```

## **Task 3.2** 

### **Strategy 0**
It tries to tune three parameters:
1) **alpha**: it is employed until 'mid-game' finishes. It tries to guide the choice of `num_objects`.
2) **beta**: employed only in 'end-game'. It tries to guide the choice of `num_objects`.
3) **gamma**: employed only in 'eng-game'. It guides whether picking a row with `num_objects` over the average (otherwise below).

### **Strategy 1**
The idea behind this strategy is to use the parameters `alpha` and `beta` to tune the two part of the strategy:

```
    if cooked["num_obj"] / cooked["active_rows_number"] * alpha > beta:
```
The metric `cooked["num_obj"] / cooked["active_rows_number"]` is the non-weighted distribution of the objects over the rows, which means it doesn't take into account that the higher is the index of a row, the higher is the possibility that more object are in there.

The two branches of this strategy exploit the hard-coded strategy in `Task 3.1` but it changes the number of objects to take or from which row the objects have to be taken.

In the end it can achieves 100% winrate over 100 games versus the `pure_random`, and the average win rate is 95%.
It doesn't beat the `optimal_strategy` and that makes sense because we don't exploit `xor` operations or `nim-sum`.

## **Task 3.3**

Behind the implementation of the `nim` with `minmax` there is the basic structure of the algorithm `minmax`:

```
def minimax(currentpos,depth,maximizingplayer):
    if depth==0:
        return currentpos
    if maximizingplayer: #we want to get the max
        maxEval=-infinity
        for each child of position
            eval=minimax(child,depth-1,false)
            maxEval=max(maxEval,eval)
        return maxEval

    else
        minEval=+infinity
        for each child of position
            eval=minimax(minEval,eval)
            minEval=min(minEval,eval)
        return minEval
```

There are few main solutions:
- `possible_new_states`: understand the next state
- `evaluate`: understand if the game is over
- `possible_moves`: calculate all the moves for the program

### **Alpha Beta Pruning**

Basically you consider branches from left to right and sto exploring subtrees once the minimax score of a node is decided. In this way the game become much smaller. 

Alpha-beta pruning is a search algorithm that seeks to decrease the number of nodes that are evaluated by the minmax algorithm. 

To implement the algorithm we refactored the `minimax()` function and add a criterion to the to know when we can stop exploring:

- `alpha`: will represent the minimum score that the maximizing player is ensured.
- `beta`: will represent the maximum score that the minimizing player is ensured.

```
if beta < alpha: stop exploring -> means that the minimax has already found a better option
```

This is implemented with an explicit `for` loop. The scores of child nodes are in the `scores` variable. Also, each `minimax()` iteration, `alpha` and `beta` are changed:

```
if is_maximizing:
            alpha = max(alpha, score)
        else:
            beta = min(beta, score)
```

Note that this is only optimization and does not change the output of the minmax algorithm, so the results are the same. We can also see that the execution time is better with the alpha-beta pruning.

| **Alpha**|**Beta**|**Time**|
|-----|------|----|
|-1|1|0.08599638938903809|
|-0.5|1|0.033998727798461914 |
|-0.5|0.5|0.06699728965759277 |
|-1|0.5|0.053972721099853516 |

In the minmax strategy **player1** always wins.

Theory and part of the code: https://realpython.com/python-minimax-nim/#lose-the-game-of-nim-against-a-python-minimax-player

Theory about ALpha-beta pruning: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning




# **Results**

These results are calculated over 100 games on average.

| **Strategy** | **Opponent strategy** | **Average Win Rate %** |
|-------|--------------------|---|
| hard_coded_strategy     | gabriele                  | 100% |
| hard_coded_strategy      | pure random                  | 90% |
| strategy_0     | gabriele                  | 85% |
| strategy_0     | pure random                  | 45%  |
| strategy_1     | gabriele                  | 100% |
| strategy_1     | pure random                  | 97% |
| strategy_1 | strategy_0 | 80% |



# **Collaborators**
- s296138 Carachino Alessio
- s301665 Francesco Sorrentino,
- s301793 Francesco Di Gangi,
- s300733 Giuseppe Atanasio

