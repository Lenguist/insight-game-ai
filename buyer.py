import random
"Buyer class for non-markov model"

class Buyer(object):
    def __init__(self, maxprice, imp, imp_incr):
        self.maxprice = maxprice
        self.imp = imp
    def check_offer(self, offer):
      random_number = random.uniform(0, 1)
      if random_number <= buyer.imp:
        return "walk away"
      elif offer <= maxprice:
        return "accept offer"
      else:
        self.imp += imp_incr
        return "reject but continue"