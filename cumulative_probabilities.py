import math
import numpy as np
from pprint import pprint

# Using a 5x5 grid with center position 'empty', we get get 5+5+4+5+5=24 different cells.
N_CELLS = 24
N_BITS = N_CELLS
# Each cell can be called or not. We need one less bit for the center position
N_BOARDS = 2**N_CELLS-1
# The number of 'balls' or numbers to draw from
N_NUMBERS = 75

def no_of_combinations(set_size, n_draws):
    """
    Returns the number of combinations by drawing n_draws times from a set of size set_size w/o
    replacement.
    """
    return int(math.factorial(set_size) / (math.factorial(n_draws) * math.factorial(set_size -
        n_draws)))

def single_card_probability(n_draws, bingo_probs):
    cumulative_probability = 0.0
    for i in range(4, n_draws):
        probability = no_of_combinations(N_CELLS, i)
        probability *= no_of_combinations(N_NUMBERS - N_CELLS, n_draws - i)
        probability /= no_of_combinations(N_NUMBERS, n_draws)
        probability *= bingo_probs[i]
        cumulative_probability += probability
    print(n_draws, cumulative_probability)
    return cumulative_probability

# Variable to store the number of bingos for each number of draws
nr_bingos = np.zeros(N_BITS + 1, dtype=int)

# Bingo patterns according to the following representation of the board:
# 5  4  3  2  1
# 10 9  8  7  6
# 14 13 x  12 11
# 19 18 17 16 15
# 24 23 22 21 20
bingo_patterns = [
   '000000000000000000011111', # row 1
   '000000000000001111100000', # row 2
   '000000000011110000000000', # row 3 (c)
   '000001111100000000000000', # row 4
   '111110000000000000000000', # row 5
   '100001000010001000010000', # col 1
   '010000100001000100001000', # col 2
   '001000010000000010000100', # col 3 (c)
   '000100001000100001000010', # col 4
   '000010000100010000100001', # col 5
   '100000100000000001000001', # diag 1 (c)
   '000010001000000100010000', # diag 2 (c)
]

# convert into ints to allow bit manipulation
bingo_patterns = list(map(lambda x: int(x, 2), bingo_patterns))

# loop over all possible boards
for x in range(1, N_BOARDS + 1):
  # count the number of 'draws' as the number of activated bits
  n_draws = bin(x).count('1')

  # compare the current pattern to all known bingo patterns
  for pattern in bingo_patterns:
     if((x & pattern) == pattern):
        nr_bingos[n_draws] += 1
        # stop once a bingo for this pattern is found
        break

# print :)
print("=== no of bingos ===")
for i,n in enumerate(nr_bingos):
  print('{}\t{}'.format(i,n))

# now calculate the number of combinations to make with each value
bingo_probs = np.zeros(N_BITS + 2)
for n_draws, n_bingos in enumerate(nr_bingos):
    n_combinations = no_of_combinations(N_CELLS, n_draws)
    bingo_probs[n_draws] = n_bingos / n_combinations

print("=== probability of at least 1 bingo ===")
for i, p in enumerate(bingo_probs):
    print('{}\t{}'.format(i, p))

print(single_card_probability(10, bingo_probs))

