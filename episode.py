class Episode(object):
  def __init__(self, buyer, seller, verbose=True):
    self.buyer = buyer
    self.seller = seller
    self.verbose = verbose # whether to print info

  def negotiation_round(self):
    if self.verbose:
      print(f"Curr state: {self.seller.state}")

    offer = self.seller.make_offer()
    decision = self.buyer.check_offer(offer)
    new_state = {"last-offer":offer, "offers-made":self.seller.state["offers-made"]+1}
    self.seller.update_table(offer, decision, new_state)
    self.seller.state = new_state

    if self.verbose:
      print(f"Seller made offer of {offer}. The buyer decided to {decision}")
    return decision

  def run_episode(self):
    decision = ""
    while decision != "walk away" and decision != "accept offer":
      decision = self.negotiation_round()

    if decision == "accept offer":
      final_offer = self.seller.state["last-offer"]
      profit = final_offer - self.seller.value
      if self.verbose:
        print(f"Deal made at {final_offer}")
        print(f"Buyer's max_price was {self.buyer.maxprice}")

    else:
      if self.verbose:
        print(f"No deal made - no profit.")
        print(f"Buyer's max_price was {self.buyer.maxprice}")
      profit = 0
    # reset seller state
    self.seller.reset_state()
    return profit