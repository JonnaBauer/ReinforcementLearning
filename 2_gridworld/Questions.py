# How many rounds of value iteration are needed before the start state of
# MazeGrid becomes non-zero? Why?

# Answer: 10 rounds of value iteration are needed before the start state 
# of MazeGrid becomes non-zero. This is because the start state is 10 steps 
# away from the terminal state, and the value of a state is determined 
# by the expected return from that state, which depends on the values of its successor states,
# so only when we have propagated the values from the terminal state back to the start state
# the start state will have a non-zero value.

# Consider the policy computed on BridgeGrid with the default discount of
# 0.9 and the default noise of 0.2. Which one of these two parameters must
# we change before the agent dares to cross the bridge, and to what value?

# Answer: We must change the noise parameter to a lower value,
# ideally 0.0 but 0.02 also works.

# (c) On the DiscountGrid, give parameter values which produce the following
# optimal policy types or state that they are impossible:
# (a) Prefer the close exit (+1), risking the cliff (-10)
# d = 0.1, n = 0.0
# (b) Prefer the close exit (+1), but avoiding the cliff (-10)
# d = 0.3, n = 0.7
# (c) Prefer the distant exit (+10), risking the cliff (-10)
# d = 0.9, n = 0.0
# (d) Prefer the distant exit (+10), avoiding the cliff (-10)
# d = 0.9, n = 0.2
# (e) Avoid both exits (also avoiding the cliff)
# Impossible

# (d) On the MazeGrid, with the default parameters, compare the value estimate
# of the start state after 100 iterations of value iteration to the empirical
# returns E[Gt] as you computed in the last exercise (-k 10 -q, and -k 10000
# -q). Report the numbers. Why do you get different results?

# Start state value after 100 iterations: 0.2821949143875512
# Empirical returns E[Gt] after 10 episodes: 9.431847614933533e-08
# Empirical returns E[Gt] after 10000 episodes: 0.00219593109788294

# We get different results because the value iteration estimates
# the optimal value by choosing actions that would mazimize expected
# future rewards, while the empirical returns are based on the random
# policy.