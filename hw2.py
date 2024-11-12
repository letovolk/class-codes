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

def min_cost_finder_exhaustive_search(cost_matrix_e):
    n = len(cost_matrix_e)
    min_cost_e = float("inf")

    for sequence in itertools.permutations(range(n)):
        cost = total_cost_calculator_exhaustive_search(cost_matrix_e, sequence)
        if cost < min_cost_e:
            min_cost_e = cost
            
    
    return min_cost_e

""""
total_time = 0
matrix_size = 6

# Finds and prints the optimal sequence, minimum cost, time for each cost matrix.
for ith_cost_matrix in cost_matrix_list:
    start_time = time.time()  

    min_cost_e = min_cost_finder_exhaustive_search(ith_cost_matrix)
    
    end_time = time.time()  
    iteration_time = end_time - start_time
    total_time += iteration_time  
    
    #print(f"Optimal sequence for the {matrix_size}x{matrix_size} matrix: {optimal_sequence}")
    print(f"Minimum cost: {min_cost_e}")
    print(f"Time elapsed for the {matrix_size}x{matrix_size} matrix: {iteration_time: } seconds\n")
    matrix_size +=1

print(f"Total time for all matrices: {total_time: } seconds")
print(" ")
"""


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
            
    cache[current_task] = min_cost
    return min_cost

"""
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
"""



def min_cost_and_timer_printer(cost_matrix_list):
    total_time_exhaustive = 0
    total_time_recursive = 0
    #total_time_heuristic = 0
    matrix_size = 6

    for ith_cost_matrix in cost_matrix_list:
        # Exhaustive search method
        start_time = time.time()
        min_cost_e = min_cost_finder_exhaustive_search(ith_cost_matrix)
        end_time = time.time()
        iteration_time_e = end_time - start_time
        total_time_exhaustive += iteration_time_e
        print(f"Exhaustive Search - Minimum cost: {min_cost_e}")
        print(f"Time elapsed for {matrix_size}x{matrix_size} matrix (Exhaustive): {iteration_time_e: } seconds\n")

        # Recursive method
        start_time = time.time()
        initial_visited = [False] * len(ith_cost_matrix)
        initial_not_visited = [True] * len(ith_cost_matrix)
        min_cost_r = total_cost_calculator_recursive_approach(ith_cost_matrix, initial_visited, initial_not_visited)
        end_time = time.time()
        iteration_time_r = end_time - start_time
        total_time_recursive += iteration_time_r
        print(f"Recursive Search - Minimum cost: {min_cost_r}")
        print(f"Time elapsed for {matrix_size}x{matrix_size} matrix (Recursive): {iteration_time_r: } seconds\n")

        # Heuristic method
        #start_time = time.time()
        #min_cost_h = min_cost_finder_heuristic(ith_cost_matrix)
        #end_time = time.time()
        #iteration_time_h = end_time - start_time
        #total_time_heuristic += iteration_time_h
        #print(f"Heuristic Search - Minimum cost: {min_cost_h}")
        #print(f"Time elapsed for {matrix_size}x{matrix_size} matrix (Heuristic): {iteration_time_h: } seconds\n")
        print("*")
        matrix_size += 1

    # Print total time for all methods
    print(f"Total time for Exhaustive Search: {total_time_exhaustive: } seconds")
    print(f"Total time for Recursive Search: {total_time_recursive: } seconds")
    #print(f"Total time for Heuristic Search: {total_time_heuristic: } seconds\n")


print(min_cost_and_timer_printer(cost_matrix_list))

