import random

# Buyer for one seller scenario
# First we check walking away, then accept/reject offer
# Accepts offer if lower or equal max
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

# Buyer for two or more sellers
# Checks walk away, then each available offer, then accept/reject
#buyer for two or more sellers
class EducatedBuyer(object):
    def __init__(self, max_price, imp_incr):
        self.max_price = max_price
        self.imp = 0
        self.imp_incr = imp_incr

    def check_all_offers(self, offers):
        decisions = [] # saves decision for each offer
        accept_indices = [] # saves indices of accepted offers
        accept_values = [] # saves values of accepted offers

        random_number = random.uniform(0, 1)
        if random_number <= self.imp:
            for i in range(len(offers)):
                decisions.append("walk away")
        else:
            for i, offer in enumerate(offers):
                if offer <= self.max_price:
                    decisions.append("accept offer")
                    accept_indices.append(i)
                    accept_values.append(offer)
                else:
                    decisions.append("reject but continue")

        # if more than one offer is accepted
        # NEED OT CHANGE REJECT BUT CONTINUE TO COMPETITOR WON OUT IF THERE ARE ANY ACCEPTS AT ALL
        if len(accept_indices) > 0:
            min_value = min(accept_values)
            min_indices = [i for i, value in zip(accept_indices, accept_values) if value == min_value]

            if len(min_indices) > 1:
                # randomly choose an offer to accept if there are multiple offers with the minimum value
                accept_index = random.choice(min_indices)
            else:
                # if there is a unique minimum, accept it
                accept_index = min_indices[0]
            for idx in range(len(decisions)):
              if idx == accept_index:
                decisions[idx] = "accept offer"
              else:
                decisions[idx] = "competitor won"

        self.imp += self.imp_incr
        return decisions

