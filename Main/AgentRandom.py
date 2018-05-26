import random
from environment import ENV
from environment import state
class AgentRandom:

    """Naive agent with pure random behaviour"""

    def __init__(self):
        """ initializes a new random agent"""


    def startState(self, laby):
        """Start an episode with initial labyrinthe, return position of start
        Args:
            laby : The initial maze created
        Returns:
            The starting position of the agent
        """
        return(laby.current_position)

    def nextAction(self, laby):
        """One step of the random agent
        Args:
            laby : The state at the current time step
        Returns:
            The action returned for the state at the current time step
        """

        state = laby.currentState()
        current_position=laby.current_position
        actions = laby.possibleActions(current_position)
        action = actions[random.randint(0,len(actions)-1)] # Returns a random action

        return(action)

    def updatePolicy():

        """ This method changes the policy of a general agent (according to the General Agent Class)
        Here the policy is constant (random)"""

#TESTING

if __name__=="__main__":

    agent_random=AgentRandom()
