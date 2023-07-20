# DO NOT CHANGE THE PARAMETERS LOCK THEM IN
from buyers import EducatedBuyer
import matplotlib.pyplot as plt
from sellers import DescentArithmeticSeller
from sellers import DescentByNSeller
from sellers import RandomSeller
range_min = 11
range_max = 100
value = 10
imp_incr = 0.1
rounds = 1000


init_offer = range_max

seller1 = QLearningSeller(value=value,
                         init_offer=init_offer,
                         init_learning_rate=0.75,
                         learning_rate_decay=0.001,
                         exploration_decay_rate=0.01,
                         min_exploration_rate=0.001)


seller2 = QLearningSeller(value=value,
                         init_offer=init_offer,
                         init_learning_rate=0.75,
                         learning_rate_decay=0.0011,
                         exploration_decay_rate=0.01,
                         min_exploration_rate=0.001,
                         other_seller=seller1)

# Add a reference to seller2 in seller1
seller1.other_seller = seller2

sellers = [seller1, seller2]

profits_seller1 = []
profits_seller2 = []

# Simulation of 100 rounds
for _ in range(100):
    total_profits = [0 for i in range(len(sellers))]
    for i in range(rounds):
        maxprice = int(random.uniform(range_min, range_max+1))
        edubuyer = EducatedBuyer(maxprice, imp_incr)
        profits = two_seller_negotiation(edubuyer, sellers, False)
        #print(qseller.q_table)
        for i in range(len(sellers)):
            total_profits[i] += profits[i] /rounds

    profits_seller1.append(total_profits[0])
    profits_seller2.append(total_profits[1])
print("Seller 1 average profits: " + str(sum(profits_seller1)/100))
print("Seller 2 average profits: " + str(sum(profits_seller2)/100))
print("Seller 1 policy:" + str(seller1.get_optimal_policy((100,0))))
print("Seller 2 policy:" + str(seller2.get_optimal_policy((100,0))))
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(profits_seller1, label='Q Seller 1')
ax.plot(profits_seller2, label='Random Seller')
ax.plot([profits_seller2[i]+profits_seller1[i] for i in range(len(profits_seller1))], label='Total')
#ax.axhline(45, color='r', linestyle='--', label='y=45 line')  # This will create a horizontal line at y=45
ax.set_xlabel('Time')
ax.set_ylabel('Average profit per round')
ax.set_title('Qseller vs Random')
ax.legend()
plt.show()