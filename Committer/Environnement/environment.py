'''''' Environment and state classes ''''''
#numpy is needed for matrix operations
import numpy
#random is needed for random initialisations
import random

#Restrictions for states in the maze:
#    - A "start" or an "arrival" state is on the border of the maze.
#    - an "arrival" state is unique in a maze.

class state:
    def __init__(self,name):
        self.name=name
    #4 states exists : hole (can go), wall (can't go), start and arrival, as :
    List_of_states=["o","x","s","a"]

    #definition of random functions, according to restrictions of a maze.

    def random_intern_state(self):
        #picking a random state allowed within the maze
        dice=random.randint(1,2)
        random_state.name=List_of_states[dice]
        return random_state

    def random_extern_state(self):
        #picking a random state allowed on the border of the maze, but not an arrival as it is unique.
        dice=random.randint(1,3)
        random_state.name=List_of_states[dice]
        return random_state


class ENV:
    def __init__(self,width,length,states):
        #Dimensions of the environment
        self.width=width
        self.length=length
        #List of states of the environment where there is a hole, a wall, a start or an end.
        self.states=states

    def Visualise(self):
        #Simple matrix plotting
        print(ENV().states)

    def create_random_ENV(self):
        #The goal is to create a "random" matrix with only states for the List_of_states in the state class,
        #   in accordance with restrictions mentionned above the document.

        #Dimensions of the Environment
        width = random.randint(3,10) #1 Dimension for now
        length = random.randint(3,10)
        self.width=width
        self.length=length

        #List of states
        states=numpy.zeros(width,length)
        #creation of states within the maze
        for i in range (width-1):
            for j in range(length-1):
                states[i,j]=state.random_intern_state()

        #creation of states around the maze
        for j in range(length):
            states[-1,j]=state.random_extern_state()
            states[0,j]=state.random_extern_state()
        for i in range(1,-1): # specific borns to exclude already assigned states
            states[i,-1]=state.random_extern_state()
            states[i,0]=state.random_extern_state()

        #creation of the arrival (substitution to an external state)
        bool_border=-random.randint(0,1) #to get 0 or -1
        [i,j]=[bool_border,bool_border]
        I_OR_J=random.randint(0,1)
        [i,j][1-I_OR_J]=random.randint(size(states)[1-I_OR_J]) #randomizing again on whole dimension the unchosen border
        states[i,j]="a" #arrival can now be put there

        #States of the environment are now fully randomly created
        self.states=states

random_environment=ENV()
random_environment.create_random_ENV()
random_environment.Visualise()
