# Question 3

# (b) How many rounds of policy iteration are needed before the start state of MazeGrid becomes non-zero? What happens if you switch off the noise (-n 0,0)?

# <Answer>
# - With default noise: It takes 1 round of polic iteration for the start state value to become non-zero (~0.0003 at iteration 1)
# - Without noise (-n 0.0): It takes 6 rounds of policy iteration for the start state value to become non-zero (~0.3874 at iteration 6)



# (c) How many iterations of policy iteration do we need for the algorithm to converge to an optimal policy? Also try without noise.

# <Answer>
# - With default noise: The algorithm converges to an optimal policy after a total of 2 iterations.
# - Without noise (-n 0.0): The algorithm converges after a total of 8 iterations. Removing noise changes the transition dynamics, resulting in more rounds required to reach stability and convergence.



# (d) Compared with value iteration, what are the advantages and disadvantages of policy iteration? Give a detailed list of the pros and cons.

# <Answer>
# 1. Policy Iteration
# - Pros: The policy converges to the optimal one in very few outer iterations. It also has a clear stopping criterion: it terminates when the policy no longer changes (policy_stable == True). 
# - Cons: Each round requires heavy computation per iteration, because internal policy evaluation cost is high. In large environments, this can lead to performance bottlenecks.

# 2. Value Iteration
# - Pros: Each iteration (sweep) is cheap and the implementation is simple. It only repeats the Bellman optimality update, with no separate policy evaluation loop and no need to store a policy during the run.
# - Cons: It often takes more total iterations to fully converge to the optimal policy. It also has no clear stopping point: you have to choose a threshold or a fixed number of iterations yourself. The policy is not available during the run, so you only get it at the end by extracting it from the values.