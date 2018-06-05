#Import needed modules
import numpy

#Import all agents from agent files:
from AgentQLearning import AgentQLearning
from AgentRandom import AgentRandom

#Import environment class
from environment import ENV
from environment import state

class Agent:

    """ General class for agent : attribute is an agent, unique method is nextAction."""

    def __init__(self,agent_name,arguments):

        """ General class for agent : contains an agent with its specific arguments  """

        if arguments!=None:
            self.agent=agent_name(*arguments)
        else:
            self.agent=agent_name()


    def nextAction(self,laby):

        """This method finds the nextAction according to the specific agent (self.agent) we use
        There it means the nextAction() method of our specific agent (self.agent) is used"""

        return self.agent.nextAction(laby)


    def updatePolicy(self,reward,laby,action,position):

        """ This method updates the policy of the agent at a certain position, considering a given reward"""
        agent_name=self.agent
        agent_name.updatePolicy(reward,laby,action,position)
        self.agent=agent_name


#TESTING

if __name__=="__main__":
    SIZE=10
    laby=ENV(SIZE,SIZE,numpy.zeros((SIZE,SIZE)),[0,0])
    laby.create_random_environment()

    #testing all agents:

    #test with AgentRandom
    Random_agent_class=Agent(AgentRandom,None)
    print("\n General Agent Class: \n",Random_agent_class)
    print("\n attributes of agent class :\n",vars(Random_agent_class))
    print("\n next action:\n",Random_agent_class.nextAction(laby))

    #test with AgentQLearning
    Epsilon=1
    Lambda=1
    Gamma=0.3
    #There will be a problem here because "arguments" is multiple objects
    QLearning_agent_class=Agent(AgentQLearning,[Epsilon,Lambda,Gamma,laby])
    print("\n General Agent Class: \n",QLearning_agent_class)
    print("\n attributes of agent class :\n",vars(QLearning_agent_class))
    print("\n next action:\n",QLearning_agent_class.nextAction(laby))
