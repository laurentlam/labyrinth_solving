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



#Random :

# random_agent = AgentRandom()


# Chosing random OR existing environment
random_env=0
if random_env>0:
    SIZE = 10
    laby=ENV(SIZE,SIZE,numpy.zeros((SIZE,SIZE)),[0,0])
    laby.create_random_environment()
else:
    SIZE = 15
    laby=ENV(SIZE,SIZE,numpy.zeros((SIZE,SIZE)),[0,0])
    laby.create_existing_environment('labyrinthe_produit.txt')

#Printing initial maze
laby.show()



# QLearning

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


def QualityEvolution(SIZE,Gamma,Nb_episodes,maxActionCount):

    """ Returns the list of qualities of the optimal route, from each episodeself.
    Qualities of the optimal route are the Q[i,j][k] following the optimal route. (Length is one less than the length of the route)
    """

    # INITIALISATION
    # Variables initialisations

    Epsilon=1
    Lambda=1

    # Initialising agent
    # Without General Agent Class :
    qlearning_agent = AgentQLearning(Epsilon,Lambda,Gamma,laby)

    # With General Agent Class :
    ############################################################################
    #qlearning_agent=Agent(AgentQLearning,[Epsilon,Lambda,Gamma,laby])
    ############################################################################

    # Initialising system
    qlearning_system=System(laby,qlearning_agent)
    initial_position=qlearning_system.laby.current_position

    # Running algorithm and getting data
    Quality=[qlearning_system.agent.Quality]

    # Start of algorithm loop
    for k in range(Nb_episodes):
        qlearning_system.laby.current_position=initial_position
        qlearning_system.runEpisode(maxActionCount)
        Quality.append(qlearning_system.agent.Quality)
    # End of algorithm loop


    # Pre-processing the data, i.e. chosing what we want, from Quality

    # Finding the best route after processing (last Quality matrix)
    Optimal_Route=OptimalRoute(qlearning_system,Quality[-1],initial_position)
    Quality_Optimal_Route=[[]]*len(Quality)

    # Extracting Quality_Optimal_Route
    for l in range(len(Optimal_Route)-1):

        [i,j]=Optimal_Route[l] # Fixed position in the optimal route

        # Finding the index of the next action knowing the next position
        action=[0,0]
        action[0]=Optimal_Route[l+1][0]-Optimal_Route[l][0]
        action[1]=Optimal_Route[l+1][1]-Optimal_Route[l][1]
        # Relative motion is the next action
        List_all_actions = [[-1,0],[0,1],[1,0],[0,-1]] #North,East,South,West
        action_index=List_all_actions.index(action)

        # Extracting Quality_Optimal_Route from Quality
        for t in range(len(Quality)):
            Quality_Optimal_Route[t].append(Quality[t][i,j][action_index])
        # End of extraction

################################################################################ DOESN'T WORK YET
    # Plotting Quality Evolution (Processing data internally)
    T=[t for t in range(len(Quality_Optimal_Route))]

    Graph_to_show=[]
    for k in range(len(Quality_Optimal_Route[0])):
        Graph_to_append=[Quality_Optimal_Route[t][k] for t in range(len(Quality_Optimal_Route))]
        Graph_to_show.append(Graph_to_append)
    plt.plot(T,Graph_to_show[-1],'ro')
    plt.show()
    #print(Quality_Optimal_Route)
################################################################################

    # Returning data to be processed
    return [Optimal_Route,Quality_Optimal_Route]



def runMain(SIZE,Gamma,Nb_episodes,maxActionCount):

    # INITIALISATION
    # Variables initialisations

    Epsilon=1
    Lambda=1


    # Initialising agent
    # Without General Agent Class
    qlearning_agent = AgentQLearning(Epsilon,Lambda,Gamma,laby)

    # With General Agent Class :
    ############################################################################
    #qlearning_agent=Agent(AgentQLearning,[Epsilon,Lambda,Gamma,laby])
    ############################################################################

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

    # Calculating the ratio between the number of victories and the number of episodes
    # Dividing the number of episodes into 4 parts to distinguish 4 phases
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


#Test correlation between SIZE and Gamma and Nb_episodes
test_cor = 0
if test_cor>0:
    Gamma = 0.01
    List_Gamma = []
    Nb_episodes=3000
    maxActionCount=3000
    List_RatioVictory_1=[]
    #Running the agent for each value of Gamma (from 0.01 to 0.99)
    for i in range(99):
        List_Gamma += [Gamma+i*0.01]
        List_RatioVictory=runMain(SIZE,Gamma+i*0.01,Nb_episodes,maxActionCount)
        List_RatioVictory_1+=[List_RatioVictory[3]]
        print("Done.")
    #Plotting the results
    plt.plot(List_Gamma,List_RatioVictory_1,'bo')
    plt.xlabel('Gamma')
    plt.ylabel('Ratio Victory')
    plt.show()

#In order to run the algorithm at the beginning if necessary
#Have to adapt the initial Variables
"""
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
"""
