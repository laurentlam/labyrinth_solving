################################################################################
#--------------------------HOW TO RUN THE ALGORITHM----------------------------#
################################################################################
#
# 1) set debugLevel=1, graphLevel=0, lastActionLevel=0 at the start of the system.py file
#
# 2) set test_cor=1 at the end of the main.py file (start of the last paragraph)
#
# 3) Due to OS issues, set the following at line 68 of system :
#                                       - MAC/LINUX : set os.system("clear")
#                                       - WINDOWS : set os.system("cls")
#
# 3) launch main.py file (this very file)
#
################################################################################



#-----------------------INCLUDING CLASSES AND METHODS--------------------------#
################################################################################
# INCLUDING MATH AND PLOTTING METHODS
import numpy
import matplotlib.pyplot as plt

# INCLUDING AGENT FILES AND ENVIRONMENT FILES
from environment import ENV
from environment import state
from AgentQLearning import AgentQLearning
from AgentRandom import AgentRandom

# INCLUDING SYSTEM FILE
from system import System
################################################################################



#-------------------------CREATING ENVIRONMENT---------------------------------#
################################################################################
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

# Printing initial maze
laby.show()
################################################################################



#-----------------------------QLEARNING FUNCTIONS------------------------------#
################################################################################
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


def runOptimalRoute():
    """ Returns the optimal route of an already created laby (see random_env parameter above),
    by launching the algorithm """

    # INITIALISATION
    # Variables initialisations

    Epsilon=1
    Lambda=1
    Gamma = 0.85
    Nb_episodes=5000
    maxActionCount=5000

    # Initialising agent
    qlearning_agent = AgentQLearning(Epsilon,Lambda,Gamma,laby)

    # Initialising system
    qlearning_system=System(laby,qlearning_agent)
    initial_position=qlearning_system.laby.current_position

    for k in range(Nb_episodes):
        qlearning_system.laby.current_position=initial_position
        qlearning_system.runEpisode(maxActionCount)
    Optimal_Route=OptimalRoute(qlearning_system,qlearning_system.agent.Quality,initial_position)
    return Optimal_Route
################################################################################



#-------------------------RUNNING TESTS AND PLOTTING---------------------------#
################################################################################
def runOne():

    """ This function plots the graph of total reward through an episode
    Note : don't forget to put the graph_level of system.py to 1
    """

    # INITIALISATION
    # Variables initialisations

    Epsilon=0.3
    Lambda=0.8
    Gamma = 0.5
    maxActionCount=5000

    # Initialising agent
    qlearning_agent = AgentQLearning(Epsilon,Lambda,Gamma,laby)

    # Initialising system
    qlearning_system=System(laby,qlearning_agent)

    # Running algorithm
    initial_position=qlearning_system.laby.current_position
    qlearning_system.runEpisode(maxActionCount)
    qlearning_system.laby.current_position=initial_position

def lastAction():

    """
    This function plots the number of actions through Nb_episodes.
    Note : don't forget to put to 1 the lastActionLevel in system.py
    """

    # INITIALISATION
    # Variables initialisations

    Epsilon=1
    Lambda=0.8
    Gamma = 0.8
    maxActionCount=5000
    Nb_episodes=500

    # Initialising agent
    qlearning_agent = AgentQLearning(Epsilon,Lambda,Gamma,laby)

    # Initialising system
    qlearning_system=System(laby,qlearning_agent)
    initial_position=qlearning_system.laby.current_position

    # RUNNING ALGORITHM
    List_of_last_actions=[]
    for k in range(Nb_episodes):
        qlearning_system.laby.current_position=initial_position
        List_of_last_actions.append(qlearning_system.runEpisode(maxActionCount))
    qlearning_system.laby.current_position=initial_position

    #PLOTTING
    Episodes=[i for i in range(Nb_episodes)]
    plt.plot(Episodes,List_of_last_actions)
    plt.xlabel("Number of episodes")
    plt.ylabel("Number of actions to get to the end")
    plt.show()

def runMain(SIZE,Gamma,Nb_episodes,maxActionCount):

    """ Runs the algorithm.
    It allows us to change significant parameters and analyse their influence on algorithm."""

    # INITIALISATION
    # Variables initialisations

    Epsilon=1
    Lambda=0.8

    # Initialising agent
    qlearning_agent = AgentQLearning(Epsilon,Lambda,Gamma,laby)

    # Initialising system
    qlearning_system=System(laby,qlearning_agent)
    initial_position=qlearning_system.laby.current_position

    # RUNNING ALGORITHM
    List_of_Total_Rewards=[]
    for k in range(Nb_episodes):
        qlearning_system.laby.current_position=initial_position
        List_of_Total_Rewards+=[qlearning_system.runEpisode(maxActionCount,k,Nb_episodes)]

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
    # Agent getting back into starting position at the end
    qlearning_system.laby.current_position=initial_position
    #print("Le ratio du nombre de victoires est : \n")
    for i in range(4):
        print("Dans le ",i+1,"ième quart de tests :",Ratio_victory[i],"\n")
    #return qlearning_system.agent.Quality
    return(Ratio_victory)

#Test correlation between SIZE and Gamma and Nb_episodes
test_cor = 1
if test_cor>0:
    Gamma = 0.8
    # List_Gamma = []
    Nb_episodes=200
    maxActionCount=500
    List_RatioVictory_1=[]
    #Running the agent for each value of Gamma (from 0.1 to 0.99)

    List_RatioVictory=runMain(SIZE,Gamma,Nb_episodes,maxActionCount)
    # List_RatioVictory_1+=[max(List_RatioVictory)]

    # List_Gamma += [0.99]
    # List_RatioVictory=runMain(SIZE,0.99,Nb_episodes,maxActionCount)
    # List_RatioVictory_1+=[max(List_RatioVictory)]
    # print("Done.")
    # #Plotting the results
    # plt.plot(List_Gamma,List_RatioVictory_1)
    # plt.xlabel('Gamma')
    # plt.ylabel('Ratio Victory max')
    # plt.show()


#In order to run the algorithm at the beginning if necessary
#Have to adapt the initial Variables
################################################################################
