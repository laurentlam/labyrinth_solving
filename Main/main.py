#INCLUDING AGENT FILES AND ENVIRONMENT FILES
import numpy
from environment import ENV
from environment import state
from AgentQLearning import AgentQLearning
from AgentRandom import AgentRandom
from system import System


#Initializing System


#Random : uncomment when General Class Agent Programming is implemented

# random_agent = AgentRandom()
# #With General Agent Class :
# #random_agent=Agent(AgentRandom,None)
# random_system=System(laby,random_agent)
#
# List_of_Total_Rewards=[]
# for i in range(Nb_episodes):
#     List_of_Total_Rewards+=[random_system.runEpisode(maxActionCount)]
#     #random_system.laby.show()
# print("Rewards:",List_of_Total_Rewards)
# print("Max reward:",max(List_of_Total_Rewards),"Min reward",min(List_of_Total_Rewards))





#QLearning
def runMain():

    #INITIALISATION
    #Variables initialisations
    Nb_episodes=200
    maxActionCount=100
    Epsilon=1
    Lambda=1
    Gamma=0.6

    SIZE=7

    #Initialising Environment
    laby=ENV(SIZE,SIZE,numpy.zeros((SIZE,SIZE)),[0,0])
    laby.create_random_environment()
    laby.show()

    #Initialising agent
    qlearning_agent = AgentQLearning(Epsilon,Lambda,Gamma,laby)
    #With General Agent Class :
    #qlearning_agent=Agent(AgentQLearning,[Epsilon,Lambda,Gamma,laby])

    #Initialising system
    qlearning_system=System(laby,qlearning_agent)
    initial_position=qlearning_system.laby.current_position

    #RUNNING ALGORITHM
    List_of_Total_Rewards=[]

    for k in range(Nb_episodes):
        qlearning_system.laby.current_position=initial_position
        List_of_Total_Rewards+=[qlearning_system.runEpisode(maxActionCount)]

    print("Rewards:",List_of_Total_Rewards)
    print("Max reward:",max(List_of_Total_Rewards),"Min reward",min(List_of_Total_Rewards))
    return qlearning_system.agent.Quality
