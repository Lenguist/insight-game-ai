"Non-markov interaction"
class Interaction(object):
  def __init__(self, buyer, seller, verbose=True):
    self.buyer = buyer
    self.seller = seller
    self.verbose = verbose # whether to print info

  def negotiation_round(self):
    if self.verbose:
      print(f"The current buyer impatience is {self.buyer.imp}.")
    offer = self.seller.make_offer()
    decision = self.buyer.check_offer(offer)
    self.seller.save_round(offer, decision)
    if self.verbose:
      print(f"Seller made offer of {offer}. The buyer decided to {decision}")
    return decision

  def run_interaction(self):
    decision = ""
    while decision != "walk away" and decision != "accept offer":
      decision = self.negotiation_round()
    if decision == "accept offer":
      final_offer = self.seller.history[-1]["offer"]
      profit = final_offer - self.seller.value
      if self.verbose:
        print(f"Deal made at {final_offer}")
        print(f"Buyer's max_price was {self.buyer.maxprice}")
    else:
      if self.verbose:
        print(f"No deal made - no profit.")
      profit = 0
    return profit