import numpy
import random
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


#Testing ENV class

#create_random_environment method is working because a new system has been created
print("laby :\n",New_system.laby)
print("debugging method by method in ENV class :\n")
print("laby width, length, states, current_position :\n",New_system.laby.width,New_system.laby.length,New_system.laby.states,New_system.laby.current_position)
# --> Need to convert to integers in numpy array
New_system.laby.show()
print("list of initial states :\n",New_system.laby.initialStates())
print("list of terminal states :\n",New_system.laby.terminalStates())
print("name_index of current state :\n",New_system.laby.currentState())
List_possible_actions=New_system.laby.possibleActions()
print("List of possible actions from the current position :\n",List_possible_actions)

#Testing runStep method
next_action=List_possible_actions[random.randint(0,len(List_possible_actions)-1)]
print("laby current_position :\n",New_system.laby.current_position)
New_system.laby.show()
#Running new step
New_system.laby.runStep(next_action)
#
print("Processing new step...\n")
print("laby new_position :\n",New_system.laby.current_position)
New_system.laby.show()


#Testing state class

#random_intern_state and random_extern_state are working because create_random_environment method is working
tested_state=state(random.randint(0,3))
print("state :\n",tested_state)
print("name_index of tested_state :\n",tested_state.name_index)
print("reward of tested_state :\n", tested_state.reward())

#Test of arrival_state()
tested_state=state(random.randint(0,2))
current_name_index=tested_state.name_index
tested_state.arrival_state()
print("processing arrival_state() ...")
new_name_index=tested_state.name_index
if new_name_index==3:
    print("arrival_state() is working")
else:
    print("arrival_state() is not working")
    print("name_index of current tested_state :\n",current_name_index)
    print("name_index of new tested_state :\n",new_name_index)
