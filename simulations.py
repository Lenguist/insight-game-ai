import random
from buyer import Buyer
from episode import Episode
import numpy as np

# imp_incr constant, max_price random
def basic_simulation(value, range_min, range_max, imp_incr, imp_init, rounds, seller, verbose=False):
  total_profit = 0
  round_cnt = 0
  for i in range(rounds):
    maxprice = int(random.uniform(range_min, range_max+1))
    buyer = Buyer(maxprice, imp_init, imp_incr)
    episode = Episode(buyer, seller, verbose=verbose)
    profit = episode.run_episode()
    total_profit += profit
  average_return = total_profit/rounds
  return average_return


# imp_incr random, max_price random
def random_imp_simulation(value, range_min, range_max, rounds, seller, verbose=False):
  # imp_init gonnna be 0 by default
  # imp_incr generated at random between 0 and 1
  total_profit = 0
  round_cnt = 0
  imp_init = 0
  imp_incr = random.choice([i / 10.0 for i in range(11)])
  for i in range(rounds):
    maxprice = int(random.uniform(range_min, range_max+1))
    buyer = Buyer(maxprice, imp_init, imp_incr)
    episode = Episode(buyer, seller, verbose=verbose)
    profit = episode.run_episode()
    total_profit += profit
  average_return = total_profit/rounds
  return average_return

# imp_incr normal around a given (or random) mean, max_price random
def normal_imp_simulation(value, range_min, range_max, rounds, seller, mean= random.choice([i / 10.0 for i in range(11)]), verbose=False):
  # imp_init gonnna be 0 by default
  # imp_incr generated at random between 0 and 1
  mean = random.choice([i / 10.0 for i in range(11)])
  variance = 0.2
  total_profit = 0
  round_cnt = 0
  imp_init = 0
  for i in range(rounds):
    imp_incr = list(np.random.normal(mean, variance, 1))[0]
    maxprice = int(random.uniform(range_min, range_max+1))
    buyer = Buyer(maxprice, imp_init, imp_incr)
    episode = Episode(buyer, seller, verbose=verbose)
    profit = episode.run_episode()
    total_profit += profit
  average_return = total_profit/rounds
  return average_return

# TO BE CODED
def normal_normal_simulation(value, range_min, range_max, rounds, seller, verbose=False):
  # choose middle at random, set variance the same
  # normal sample both maxprice and imp_init
  # benefits learningn agents
  # imp_init gonnna be 0 by default
  # imp_incr generated at random between 0 and 1
  total_profit = 0
  round_cnt = 0
  imp_init = 0
  imp_incr = random.choice([i / 10.0 for i in range(11)])
  for i in range(rounds):
    maxprice = int(random.uniform(range_min, range_max+1))
    buyer = Buyer(maxprice, imp_init, imp_incr)
    episode = Episode(buyer, seller, verbose=verbose)
    profit = episode.run_episode()
    total_profit += profit
  average_return = total_profit/rounds
  return average_return