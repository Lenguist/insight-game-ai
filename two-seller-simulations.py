#parallel selling
# params that are needed to initialize seller
value = 10
range_min = 11
range_max = 30
init_offer = range_max

n = int((init_offer-value)/2)

seller1 = RandomSeller(value=value, init_offer=init_offer)
seller2 = DescentArithmeticSeller(value=value, init_offer=init_offer, init_descent = n)
seller1_total_profit = 0
seller2_total_profit = 0
rounds = 5
for i in range(rounds):
  imp_init = 0
  imp_incr = random.choice([i / 10.0 for i in range(11)])
  maxprice = int(random.uniform(range_min, range_max+1))
  buyer = Buyer(maxprice, imp_init, imp_incr)
  episode1 = Episode(buyer, seller1, verbose=True)
  episode2 = Episode(buyer, seller2, verbose=True)
  print("RandomSeller")
  seller1_profit = episode1.run_episode()
  print("HeuristicSeller")
  seller2_profit = episode2.run_episode()
  print("\n")
  seller1_total_profit += seller1_profit
  seller2_total_profit += seller2_total_profit


def two_seller_negotiation(edubuyer, sellers):
  # assume 2 sellers
  terminate = False
  while not terminate:
    offers = [seller.make_offer() for seller in sellers]
    decisions = edubuyer.check_all_offers(offers)
    terminate = ("walk away" in decisions or "accept offer" in decisions)
    # this kind of a junky way to code it 
    # but it works for now
    for i, seller in enumerate(sellers):
      new_state = {"last-offer":offers[i],
                  "comp-last-offer":(offers[:i] + offers[i+1:])[0],
                  "offers-made":seller.state["offers-made"]+1}
      seller.state = new_state
  # get reward for the agents if terminated
  profits = [None for i in range(len(sellers))]
  for i, seller in enumerate(sellers):
    if decisions[i] == "accept offer":
      profits[i]=seller.state["last-offer"]-seller.value
    elif decisions[i] == "walk away":
      profits[i]=0
    elif decisions[i] == "competitor won":
      profits[i]=0
  return profits


import numpy as np
import matplotlib.pyplot as plt
def show_histogram(mean, stdev):
  num_samples = 1000
  samples_float = np.random.normal(mean, stdev, num_samples)
  samples = np.round(samples_float).astype(int)
  plt.hist(samples, bins=20, density=True)
  plt.show()

def sample_one_point(mean, stdev):
  num_samples = 1
  samples_float = np.random.normal(mean, stdev, num_samples)
  samples = np.round(samples_float).astype(int)
  return samples[0]