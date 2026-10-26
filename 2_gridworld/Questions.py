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
