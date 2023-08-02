# insight-game-ai



INSIGHT (Intelligent Negotiation Strategy for Information Games
with Hidden Tactics) is the culmination of our research in the use of
reinforcement learning and game theory to create optimal bidding strategies in environments with hidden information.
The broader goal of this research was to devise strategies applicable to a wide variety of real-world
situations, such as trade negotiations, financial markets, and other bidding games.

We created a discrete Markov model to simulate bidding
episodes in which multiple sellers compete to maximize profit for each
buyer. INSIGHT combines different RL and heuristic strategies from existing research to learn over time the most profitable strategies in any
given situation. Then, we investigated how fine-tuning of parameters and
reward functions within the INSIGHT model affects its performance in
different scenarios, competing against opponents with a fixed stochastic
strategy, as well as opposing agents with reinforcement learning strategies.

Our results show that using this combination of strategies, we can create
sellers to outperform any given static opponent, but that two competing
Q-Learning sellers which both attempt to adapt to each other fail to co-
operate, thus resulting in low pareto efficiency. This mirrors a situation in
prisoner’s dilemma where both agents play based on the myopic strategy
of choosing only to defect, maximizing short term payoffs which eventu-
ally lead to a far worse outcome for both agents involved.

The INSIGHT model shows the powers and limitations of reinforcement learning for these
negotiation situations, and leaves room for a breadth of future research
involving other RL algorithms that could learn to cooperate.

Developed as part of 2023 summer Columbia Summer Undergraduate Research Experience in Math Modelling (CSUREMM)


Buyer: Hello! I wanted to buy this car. How much is it?
```
                              _.-="_-         _
                         _.-="   _-          | ||"""""""---._______     __..
             ___.===""""-.______-,,,,,,,,,,,,`-''----" """""       """""  __'
      __.--""     __        ,'                   o \           __        [__|
 __-""=======.--""  ""--.=================================.--""  ""--.=======:
]       [w] : /        \ : |========================|    : /        \ :  [w] :
V___________:|          |: |========================|    :|          |:   _-"
 V__________: \        / :_|=======================/_____: \        / :__-"
 -----------'  "-____-"  `-------------------------------'  "-____-"
```
* *you bought this car for 50 so you shouldn't sell cheaper* *

Buyer: What is your initial offer?
You: 55
Buyer: Okay, no, that's way too much. How about this car instead?
```

        __-------__
      / _---------_ \
     / /           \ \
     | |           | |
     |_|___________|_|
 /-\|                 |/-\
| _ |\       0       /| _ |
|(_)| \      !      / |(_)|
|___|__\_____!_____/__|___|
[_________|MEIN1|_________]
 ||||    ~~~~~~~~     ||||
 `--'                 `--'
```
Deal made at 30
buyer max price: 36
missed value: 6