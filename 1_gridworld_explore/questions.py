# Implement the computation of the return of an episode in gridworld.py, see
# runEpisode function, and the computation of the estimated value of the start
# state (see main function) and # Exercise 1 comments. Consult the slide on
# the Value Function (number 54). 

# (a) What is the value of the start state in the MazeGrid environment for the
# random policy (default discount factor γ = 0.9). Try different number
# of episodes (use -k xxxx -q) and provide mean value and the standard
# deviation over the episodes. Try also k = 10000.

#k |  Mean | Std
#1 | 0.00785516721127895 | 0.0
#100| 0.0035480765654269768 | 0.015278325436963286
#1000| 0.0017339617506245207 | 0.009312737450632706
#10000 |0.002195931097882947 | 0.012729533343982668

# (b) How many episodes do you need to be sure (confidence 95%) that your
# mean estimate is within ±0.0004 of the true mean?

z = 1.96
std = 0.012729533343982668
E = 0.0004

n = (z * std / E) ** 2
print(n)

# We need 3891 episodes to be sure (confidence 95%) 
# that our mean estimate is within ±0.0004 of the true mean.

# Hint:2
# (c) Do the same with the DiscountGrid for a discount γ = 0.95. How many
# episodes do you need to be sure (confidence 95%) that your mean estimate
# is within ±0.1 of the true mean?

# K = 10000 gave us
# Mean = -6.3922884053569184
# std = 3.781327443263696

z = 1.96
std = 3.781327443263696
E = 0.1

n = (z * std / E) ** 2
print(n)

# We need 5493 episodes to be sure (confidence 95%)
# that our mean estimate is within ±0.1 of the true mean.


# C.T.T assume 2 