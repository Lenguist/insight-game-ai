"Seller classes"
import random
import numpy as np
class Seller(object):
  def __init__(self, value, init_offer):
    self.value = value
    self.init_offer = init_offer
    self.state = {"last-offer": self.init_offer, "offers-made":0} # initial state
  def make_offer(self):
    raise NotImplementedError("Subclasses should implement this method.")
  def reset_state(self):
    self.state = {"last-offer":self.init_offer, "offers-made":0}
  def update_table(self):
    pass


class RandomSeller(Seller):
  def make_offer(self):
    offer = int(random.uniform(self.value+1, self.state["last-offer"])) # return random offer
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
  def __init__(self, value, init_offer, descent):
    super().__init__(value, init_offer)
    self.descent = descent
  def make_offer(self):
    offer = self.state["last-offer"]-self.descent
    return offer

class DescentArithmeticSeller(Seller):
  def __init__(self, value, init_offer, init_descent):
    super().__init__(value, init_offer)
    self.init_descent = init_descent
    self.descent = init_descent
  def make_offer(self):
    offer = self.state["last-offer"]-max(self.descent,1)
    self.descent = self.descent-1
    return offer
  def reset_state(self):
    super().reset_state()
    self.descent = self.init_descent

class QLearningSeller(Seller):
  def __init__(self, value, init_offer):
    super().__init__(value, init_offer)
    action_space_size = self.init_offer - self.value
    state_space_size = (self.init_offer - self.value) ^ 2
    self.q_table = np.zeros((state_space_size, action_space_size))

    # Q-Learning parameters
    self.learning_rate = 0.1
    self.discount_rate = 0.99
    self.exploration_rate = 1
    self.max_exploration_rate = 1
    self.min_exploration_rate = 0.01
    self.exploration_decay_rate = 0.001

  # start with just greedy implementation
  def make_offer(self):
    offer = np.argmax(self.q_table[self.state, :])
    return offer
  
  def update_table(self, offer, decision, new_state):
    if decision == 'accept offer':
      reward = offer - self.value
    else:
      reward = 0
    
    self.q_table[self.state, offer] = self.q_table[self.state, offer] * (1 - self.learning_rate) + \
                                  self.learning_rate * (reward + self.discount_rate * np.max(self.q_table[new_state, :]))