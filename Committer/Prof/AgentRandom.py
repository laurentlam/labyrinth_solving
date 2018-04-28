import random

class AgentRandom:
    """Votre description"""

    def __init__(self,name):
        """Initializes a new agent.
        """

        self.num_states = params['num_states']
        self.num_actions = params['num_actions']

    def startState(self, laby):
        """Start an episode with state 'initial_state', return first action
        Args:
            initial_state (int): The first states the agent makes
        Returns:
            The first action the agent performs
        """

        states=laby.initialStates();
        action = random.randint(0,self.num_actions-1) # Returns a random action

		return(states[0])

	def nextAction(self, laby):
        """One step of the agent in the reinforcement learning loop.

        Usually, this function will do two things:
        1) Use the reward to update values
        2) Call the agent's policy to determine the next action, given
           the state

        Args:
            reward (float): The reward recieved for performing the previous
                action in the previous state
            state : The state at the current time step
        Returns:
            The action returned for the state at the current time step
        """
        """The policy of an agent.

        In reinforcement learning, the policy returns an action, given the
        current state.

        Args:
            state : The state the agent is in.
        Returns:
            The action (int) the agent performs.
        """
        actions=laby.possibleActions();
		...
		return(actions[0])
