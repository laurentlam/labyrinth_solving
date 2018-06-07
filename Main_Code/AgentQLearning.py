import numpy
import random
from environment import ENV
from environment import state

#For tests
from system import System

class AgentQLearning:

    """ QLearning Agent
    Agent evolves within the maze in accordance with QLearning algorithms.
    """


    #Init is tested in the testing question
    def __init__(self,Epsilon,Lambda,Gamma,laby):

        """ Initializes a new Qagent : Quality Matrix and parameters Epsilon, Lambda, Gamma """

        #Quality matrix :
        length=laby.length
        width=laby.width

        #Creating quality matrix (size of environment) : every direction is possible at first

        dt = numpy.dtype([('North', numpy.int),('East', numpy.int),('South', numpy.int),('West', numpy.int)])
        self.Quality=numpy.zeros((laby.width,laby.length),dt)

        #Note for the type of the Matrix :

            #Numpy array of shape length*width
            #Each element is a 4-array of numpy.int type

            #To get to the Quality_list of the position (x,y), do self.Quality[x,y]
            #Example : self.Quality[x,y]=(0,0,0,0) at first

        #Representing [N,E,S,W] Actions (careful: usual x,y is not i,j)
        List_all_actions = [[-1,0],[0,1],[1,0],[0,-1]]
        #We put huge negative value in impossible actions, to treat them differently in the process.
        for i in range(width):
            for j in range(length):
                #We create the following variable not to go in laby 4 time for the same thing.
                possible_actions_ij=laby.possibleActions([i,j])
                for k in range(4):
                    if List_all_actions[k] in possible_actions_ij:
                        self.Quality[i,j][k] = 0
                    else:
                        self.Quality[i,j][k] = -1e6

        self.Epsilon=Epsilon
        self.Lambda=Lambda
        self.Gamma = Gamma


    def maxQuality(self,position):

        """ Returns (value,index(value)) with best value for the given position in Quality matrix. """

        [i,j]=position
        List_all_actions = [[-1,0],[0,1],[1,0],[0,-1]] #North,East,South,West
        Quality=self.Quality

        # Finding maximum quality with its (possibly multiple) index
        max_current_quality=Quality[i,j][0]
        index_max_current_quality=[0]
        for k in range(1,4):
            if max_current_quality<Quality[i,j][k]:
                max_current_quality=Quality[i,j][k]
                index_max_current_quality=[k]
            elif max_current_quality==Quality[i,j][k]:
                index_max_current_quality.append(k)

        return [max_current_quality,index_max_current_quality[random.randint(0,len(index_max_current_quality)-1)]]
        # Index of maximum quality is chosen randomly in all possible indexes of max Quality
        # in order to add discovery where multiple routes are possible for the agent.

    def nextAction(self,laby):

        """
        Returns a, the next action so as s'=a(s), where s' is the next state and s is the current state in the maze.
        Next Action is chosen wether randomly or with best possible quality for the action.
        """

        [i,j]=laby.current_position #attribute is used multiple times so we call it once
        # Possible actions in Quality Matrix
        possible_actions = laby.possibleActions([i,j])

        # Error case : no action is possible (the maze is not well built)
        if possible_actions==[]:
            print("No possible action (in nextAction)")
            #print(laby.show())
            return None

        # Playing random : whether it's discovery (random wandering in the maze), or it's driven by Quality maximum
        random_value=random.random()

        if random_value<self.Epsilon:
            # Chosing random Action : wandering in the maze
            action = possible_actions[random.randint(0,len(possible_actions)-1)]

        else:
            # Chosing acute Action : driven by Quality maximum

            index_max_current_quality=self.maxQuality([i,j])[1]

            # Going from index in Quality matrix to action
            List_all_actions = [[-1,0],[0,1],[1,0],[0,-1]] # North,East,South,West
            action=List_all_actions[index_max_current_quality]



        if action in possible_actions:
            return action
        else:
            print("\n Error : invalid action (in nextAction)\n")
            print(" possible actions :\n", possible_actions)
            return None


    def ChangeParameters(self,reward,laby,action,position):

        """
        This method changes Epsilon, Lambda
        and the Quality of the transition from actual position of the agent
        to the next position (given by the action)

        NB : we chose an arbitrary position in arguments instead of actual position of the agent
        to change the parameters AFTER moving the agent (ancient position would have been lost otherwise).
        """


        [i,j]=position

        # Error case : given action is not a possible action
        if action not in laby.possibleActions([i,j]):
            print("Error : invalid action (in ChangeParameters)\n")
            print("possible actions:\n",laby.possibleActions([i,j]))
            print("action :",action)
            return None

        List_all_actions = [[-1,0],[0,1],[1,0],[0,-1]] #North,East,South,West
        action_index=List_all_actions.index(action)


        next_position=laby.next_position([i,j],action)
        max_quality=self.maxQuality(next_position)[0]
        self.Quality[i,j][action_index]=self.Lambda*(reward+self.Gamma*max_quality)+(1-self.Lambda)*self.Quality[i,j][action_index]

        #self.Epsilon = 0.99*self.Epsilon
        self.Lambda = 0.99*self.Lambda


#TESTING

if __name__=="__main__":

    SIZE=10
    Epsilon=1
    Lambda=1
    Gamma=0.3
    laby=ENV(SIZE,SIZE,numpy.zeros((SIZE,SIZE)),[0,0])
    laby.create_random_environment()

    #__init__()
    qlearning_agent=AgentQLearning(Epsilon,Lambda,Gamma,laby)
    # print(vars(agent_qlearning))
    [i,j]=laby.current_position
    print("\n current position: \n",[i,j])
    print("\n Quality at current position:\n",qlearning_agent.Quality[i,j])

    #maxQuality()
    # for k in range(SIZE):
    #     for l in range(SIZE):
    #         print("\n chosen position :\n",[k,l])
    #         print("\n Associated quality matrix :\n",agent_qlearning.Quality[k,l])
    #         print("value and index of maximum Quality for the chosen position",agent_qlearning.maxQuality([k,l]))

    #nextAction() -->Problem when algorithm has started
    #laby.show()
    next_action=qlearning_agent.nextAction(laby)
    print("next action is: ",next_action)

    #ChangeParameters()
    [i,j]=laby.current_position
    next_action=qlearning_agent.nextAction(laby)
    #print("Quality at current position, Epsilon, Lambda :",qlearning_agent.Quality[i,j],qlearning_agent.Epsilon,qlearning_agent.Lambda)

    next_position=laby.next_position(next_action)
    reward=state(laby.State(next_position)).reward()
    #print("reward of next state:\n",reward)

    qlearning_agent.ChangeParameters(reward,laby,next_action)
    #print("Changing parameters...\n")
    #print("Quality at current position, Epsilon, Lambda : ",qlearning_agent.Quality[i,j],qlearning_agent.Epsilon,qlearning_agent.Lambda)
