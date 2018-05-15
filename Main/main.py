#INCLUDING AGENT FILES AND ENVIRONMENT FILES
import numpy
from environment import ENV
from environment import state
from AgentRandom import AgentRandom
from system import System

#Variables initialisations
SIZE=10
Nb_episodes=10
maxActionCount=1000
#STEPS

#Initializing System

#Initializing Environment
random_environment=ENV(SIZE,SIZE,numpy.zeros((SIZE,SIZE)),[0,0])
random_environment.create_random_environment()
random_environment.show()
agent = AgentRandom()
New_system=System(random_environment,agent)

List_of_Total_Rewards=[]
for i in range(Nb_episodes):
    List_of_Total_Rewards+=[New_system.runEpisode(maxActionCount)]
    New_system.laby.show()
print("Rewards:",List_of_Total_Rewards)
print("Max reward:",max(List_of_Total_Rewards),"Min reward",min(List_of_Total_Rewards))
