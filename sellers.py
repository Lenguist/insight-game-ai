"Seller classes"
import random
import numpy as np
import math
class Seller(object):
  def __init__(self, value, init_offer):
    self.value = value
    self.init_offer = init_offer
    self.state = {"last-offer": self.init_offer, "offers-made":0, "comp-last-offer":self.init_offer} # initial state
  def make_offer(self):
    raise NotImplementedError("Subclasses should implement this method.")
  def reset_state(self):
    self.state = {"last-offer":self.init_offer, "offers-made":0, "comp-last-offer":self.init_offer}
  def update_table(self, offer, decision, new_state):
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


class CompetitiveSeller(Seller):
  def __init__(self, value, init_offer):
    super().__init__(value, init_offer)
  def make_offer(self, last_opponent_offer, last_opponent_decrease):
    if last_opponent_offer == None:
      offer = self.init_offer
    else:
      offer = max(last_opponent_offer - (last_opponent_decrease+1), 10)
    return offer

class ReactiveSeller(Seller):
  def __init__(self, value, init_offer):
    super().__init__(value, init_offer)
  def make_offer(self, last_opponent_offer, last_opponent_decrease):
    if last_opponent_offer == None:
      offer = self.init_offer
    else:
      if last_opponent_decrease < 5:
        offer = max(last_opponent_offer - (last_opponent_decrease+1), 10)
      else:
        offer = self.value
    return offer

import random
from sellers import Seller
import numpy as np
import math

class OldQLearningSeller(Seller):
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
    self.exploration_rate = .01

    # # unused variables for a changing exploration rate
    # self.max_exploration_rate = 1
    # self.min_exploration_rate = 0.01
    # self.exploration_decay_rate = 0.001

  def make_offer(self):
    random_number = random.uniform(0, 1)
    if random_number > self.exploration_rate:
      #print(self.q_table[self.get_state_array_number(self.state), :])
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



import random
from sellers import Seller
import numpy as np
import math

class VanillaQLearningSeller(Seller):
  def __init__(self, value, init_offer, init_learning_rate,
                                        learning_rate_decay,
                                        exploration_decay_rate,
                                        min_exploration_rate):
    super().__init__(value, init_offer)
    self.q_table = {}
    self.total_offers_made = 0  # Add a new instance variable to keep track of the total number of offers made across all episodes

    # Q-Learning parameters
    self.discount_rate = 1 # no time discount bc limited rounds
    self.init_learning_rate = init_learning_rate
    self.learning_rate_decay = learning_rate_decay
    self.init_exploration_rate = 1.0  # Maximum exploration rate
    self.exploration_decay_rate = exploration_decay_rate  # Exponential decay rate for exploration probability
    self.min_exploration_rate = min_exploration_rate  # Minimum exploration rate

    self.exploration_rate = self.init_exploration_rate
    self.learning_rate = self.init_learning_rate


  def make_offer(self):
    state_tuple = (self.state['last-offer'], self.state['offers-made'])
    random_number = random.uniform(0, 1)
    if random_number > self.exploration_rate:
      # Check if state exists in q_table and if not, create it
      if state_tuple not in self.q_table:
          self.q_table[state_tuple] = {}
      # Get the action that has the highest q value
      offer = max(self.q_table[state_tuple], key=self.q_table[state_tuple].get, default=self.value+1)
    else: #exploring
      offer = random.randint(self.value+1,self.state['last-offer']-1)
    self.total_offers_made += 1  # Increment the total number of offers made every time an offer is made
    return offer

  def update_table(self, offer, decision, new_state):
    old_state_tuple = (self.state['last-offer'], self.state['offers-made'])
    new_state_tuple = (new_state['last-offer'], new_state['offers-made'])
    if decision == 'accept offer':
      reward = offer - self.value
    else:
      reward = 0

    # Ensure current state and new state are in the q_table
    if old_state_tuple not in self.q_table:
      self.q_table[old_state_tuple] = {}
    if new_state_tuple not in self.q_table:
      self.q_table[new_state_tuple] = {}

    old_value = self.q_table[old_state_tuple].get(offer, 0)
    max_new_state_value = max(self.q_table[new_state_tuple].values(), default=0)

    self.q_table[old_state_tuple][offer] = old_value * (1 - self.learning_rate) + \
      self.learning_rate * (reward + self.discount_rate * max_new_state_value)

  # returns a sequence of offers that constitutes optimal policy starting in state
  def get_optimal_policy(self, state):
      optimal_policy = []

      # Loop until a terminal state is reached or a state-action pair not in the Q-table is found
      while state in self.q_table and self.q_table[state]:
          action = max(self.q_table[state], key=self.q_table[state].get)
          optimal_policy.append((state, action))
          # Update state, assuming action results in a decreased 'last-offer' and increased 'offers-made'
          state = (action, state[1]+1)
      return optimal_policy

  # starts exploiting
  def set_exploiting(self):
    self.exploration_rate = 0

  # overwrites default reset state and updates lr rate
  # and exploration rate at the end of the episode
  def reset_state(self):
    super().reset_state()
    self.learning_rate = self.init_learning_rate / (1 + self.learning_rate_decay * self.total_offers_made)
    self.exploration_rate = self.min_exploration_rate + \
      (self.init_exploration_rate - self.min_exploration_rate) * \
      np.exp(-self.exploration_decay_rate * self.total_offers_made)
