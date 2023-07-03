import random
"Seller classes for non-markov model"

class Seller(object):
  def __init__(self, value):
    self.value = value
    self.history = []
  def make_offer(self):
    raise NotImplementedError("Subclasses should implement this method.")
  def save_round(self, offer, decision):
    self.history.append({"offer":offer, "decision":decision})

class DescentByOneSeller(Seller):
  def __init__(self, value, init_offer):
    super().__init__(value)  # Call to parent's __init__ method
    self.init_offer = init_offer
  def make_offer(self):
    if len(self.history)==0:
      offer = self.init_offer
    else:
      offer = self.history[-1]["offer"]-1
    return offer


class UserInputSeller(Seller):
 def make_offer(self):
  offer = int(input("You: "))
  return offer