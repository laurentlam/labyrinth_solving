#INCLUDING AGENT FILES AND ENVIRONMENT FILES
import numpy
from environment import ENV
from environment import state
from AgentQLearning import AgentQLearning
from system import System

#Variables initialisations
SIZE=10
Nb_episodes=10
maxActionCount=100
Epsilon=1
Lambda=1
Gamma=0.3

#STEPS

#Initializing System

#Initializing Environment
laby=ENV(SIZE,SIZE,numpy.zeros((SIZE,SIZE)),[0,0])
laby.create_random_environment()
laby.show()
agent = AgentQLearning(Epsilon,Lambda,Gamma,laby)
New_system=System(laby,agent)

List_of_Total_Rewards=[]
for i in range(Nb_episodes):
    Lambda=1
    Epsilon=1
    List_of_Total_Rewards+=[New_system.runEpisode(maxActionCount)]
    #New_system.laby.show()
print("Rewards:",List_of_Total_Rewards)
print("Max reward:",max(List_of_Total_Rewards),"Min reward",min(List_of_Total_Rewards))
