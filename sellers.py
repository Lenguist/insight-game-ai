class Seller(object):
  def __init__(self, value, imp_init, init_offer):
    self.value = value
    self.imp_init = imp_init
    self.init_offer = init_offer
    self.state = {"last-offer": self.init_offer, "imp":self.imp_init} # initial state
  def make_offer(self):
    raise NotImplementedError("Subclasses should implement this method.")
  def reset_state(self):
    self.state = {"last-offer":self.init_offer, "imp":self.imp_init}

class RandomSeller(Seller):
  def make_offer(self):
    offer = int(random.uniform(value+1, self.state["last-offer"])) # return random offer
    return offer

class DescentByOneSeller(Seller):
  def make_offer(self):
    offer = self.state["last-offer"]-1
    return offer

class UserInputSeller(Seller):
 def make_offer(self):
  offer = int(input("You: "))
  return offer

class DescentByNSeller(Seller):
  def __init__(self, value, imp_init, init_offer, descent):
    super().__init__(value, imp_init, init_offer)
    self.descent = descent
  def make_offer(self):
    offer = self.state["last-offer"]-self.descent
    return offer

class DescentArithmeticSeller(Seller):
  def __init__(self, value, imp_init, init_offer, init_descent):
    super().__init__(value, imp_init, init_offer)
    self.init_descent = init_descent
    self.descent = init_descent
  def make_offer(self):
    offer = self.state["last-offer"]-max(self.descent,1)
    self.descent = self.descent-1
    return offer
  def reset_state(self):
    super().reset_state()
    self.descent = self.init_descent