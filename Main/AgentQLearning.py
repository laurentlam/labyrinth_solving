import numpy
import random
from environment import ENV
from environment import state

class AgentQLearning:

    """ QLearning Agent"""


    #There will be a problem with General Agent Class here because "arguments" is one object only
    def __init__(self,Epsilon,Lambda,Gamma,laby):

        """ initializes a new Qagent : Quality Matrix and parameters Epsilon, Lambda, Gamma"""
        #Quality matrix :
        length=laby.length
        width=laby.width
        #Creating quality matrix (size of environment) : every direction is possible at first
        self.Quality=numpy.zeros((laby.width,laby.length,4))

        # Quality = self.Quality.tolist()

        #Representing [N,E,S,W] Actions
        List_all_actions = [[0,1],[1,0],[0,-1],[-1,0]]
        #We put strictly negative quality in impossible actions, knowing they won't become positive in the process.
        for i in range(width):
            for j in range(length):
                #We create the following variable not to go in laby 4 time for the same thing.
                possible_actions_ij=laby.possibleActions([i,j])
                for k in range(4):
                    if List_all_actions[k] in possible_actions_ij:
                        self.Quality[i][j][k] = 0
                    else:
                        self.Quality[i][j][k] = -10
        # self.Quality = Quality
        self.Epsilon=Epsilon
        self.Lambda=Lambda
        self.Gamma = Gamma

    #StartState is not useful anymore since current_position is an attribute of laby.
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
        #amax,argmax
        current_position=self.startState(laby)
        Quality=self.Quality
        max_current_quality=Quality[current_position[0]][current_position[1]][0]
        index_max_current_quality=0
        for i in range(1,4):
            if max_current_quality<Quality[current_position[0]][current_position[1]][i]:
                max_current_quality=Quality[current_position[0]][current_position[1]][i]
                index_max_current_quality=i
        return([max_current_quality,index_max_current_quality])




    def nextAction(self,laby):
        """ returns a, next action. s'=a(s) """
        List_all_actions=[[0,1],[1,0],[0,-1],[-1,0]] #North,East,South,West
        #Possible actions in Quality Matrix
        actions = laby.possibleActions(laby.current_position)
        random_value=random.random()

        if random_value<self.Epsilon:
            #Chosing random Action
            action = actions[random.randint(0,len(actions)-1)]

        else:
            #Chosing acute Action
            (max_current_quality,index_max_current_quality)=self.maxQuality(laby)
            #Going from index in Quality matrix to action
            action=List_all_actions[index_max_current_quality]

        if action in actions:
            return (action)


    #STILL TO CHANGE
    def ChangeParameters(self,reward,laby,action_index):
        # current_position = self.startState(laby)
        current_position=laby.current_position
        max_current_quality=self.maxQuality(laby)[0]
        self.Quality[current_position[0]][current_position[1]][action_index]=self.Lambda*(reward+self.Gamma*max_current_quality[0]+(1-self.Lambda)*self.Quality[current_position[0][current_position[1]][action_index])
        self.Epsilon = 0.99*self.Epsilon
        self.Lambda = 0.99*self.Lambda


#Architecture
    #Algorithm : Refreshing quality matrix step by step

        #Finding agent position (s)
        #Begin loop (condition : not arrived OR nb_steps<nb_steps_max)

            #CHOSING NEXT ACTION (nextAction method) : random and chosen depending on epsilon factor

            #Random value as 0<value<epsilon : Chosing random action from s position to (unknown) s' position
            #Random value as 1>value>epsilon : Chosing acute action from s position to s' position with best quality Q(s,s')

            #REFRESHING PARAMETERS AND QUALITY MATRIX : ChangeParameters() method


#TESTING

if __name__=="__main__":
    SIZE=10
    Epsilon=1
    Lambda=1
    Gamma=0.3
    laby=ENV(SIZE,SIZE,numpy.zeros((SIZE,SIZE)),[0,0])
    laby.create_random_environment()

    #__init__()
    agent_qlearning=AgentQLearning(Epsilon,Lambda,Gamma,laby)
    # print(vars(agent_qlearning))
