import time
import random
import itertools

random.seed(2024402252)
# Cost Matrix Generator 
def cost_matrix_generator(n):
    cost_matrix=list()
    for i in range(n):
        cost_matrix.append([])
        for j in range(n):
            cost_matrix[-1].append(random.random())
    return cost_matrix

# Whole Cost Matrices
cost_matrix_list = [
    cost_matrix_generator(6),
    cost_matrix_generator(7),
    cost_matrix_generator(8),
    cost_matrix_generator(9),
    cost_matrix_generator(10),
    cost_matrix_generator(11)
]

# Exhaustive Search
print("Exhaustive Search Starts")

# Calculates the total cost for a given sequence
def total_cost_calculator_exhaustive_search(cost_matrix_e, sequence):
    total_cost = 0
    for i in range(len(sequence) - 1):
        total_cost += cost_matrix_e[sequence[i]][sequence[i + 1]]
    return total_cost

def optimal_sequence_finder_exhaustive_search(cost_matrix_e):
    n = len(cost_matrix_e)
    min_cost = float("inf")
    optimal_sequence = None
    
    for sequence in itertools.permutations(range(n)):
        cost = total_cost_calculator_exhaustive_search(cost_matrix_e, sequence)
        if cost < min_cost:
            min_cost = cost
            optimal_sequence = sequence
    
    return optimal_sequence, min_cost


total_time = 0
matrix_size = 6

# Finds and prints the optimal sequence, minimum cost, time for each cost matrix.
for ith_cost_matrix in cost_matrix_list:
    start_time = time.time()  

    optimal_sequence, min_cost = optimal_sequence_finder_exhaustive_search(ith_cost_matrix)
    
    end_time = time.time()  
    iteration_time = end_time - start_time
    total_time += iteration_time  
    
    print(f"Optimal sequence for the {matrix_size}x{matrix_size} matrix: {optimal_sequence}")
    print(f"Minimum cost: {min_cost}")
    print(f"Time elapsed for the {matrix_size}x{matrix_size} matrix: {iteration_time: } seconds\n")
    matrix_size +=1

print(f"Total time for all matrices: {total_time: } seconds")
print(" ")



print("Recursive Approach Starts")
print(" ")

def total_cost_calculator_recursive_approach(cost_matrix_r, visited, not_visited, cache={}):
    
    if not any(not_visited):  # All cases are visited
        return 0

    current_task = tuple(visited) # Immutability to work with dictinories 
    if current_task in cache:
        return cache[current_task]
    
    # Base to start memoization 

    min_cost = float('inf')

    for cell in range(len(cost_matrix_r)):
        if not_visited[cell]: 
            if any(visited): 
                last_visited = visited.index(True, 0) 
                transition_cost = cost_matrix_r[last_visited][cell]
            else:
                transition_cost = 0  

            # Backtrack 
            new_visited = visited[:]
            new_not_visited = not_visited[:]
            new_visited[cell] = True
            new_not_visited[cell] = False

            # Recursive call to calculate the cost for remaining nodes
            total_cost = transition_cost + total_cost_calculator_recursive_approach(
                cost_matrix_r, new_visited, new_not_visited, cache
            )

            # Update minimum cost
            min_cost = min(min_cost, total_cost)

    # Store in cache
    cache[current_task] = min_cost
    return min_cost

total_time = 0
matrix_size = 6


for jth_cost_matrix in cost_matrix_list:
    start_time = time.time()

    # Initial conditions 
    initial_visited = [False] * len(jth_cost_matrix)
    initial_not_visited = [True] * len(jth_cost_matrix)

    min_cost = total_cost_calculator_recursive_approach(jth_cost_matrix, initial_visited, initial_not_visited)

    end_time = time.time()
    iteration_time = end_time - start_time
    total_time += iteration_time

    print(f"Minimum cost for {matrix_size}x{matrix_size} matrix: {min_cost}")
    print(f"Time elapsed for the {matrix_size}x{matrix_size} matrix: {iteration_time: } seconds\n")
    matrix_size += 1

print(f"Total time for all matrices: {total_time: } seconds")

