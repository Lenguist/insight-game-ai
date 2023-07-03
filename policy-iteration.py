"policy iteration to get optimal offer sequence for non-markov model"

value = 10
range_min = 11
range_max = 30
imp_incr = 0.2
imp_init = 0


# to get optimal strategy
import math
from itertools import combinations

def all_possible_strategies(range_min, range_max, imp_incr, imp_init):
  strategies = []
  #get max number of moves possible
  max_moves = math.ceil((1-imp_init)/imp_incr + 1)

  # Reverse the input range
  numbers = list(range(range_min, range_max + 1))[::-1]

  # Generate all combinations
  all_combinations = [list(comb) for i in range(1, max_moves + 1) for comb in combinations(numbers, i)]

  # Filter out combinations that don't end with range_min or don't have k numbers
  filtered_combinations = [comb for comb in all_combinations if (comb[-1] == range_min) or len(comb) == max_moves]

  return filtered_combinations


all_strategies = all_possible_strategies(range_min, range_max, imp_incr, imp_init)


def calculate_payoff_realprice(strategy, real_price, imp_incr, imp_init, value):
  payoff = 0
  last_imp = 0
  curr_imp = imp_init
  for i in range(len(strategy)):
    bid = strategy[i]
    if bid <= real_price:
      discount_factor = 1
      for j in range(i):
        discount_factor = discount_factor*(1-j*imp_incr)
      payoff += discount_factor*(bid-value)
      break
    if bid > real_price:
      last_imp = curr_imp
      curr_imp = last_imp+imp_incr
  return payoff

def calculate_expected_payoff(strategy, range_min, range_max, imp_incr, imp_init, value):
  expected_payoffs = []
  for real_price in range(range_min, range_max+1):
    expected_payoffs.append(calculate_payoff_realprice(strategy, real_price, imp_incr, imp_init, value))
  expected_payoffs.append(sum(expected_payoffs)/(range_max+1-range_min))
  return expected_payoffs

import pandas as pd

header = ["R"]
data = [list(range(range_min, range_max+1)) + ["total"]]
for strategy in all_strategies:
  header.append(str(strategy))
  data.append(calculate_expected_payoff(strategy, range_min, range_max, imp_incr, imp_init, value))

# Transpose the data
data = list(map(list, zip(*data)))
# Convert the data to a pandas DataFrame
df = pd.DataFrame(data, columns=header)

print(df.iloc[len(df)-1][1:].sort_values()[:15])