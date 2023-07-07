"Seller classes"
import random
import numpy as np
import math
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
    if offer>self.value+1:
      return offer
    else:
      return self.value+1
    return offer
  def reset_state(self):
    super().reset_state()
    self.descent = self.init_descent


class QLearningSeller(Seller):
  def __init__(self, value, init_offer):
    super().__init__(value, init_offer)
    action_space_size = self.init_offer - self.value
    state_space_size = (self.init_offer - self.value) ** 2
    self.q_table = np.zeros((state_space_size, action_space_size))

    # Q-Learning parameters
    # alpha
    self.learning_rate = 0.1
    # gamma
    self.discount_rate = 0.99
    # exploration rate for when the model is still learning
    self.exploration_rate = .15

    # # unused variables for a changing exploration rate
    # self.max_exploration_rate = 1
    # self.min_exploration_rate = 0.01
    # self.exploration_decay_rate = 0.001

  def make_offer(self):
    random_number = random.uniform(0, 1)
    if random_number > self.exploration_rate:
      offer = np.argmax(self.q_table[self.get_state_array_number(self.state), :]) + (self.value+1)
    else: #exploring
      offer = random.randint(self.value+1,self.state['last-offer']-1)
    return offer

  def update_table(self, offer, decision, new_state):
    if decision == 'accept offer':
      reward = offer - self.value
    else:
      reward = 0    
    state_array_number = self.get_state_array_number(self.state)
    new_state_array_number = self.get_state_array_number(new_state)
    self.q_table[state_array_number, offer-(self.value+1)] = self.q_table[state_array_number, offer-(self.value+1)] * (1 - self.learning_rate) + \
                                  self.learning_rate * (reward + self.discount_rate * np.max(self.q_table[new_state_array_number, :]))
  
  # helper methods
  def get_state_array_number(self, state):
    return state['last-offer']-(self.value+1)+(self.init_offer-self.value)*state['offers-made']

  def from_array_num_get_state(self, array_num):
    offers_made = math.floor(array_num/(self.init_offer-self.value))
    last_offer =  array_num % (self.init_offer-self.value) + (self.value + 1)
    return {"last-offer":last_offer, "offers-made":offers_made}
  
  def set_exploiting(self):
    self.exploration_rate = 0
