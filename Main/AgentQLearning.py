import numpy
import random
from environment import ENV
from environment import state

class AgentQLearning:

    """ QLearning Agent"""


    #Init is tested in the testing question
    def __init__(self,Epsilon,Lambda,Gamma,laby):

        """ initializes a new Qagent : Quality Matrix and parameters Epsilon, Lambda, Gamma"""

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
        #We put strictly negative quality in impossible actions, to treat them differently in the process.
        for i in range(width):
            for j in range(length):
                #We create the following variable not to go in laby 4 time for the same thing.
                ######### print("i,j=:\n",i,j)
                possible_actions_ij=laby.possibleActions([i,j])
                ######### print("\n possible_actions:\n",possible_actions_ij)
                ######### print("\n List_all_actions\n",List_all_actions)
                for k in range(4):
                    ######### print("\n Une matrice de QUALITE (AVANT):\n",self.Quality[i,j])
                    if List_all_actions[k] in possible_actions_ij:
                        self.Quality[i,j][k] = 0
                    else:
                        self.Quality[i,j][k] = -10
                    ######### print("\n Une matrice de QUALITE (APRES):\n",self.Quality[i,j])

        self.Epsilon=Epsilon
        self.Lambda=Lambda
        self.Gamma = Gamma

    # def maxQuality(self,laby): #We chose to use an arbitrary position instead of the current position
    def maxQuality(self,position):

        """ returns (value,index(value)) with best value for the position in Quality matrix"""

        #amax,argmax
        # [i,j]=self.startState(laby)
        [i,j]=position
        Quality=self.Quality

        max_current_quality=Quality[i,j][0]
        index_max_current_quality=0
        for k in range(1,4):
            if max_current_quality<Quality[i,j][k]:
                max_current_quality=Quality[i,j][k]
                index_max_current_quality=k

        return [max_current_quality,index_max_current_quality]



    #Ultimate testing is with runStep() ENV method
    def nextAction(self,laby):

        """ returns a, next action as s'=a(s) """
        [i,j]=laby.current_position #attribute is used two times so we call it once
        List_all_actions = [[-1,0],[0,1],[1,0],[0,-1]] #North,East,South,West
        #Possible actions in Quality Matrix
        actions = laby.possibleActions([i,j])
        if actions==[]:
            print("No possible action")
            print(laby.show())
            return None
        random_value=random.random()

        if random_value<self.Epsilon:
            #Chosing random Action

            action = actions[random.randint(0,len(actions)-1)]

        else:
            #Chosing acute Action
            current_position=laby.current_position
            (max_current_quality,index_max_current_quality)=self.maxQuality([i,j])
            #Going from index in Quality matrix to action
            action=List_all_actions[index_max_current_quality]

        if action in actions:
            return action
        else:
            print("Error : invalid action\n")
            return None


    #STILL TO CHANGE
    def ChangeParameters(self,reward,laby,action):
        [i,j]=laby.current_position # We call it once since it is used multiple times

        #Error case : given action is not a possible action
        if action not in laby.possibleActions([i,j]):
            print("Error : invalid action\n")
            return None

        List_all_actions = [[-1,0],[0,1],[1,0],[0,-1]] #North,East,South,West
        action_index=List_all_actions.index(action)
        print("action_index of given action:\n",action_index)
        if self.Quality[i,j][action_index]>=0:
            #The quality matrix is changed only if quality is already positive, otherwise action is also impossible (double check)
            max_current_quality=self.maxQuality([i,j])[0]
            print("\n max_current_quality: \n",max_current_quality)
            self.Quality[i,j][action_index]=self.Lambda*(reward+self.Gamma*max_current_quality+(1-self.Lambda)*self.Quality[i,j][action_index])

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
    [i,j]=laby.current_position
    print("\n current position: \n",[i,j])
    print("\n Quality at current position:\n",agent_qlearning.Quality[i,j])

    #maxQuality()
    # for k in range(SIZE):
    #     for l in range(SIZE):
    #         print("\n chosen position :\n",[k,l])
    #         print("\n Associated quality matrix :\n",agent_qlearning.Quality[k,l])
    #         print("value and index of maximum Quality for the chosen position",agent_qlearning.maxQuality([k,l]))

    #nextAction()
    next_action=agent_qlearning.nextAction(laby)
    print("\n next action is :\n",next_action)

    #ChangeParameters()
    [i,j]=laby.current_position
    next_action=agent_qlearning.nextAction(laby)
    print("\ Quality at current position, Epsilon, Lambda :\n",agent_qlearning.Quality[i,j],agent_qlearning.Epsilon,agent_qlearning.Lambda)

    next_position=laby.next_position(next_action)
    reward=state(laby.State(next_position)).reward()
    print("reward of next state:\n",reward)
    
    agent_qlearning.ChangeParameters(reward,laby,next_action)
    print("\n Changing parameters...\n")
    print("\n Quality at current position, Epsilon, Lambda :\n",agent_qlearning.Quality[i,j],agent_qlearning.Epsilon,agent_qlearning.Lambda)
