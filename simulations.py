import random
from buyer import Buyer
from episode import Episode

def simulation(value, range_min, range_max, imp_incr, imp_init, rounds, seller, verbose=False):
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