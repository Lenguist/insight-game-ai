import random

class Buyer(object):
    def __init__(self, maxprice, imp_init, imp_incr):
        self.maxprice = maxprice
        self.imp = imp_init
        self.imp_incr = imp_incr
    def check_offer(self, offer):
      random_number = random.uniform(0, 1)
      if random_number <= self.imp:
        return "walk away"
      elif offer <= self.maxprice:
        return "accept offer"
      else:
        self.imp += self.imp_incr
        return "reject but continue"