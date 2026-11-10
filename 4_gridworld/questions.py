# Question 2.1

# (a) How are the learned values different from those learned by value iteration(previous exercise) and shown in Fig. 1, and why? How can you make them closer to the optimal values?

# Q-learning result splits sells into four Q-values for each action. 
# Near the goal, Q-values came close to optimal but distant states like the start area stayed low or unvisited because 100 episodes weren't enough sampling.
# So, to get optimal values, we need to get more training episodes.

# (b) How do the learned q-values compare to those of the value iteration agent (see Fig. 2)? Why will your agent usually not learn the optimal policy?

# Value Iteration computes the optimal policy directly while Q-learning takes random steps.
# This random exploration often leads to big penalties, which discourages the agent from trying the best path.

# (c) Train your Q-learner on the CliffGrid for 300 episodes. Compare the value it learns for the start state with the average returns from the training episodes (printed out automatically). Why are they so different?

# AVERAGE RETURNS FROM START STATE for Cliffgird: -29.775767456143047
# AVERAGE RETURNS FROM START STATE for Mazegrid: 0.15711442949003993
# Training return is lower than the start state value because ε-greedy exploration sometimes causes falls off the cliff.
