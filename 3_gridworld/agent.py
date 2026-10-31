import util, random

class Agent:

  def getAction(self, state):
    """
    For the given state, get the agent's chosen
    action.  The agent knows the legal actions
    """
    abstract

  def getValue(self, state):
    """
    Get the value of the state.
    """
    abstract

  def getQValue(self, state, action):
    """
    Get the q-value of the state action pair.
    """
    abstract

  def getPolicy(self, state):
    """
    Get the policy recommendation for the state.

    May or may not be the same as "getAction".
    """
    abstract

  def update(self, state, action, nextState, reward):
    """
    Update the internal state of a learning agent
    according to the (state, action, nextState)
    transistion and the given reward.
    """
    abstract


class RandomAgent(Agent):
  """
  Clueless random agent, used only for testing.
  """

  def __init__(self, actionFunction):
    self.actionFunction = actionFunction

  def getAction(self, state):
    return random.choice(self.actionFunction(state))

  def getValue(self, state):
    return 0.0

  def getQValue(self, state, action):
    return 0.0

  def getPolicy(self, state):
    return 'random'

  def update(self, state, action, nextState, reward):
    pass



class ValueIterationAgent(Agent):
  def __init__(self, mdp, discount = 0.9, iterations = 100):
    """
    Your value iteration agent should take an mdp on
    construction, run the indicated number of iterations
    and then act according to the resulting policy.
    """
    self.mdp = mdp
    self.discount = discount
    self.iterations = iterations
    self.values = util.Counter()
    states = self.mdp.getStates()
    for i in range(iterations):
      values_iteration = util.Counter()
      for state in states:
        if self.mdp.isTerminal(state):
          values_iteration[state] = 0
        else:
          actions = self.mdp.getPossibleActions(state)
          values_iteration[state] = float('-inf')
          for action in actions:
            TSP = self.mdp.getTransitionStatesAndProbs(state, action)
            reward = 0
            for nextState, prob in TSP:
              estValue = self.values.getCount(nextState)
              immediate_reward =self.mdp.getReward(state, action, nextState)
              reward += prob * (immediate_reward + self.discount * estValue)
            values_iteration[state] = max(values_iteration[state], reward)
      self.values = values_iteration
    print("Start state value after {} iterations: {}".format(iterations, self.values.getCount(self.mdp.getStartState())))
  


  def getValue(self, state):
    """
    Look up the value of the state (after the indicated
    number of value iteration passes).
    """

    return self.values[state]



  def getQValue(self, state, action):
    """
    Look up the q-value of the state action pair
    (after the indicated number of value iteration
    passes).  Note that value iteration does not
    necessarily create this quantity and you may have
    to derive it on the fly.
    """
    TSP = self.mdp.getTransitionStatesAndProbs(state, action)
    reward = 0
    for nextState, prob in TSP:
      estValue = self.values.getCount(nextState)
      immediate_reward =self.mdp.getReward(state, action, nextState)
      reward += prob * (immediate_reward + self.discount * estValue)
    return reward



  def getPolicy(self, state):
    """
    Look up the policy's recommendation for the state
    (after the indicated number of value iteration passes).
    """
    actions = self.mdp.getPossibleActions(state)
    if len(actions) == 0:
      return None
    best_action = None
    best_value = float('-inf')
    for action in actions:
      q_value = self.getQValue(state, action)
      if q_value > best_value:
        best_value = q_value
        best_action = action
    return best_action
  



  def getAction(self, state):
    """
    Return the action recommended by the policy.
    """
    return self.getPolicy(state)


  def update(self, state, action, nextState, reward):
    """
    Not used for value iteration agents!
    """

    pass


################################################################################
# Below can be ignored for Exercise 2

class QLearningAgent(Agent):

  def __init__(self, actionFunction, discount = 0.9, learningRate = 0.1, epsilon = 0.2):
    """
    A Q-Learning agent gets nothing about the mdp on
    construction other than a function mapping states to actions.
    The other parameters govern its exploration
    strategy and learning rate.
    """
    self.setLearningRate(learningRate)
    self.setEpsilon(epsilon)
    self.setDiscount(discount)
    self.actionFunction = actionFunction

    raise "Your code here."




  # THESE NEXT METHODS ARE NEEDED TO WIRE YOUR AGENT UP TO THE CRAWLER GUI

  def setLearningRate(self, learningRate):
    self.learningRate = learningRate

  def setEpsilon(self, epsilon):
    self.epsilon = epsilon

  def setDiscount(self, discount):
    self.discount = discount

  # GENERAL RL AGENT METHODS

  def getValue(self, state):
    """
    Look up the current value of the state.
    """

    raise ValueError("Your code here.")



  def getQValue(self, state, action):
    """
    Look up the current q-value of the state action pair.
    """

    raise ValueError("Your code here.")



  def getPolicy(self, state):
    """
    Look up the current recommendation for the state.
    """

    raise ValueError("Your code here.")



  def getAction(self, state):
    """
    Choose an action: this will require that your agent balance
    exploration and exploitation as appropriate.
    """

    raise ValueError("Your code here.")



  def update(self, state, action, nextState, reward):
    """
    Update parameters in response to the observed transition.
    """

    raise ValueError("Your code here.")

  
####################################################


class PolicyIterationAgent(Agent):
  def __init__(self, mdp, discount=0.9, iterations=100):
      self.mdp = mdp
      self.discount = discount
      self.iterations = iterations
      self.values = util.Counter()
      self.policy = {}
      states = self.mdp.getStates()
      theta = 0.0000001

      for state in states:
          if not self.mdp.isTerminal(state):
              actions = self.mdp.getPossibleActions(state)
              if actions:
                  self.policy[state] = actions[0]
      for i in range(iterations):
        while True:
          delta = 0
          for state in states:
            if self.mdp.isTerminal(state):
              self.values[state] = 0
              continue
            action = self.policy[state]
            old_value = self.values.getCount(state)
            new_value = self.getQValue(state,action)
            self.values[state] = new_value
            delta = max(delta, abs(old_value - new_value))
          if delta < theta:
            break
          

