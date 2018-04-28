import random

class AgentRandom:
    """Votre description"""

    def __init__(self,name):
        """Initializes a new agent.
        """

    def startState(self, laby):
        """Start an episode with initial labyrinthe, return position of start
        Args:
            laby : The initial maze created
        Returns:
            The starting position of the agent
        """

        states=laby.initialStates();

		return(states[0])

	def nextAction(self, laby):
        """One step of the random agent

        Args:
            laby : The state at the current time step
        Returns:
            The action returned for the state at the current time step
        """

        state = laby.currentState();
        actions = laby.possibleActions();
        action = actions[random.randint(0,len(actions)-1)]; # Returns a random action

		return(action)
