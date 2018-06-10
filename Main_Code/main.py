#INCLUDING AGENT FILES AND ENVIRONMENT FILES
import numpy
import matplotlib.pyplot as plt

from environment import ENV
from environment import state
from AgentQLearning import AgentQLearning
from AgentRandom import AgentRandom

# We don't use a general agent class for now as we only have two agents
################################################################################
#from Agents import Agent
################################################################################

from system import System

random_env=0
debugLevel=0

#Random :

# random_agent = AgentRandom()


# Chosing random OR existing environment

if random_env>0:
    SIZE = 10
    laby=ENV(SIZE,SIZE,numpy.zeros((SIZE,SIZE)),[0,0])
    laby.create_random_environment()
else:
    SIZE = 15
    laby=ENV(SIZE,SIZE,numpy.zeros((SIZE,SIZE)),[0,0])
    laby.create_existing_environment('labyrinthe_produit.txt')

laby.show()



# QLearning
# Returns the optimal route of any starting position, given a quality matrix and a system
def OptimalRoute(System,Quality_Matrix,starting_position):

    """ Returns the optimal route to finish the maze with maximum reward, given a quality matrix and starting from a given position"""

    [i,j]=starting_position
    Optimal_Route=[[i,j]]

    while System.laby.states[i,j]!=3:
        next_action_index=System.agent.maxQuality([i,j])[1]
        List_all_actions = [[-1,0],[0,1],[1,0],[0,-1]] #North,East,South,West
        [di,dj]=List_all_actions[next_action_index]
        i+=di
        j+=dj
        Optimal_Route.append([i,j])

    return Optimal_Route

def runMain(SIZE,Gamma,Nb_episodes,maxActionCount):

    # INITIALISATION
    # Variables initialisations

    Epsilon=1
    Lambda=1


    # Initialising agent
    qlearning_agent = AgentQLearning(Epsilon,Lambda,Gamma,laby)

    # Initialising system
    qlearning_system=System(laby,qlearning_agent)
    initial_position=qlearning_system.laby.current_position

    # RUNNING ALGORITHM
    List_of_Total_Rewards=[]
    for k in range(Nb_episodes):
        qlearning_system.laby.current_position=initial_position
        List_of_Total_Rewards+=[qlearning_system.runEpisode(maxActionCount)]

    #print("Rewards:",List_of_Total_Rewards)
    #print("Max reward:",max(List_of_Total_Rewards),"Min reward",min(List_of_Total_Rewards))
    Ratio_victory=[0,0,0,0]

    for k in range(4):
        for x in range(len(List_of_Total_Rewards)//4):
            debut=len(List_of_Total_Rewards)//4*k
            if List_of_Total_Rewards[debut+x]>10000:
                Ratio_victory[k]+=1
        Ratio_victory[k]/=len(List_of_Total_Rewards)//4

    #print("Le ratio du nombre de victoires est : \n")
    for i in range(4):
        print("Dans le ",i,"ième dixième de tests :",Ratio_victory[i],"\n")
    #return qlearning_system.agent.Quality
    return(Ratio_victory)

#Test correlation between SIZE and Gamma and Nb_episodes
#SIZE,Gamma,Nb_episodes,maxActionCount
SIZE=8
Gamma = 0.99
List_Gamma = []
Nb_episodes=2000
maxActionCount=2000
List_RatioVictory_1=[]
"""
for i in range(50):
    List_Gamma += [Gamma+i*0.01]
    List_RatioVictory=runMain(SIZE,Gamma+i*0.01,Nb_episodes,maxActionCount)
    List_RatioVictory_1+=[List_RatioVictory[3]]
print("Done.")
plt.plot(List_Gamma,List_RatioVictory_1,'bo')
plt.xlabel('Gamma')
plt.ylabel('Ratio Victory')
plt.show()
"""
    #print("Ratio step",i+1,":",List_RatioVictory[i])
#runMain(SIZE,Gamma,Nb_episodes,maxActionCount)

def runOptimalRoute():

    # INITIALISATION
    # Variables initialisations

    Epsilon=1
    Lambda=1
    Gamma = 0.85
    SIZE=5
    Nb_episodes=5000
    maxActionCount=5000

    # Initialising agent
    # Without General Agent Class :
    qlearning_agent = AgentQLearning(Epsilon,Lambda,Gamma,laby)

    # Initialising system
    qlearning_system=System(laby,qlearning_agent)
    initial_position=qlearning_system.laby.current_position

    for k in range(Nb_episodes):
        qlearning_system.laby.current_position=initial_position
        qlearning_system.runEpisode(maxActionCount)
    Optimal_Route=OptimalRoute(qlearning_system,qlearning_system.agent.Quality,initial_position)
    return Optimal_Route

if __name__=="__main__":

    SIZE=5
    Gamma = 0.8
    Nb_episodes=1000
    maxActionCount=1000
    initial_position=qlearning_system.laby.current_position
    for k in range(Nb_episodes):
        qlearning_system.laby.current_position=initial_position
        List_of_Total_Rewards+=[qlearning_system.runEpisode(maxActionCount)]
    Optimal_Route=OptimalRoute(qlearning_system,qlearning_system.agent.Quality,initial_position)
