#INCLUDING AGENT FILES AND ENVIRONMENT FILES
import Environnement.environment
import Agent.AgentRandom
import system

#Variables initialisations
SIZE=10
Nb_episodes=100
max_Action_Count
#STEPS

#Initializing System

#Initializing Environment
random_environment=ENV(SIZE,SIZE,numpy.zeros((SIZE,SIZE)),[0,0])
random_environment.create_random_environment()
random_environment.show()

New_system=system(random_environment,AgentRandom)

List_of_Rewards=[]
for i in range(Nb_episodes):
    List_of_Total_Rewards.append(New_system.runEpisode(maxActionCount))
    New_system.laby.show()
