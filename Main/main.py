#INCLUDING AGENT FILES AND ENVIRONMENT FILES
import numpy
from environment import ENV
from environment import state
from AgentQLearning import AgentQLearning
from AgentRandom import AgentRandom
from system import System

import matplotlib.pyplot as plt

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
def runMain(SIZE,Gamma,Nb_episodes,maxActionCount):

    #INITIALISATION
    #Variables initialisations
    #Nb_episodes=100
    #maxActionCount=100
    Epsilon=1
    Lambda=1
    #Gamma=0.5

    #SIZE=5

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
    Ratio_victory=[0,0,0,0,0,0,0,0,0,0]

    for k in range(10):
        for x in range(len(List_of_Total_Rewards)//10):
            debut=len(List_of_Total_Rewards)//10*k
            if List_of_Total_Rewards[debut+x]>10000:
                Ratio_victory[k]+=1
        Ratio_victory[k]/=len(List_of_Total_Rewards)//10

    print("Le ratio du nombre de victoires est : \n")
    for i in range(10):
        print("Dans le ",i,"ième dixième de tests :",Ratio_victory[i],"\n")
    return qlearning_system.agent.Quality
    return(Ratio_victory)

#Test correlation between SIZE and Gamma and Nb_episodes
#SIZE,Gamma,Nb_episodes,maxActionCount
SIZE=10
Gamma = 0.01
List_Gamma = [0.01]
Nb_episodes=500
maxActionCount=500
List_RatioVictory_1=[]
List_RatioVictory_2=[]
List_RatioVictory_3=[]
List_RatioVictory_4=[]
##    List_Gamma += [Gamma+i*0.01]
#    List_RatioVictory+=[runMain(SIZE,Gamma+i*0.01,Nb_episodes,maxActionCount)[3]]
#plt.plot(List_RatioVictory,List_Gamma)
#plt.xlabel('Gamma')
#plt.ylabel('Ratio Victory')
#plt.show()

    #print("Ratio step",i+1,":",List_RatioVictory[i])

Q=runMain(SIZE,Gamma,Nb_episodes,maxActionCount)
