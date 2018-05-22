import numpy
import random
from environment import ENV
from environment import state

"""def QLearning(laby,width,length,Nb_episodes):
    Q = numpy.zero(WIDTH,LENGTH)
    for n in range(Nb_episodes):
        lambda = 1
        eps = 1
        init_state_list = laby.initialStates()
        state = init_state_list[0]
        for i in range
    """

class AgentQLearning:

    """ QLearning Agent"""

    def __init__(self,Epsilon,Lambda,laby):

        """ initializes a new Qagent"""

        self.Quality=numpy.zeros(laby.width,laby.length).tolist()
        self.Epsilon=Epsilon
        self.Lambda=Lambda

    def startState(self, laby):
        """Start an episode with initial labyrinthe, return position of start
        Args:
            laby : The initial maze created
        Returns:
            The starting position of the agent
        """
        return(laby.current_position)

    def ChangeQuality():


    def nextAction(self,laby,epsilon,lambda):
        #A tester
        actions = laby.possibleActions()
        random_value=random.random()

        if random_value<epsilon:
            #Chosing random Action
            action = actions[random.randint(0,len(actions)-1)]

        else:
            #Chosing acute Action
            current_position=self.startState(laby)
            current_position_indice=current_position[0]+width*current_position[1]
            #

        self.ChangeQuality()
        epsilon=0.99*epsilon
        Lambda=0.99*Lambda

        return (action)


#Architecture
    #Creating quality matrix (size of environment)
    #Algorithm : Refreshing quality matrix step by step

        #Finding agent position (s)
        #Begin loop (condition : not arrived OR nb_steps<nb_steps_max)

            #CHOSING NEXT ACTION (nextAction method) : random and chosen depending on epsilon factor

            #Random value as 0<value<epsilon : Chosing random action from s position to (unknown) s' position
            #Random value as 1>value>epsilon : Chosing acute action from s position to s' position with best quality Q(s,s')

            #REFRESHING PARAMETERS AND QUALITY MATRIX

            #Q(s,a)=L*(r+G*max(Q(s',a')) + (1-G)*Q(s,a))
            #Lambda=Lambda*0.99
            #Epsilon=Epsilon*0.99

            #Changing agent position (done in the main program, or the system program)

        #End of loop (Matrix should be complete and steady)

    #End of Algorithm
