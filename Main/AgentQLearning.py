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

    def __init__(self,Epsilon,Lambda,Gamma,laby):

        """ initializes a new Qagent"""
        length=laby.length
        width = laby.width

        self.Quality=numpy.zeros((laby.width,laby.length,4))
        Quality = self.Quality.tolist()
        #Representing [N,E,S,W] Actions
        List_all_actions = [[0,1],[1,0],[0,-1],[-1,0]]
        current_position = laby.current_position
        for i in range(width):
            for j in range(length):
                laby.current_position = [i,j]
                for k in range(4):
                    if List_all_actions[k] in laby.possibleActions():
                        Quality[i][j][k] = 0
                    else:
                        Quality[i][j][k] = -10
        self.Quality = Quality
        laby.current_position = current_position
        self.Epsilon=Epsilon
        self.Lambda=Lambda
        self.Gamma = Gamma

    def startState(self, laby):
        """Start an episode with initial labyrinthe, return position of start
        Args:
            laby : The initial maze created
        Returns:
            The starting position of the agent
        """
        return(laby.current_position)

    def maxQuality(self,laby):

        """ returns (value,index(value) with best value for the current position in Quality matrix"""
        current_position=self.startState(laby)
        max_current_quality=max(self.Quality[current_position[0],current_position[1]])
        index_max_current_quality=self.Quality[current_position[0],current_position[1]].index(max_current_quality)
        return(max_current_quality,index_max_current_quality)

    def ChangeParameters(self,Epsilon,Lambda,Gamma,reward):
        Epsilon = 0.99*Epsilon
        Lambda = 0.99*Lambda
        current_position = self.startState(self.laby)
        self.Quality[current_position[0],current_position[1]]=Lambda*(reward+Gamma*maxQuality(self.laby)[0]+(1-Lambda)*self.Quality[current_position[0],current_position[1]])
        self.Epsilon=Epsilon
        self.Lambda=Lambda


    def nextAction(self,laby):
        """ returns a, next action. s'=a(s) """
        List_all_actions=[[0,1],[1,0],[0,-1],[-1,0]] #North,East,South,West
        #Possible actions in Quality Matrix
        actions = laby.possibleActions()
        random_value=random.random()

        if random_value<Epsilon:
            #Chosing random Action
            action = actions[random.randint(0,len(actions)-1)]

        else:
            #Chosing acute Action
            (max_current_quality,index_max_current_quality)=self.maxQuality(laby)
            #Going from index in Quality matrix to action
            action=List_all_actions[index_max_current_quality]

        if action in actions:
            return (action)

#Architecture
    #Creating quality matrix (size of environment)
    #Algorithm : Refreshing quality matrix step by step

        #Finding agent position (s)
        #Begin loop (condition : not arrived OR nb_steps<nb_steps_max)

            #CHOSING NEXT ACTION (nextAction method) : random and chosen depending on epsilon factor

            #Random value as 0<value<epsilon : Chosing random action from s position to (unknown) s' position
            #Random value as 1>value>epsilon : Chosing acute action from s position to s' position with best quality Q(s,s')

            #REFRESHING PARAMETERS AND QUALITY MATRIX : ChangeParameters() method

        #End of loop (Matrix should be complete and steady)

    #End of Algorithm
