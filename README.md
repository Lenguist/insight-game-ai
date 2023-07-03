# insight-game-ai
Repository for the code developed for summer 2023 CSUREMM workshop


The Simple Simulation

Rules: There is a Seller (Agent) who interacts with a Buyer (environment) trying to sell a car.
The car has intrinsic value to the seller which is modelled with a variable value. Any price higher than value will constitute a profit for the Seller.
The Buyer has some max price they are willing to pay for the car. This value is generated from a uniform random distribution in the range of (range_min, range_max).
This range is known to the Seller. After the Buyer max price is set it will not change over the course of the episode.
The Seller makes repeated offers to the Buyer and the Buyer will either accept the offer (if it is below maximum price) or reject it.
Every time the Seller makes an offer Buyer get more impatient and they are more likely to walk away from the deal entrirely.
This is modelled by the Buyer having some probability to walk (impatience) evaluated at the beginning of each round.
Impatience is incremented each round by a constant amount known to the Seller. The initial impatience is always 0.

The goal of the Seller agent is to maximize average expected return for a random buyer.


Variables:
value - constant across episodes, known to the Agent
range_min, range_max - constant across episodes, known to the Agent
Buyer's max_price - generated uniformly random from range_min, range_max at the beginning of each episode
imp_incr - constant across episodes, known to the Agent
imp_init - assumed to always be 0

Prices are assumed to be discretized as integers.

Future complications to the model are immediately obvious from writing out the variables.
1. buyer max_price can be generated using a different known distribution
2. buyer max_price can be generated using an unknown distribution
3. imp_incr can be be non-constant, or hidden from the Seller
4. imp_init can differ to account for Buyer variability
We will discover which of those complications are informative in the process of experimentation.

After we experiment with those the next step would be to allow Buyer to make bids, limit the supply of vehicles, introduce competition with another Seller,
and make Buyer behaviour incrasingly more complex (bluffs, urgency, etc)

QUESTION: shouldn't the number of cars be constant? aka there is incentive to keep the car if the car supply is limited


code is structured in the following way. First, we initialize a Simulation with a certain value, range_min, range_max, imp_incr and imp_init.
after that, we initialize an Interaction which constitutes to a single negotiation. That will include a Buyer max_price which will be generated according to simulaiton rules.

Markov assumption states that the past doesn't affect the present - all information relevant to decision making is contained in the "state"
To this end we will modify our original agents to have access to state rather than history
State will encapsulate the current impatience, and the current
