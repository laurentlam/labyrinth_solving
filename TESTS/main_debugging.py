import numpy
from environment import ENV
from environment import state
from AgentRandom import AgentRandom
from system import System

#Variables initialisations
SIZE=10
Nb_episodes=100
maxActionCount=100
#STEPS

#Initializing System

#Initializing Environment
random_environment=ENV(SIZE,SIZE,numpy.zeros((SIZE,SIZE)),[0,0])
random_environment.create_random_environment()
agent = AgentRandom()
New_system=System(random_environment,agent)

print("laby\n",New_system.laby)
print("debugging method by method in ENV class\n")
print("laby width, length, states, current_position\n",New_system.laby.width,New_system.laby.length,New_system.laby.states,New_system.laby.current_position)
# --> Need to convert to integers in numpy array
New_system.laby.show()
print("list of initial states\n",New_system.laby.initialStates())
print("list of terminal states\n",New_system.laby.terminalStates())
print("name_index of current state\n",New_system.laby.currentState())
print("List of possible actions from the current position\n",New_system.laby.possibleActions())

#Testing runStep method


#TO DO
