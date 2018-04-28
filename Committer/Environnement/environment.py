# '''''' Environment and state classes ''''''
#numpy is needed for matrix operations ---> Need to use pure 2D-list manipulation
import numpy
#random is needed for random initialisations
import random

#Restrictions for states in the maze:
#    - A "start" or an "arrival" state is on the border of the maze.
#    - an "arrival" state is unique in a maze.
#Reminder : List_of_states=["o","x","s","a"], respectively hole, wall, start and arrival

class state:
    def __init__(self,name_index):
        """ A state is defined by its name_index, meaning the index corresponds to a state (see List_of_states)"""

        self.name_index=name_index

    def arrival_state(self):
        """ This method makes the state an arrival stateself.
        The arrival state has its name_index to 3 (see List_of_states)"""

        self.name_index=3

    #definition of random functions, according to restrictions of a maze.

    def random_intern_state(self):
        """This method randomly creates a state of the inside of the maze in accordance with restrictions.
        The intern possible states are holes and walls, corresponding to a name_index of 0 or 1 (see List_of_states)"""

        dice=random.randint(0,1)
        self.name_index=dice

    def random_extern_state(self):
        """This method randomly creates a state of the border of the maze in accordance with restrictions.
        We intentionally forget the (unique) arrival state (name_index of 4, see List_of_states) to add it in the end"""

        dice=random.randint(0,2)
        self.name_index=dice


class ENV:
    def __init__(self,width,length,states,current_position):
        """An environment is defined by its shape (width and length) and its states,
        wich is a numpy matrix (array) of indexes of states (name_index of each state)"""

        #Dimensions of the environment
        self.width=width
        self.length=length
        #List of states of the environment where there is a hole, a wall, a start or an end.
        self.states=states


    def show(self):
        """This method prints on the screen the matrix of states of the environment.
        For this, the matrix of states has to be created from the matrix of name_index of states (self.states).
        The transition can be done with the List_of_states."""

        #4 states exists : hole (can go), wall (can't go), start and arrival, as :
        List_of_states=["o","x","s","a"]
        #conversion to python classical matrix
        List_to_print=self.states.tolist()
        #conversion of each state to its associated character
        for x in List_to_print:
            #x corresponds to each different list of states
            for y in x:
                #y corresponds to each different state in a list of states
                y=List_of_states[y]
                #the state has become its character value instead of the index
        #The matrix is now fully converted
        print(List_to_print)


    def create_random_environment(self):
        """ This method initializes an environment randomly, according to the assumed restrictions"""

        #Dimensions of the Environment
        width = random.randint(3,10) #1 Dimension for now
        length = random.randint(3,10)
        self.width=width
        self.length=length

        #List of states
        states=numpy.zeros((width,length))
        #creation of states within the maze
        for i in range (width-1):
            for j in range (length-1):
                states[i,j]=state(0)
                states[i,j].random_intern_state()

        #creation of states around the maze
        for j in range(length):
            states[-1,j]=state(0)
            states[-1,j].random_extern_state()
            states[0,j]=state(0)
            states[0,j].random_extern_state()
        for i in range(1,-1): # specific borns to exclude already assigned states
            states[i,-1]=state(0)
            states[i,-1].random_extern_state()
            states[i,0]=state(0)
            states[i,0].random_extern_state()

        #creation of the arrival (substitution to an external state)
        bool_border=-random.randint(0,1) #to get 0 or -1
        [i,j]=[bool_border,bool_border]
        I_OR_J=random.randint(0,1)
        [i,j][1-I_OR_J]=random.randint(1,states.shape[1-I_OR_J]) #randomizing again on whole dimension the unchosen border
        states[i,j]=state(0)
        states[i,j].arrival_state() #arrival can now be put there

        #States of the environment are now fully randomly created in accordance with every restriction
        self.states=states


     def isInitialState(self, state):
        """Check whether state is a starting position, return a boolean"""
		if (state.name_index!=2):
		    return(False)
        else:
            return(True)


    def initialStates(self):
        """Return list of all possible starting positions"""
        initStates = []
        for i in range(self.length):
            for j in range(self.width):
                if self.isInitialState(self.states[i][j]):
                   initStates.append(self.states[i][j])
		return(initStates)


    def isTerminalState(self, state):
        """Check whether state is a finish position, return a boolean"""
		if (state.name_index!=3):
		    return(False)
        else:
            return(True)


    def terminalStates(self):
        """Return list of all possible starting positions"""
        termStates = []
        for i in range(self.length):
            for j in range(self.width):
                if self.isTerminalState(self.states[i][j]):
                   termStates.append(self.states[i][j])
		return(termStates)


    def currentState(self):
        """Returns the name_index of the current state, meaning the state of the current position"""
		current_state=self.states[self.current_position]
        #if current_state is a state value (4 for example), then currentState will become currentPosition.
		return(current_state)


    def possibleActions(self):
         """Description de la methode"""
        #NOT FINISHED
        possible_actions=[]
        current_state=self.currentState()
        if current_state==1 or current_state==3:
            return
        #North and South
        j=0
        for i in [-1,1]:
            if states[self.current_position[0]+i,self.current_position[1]]!=1:
                possible_actions.append([i,j])

        #West and East
        i=0
        for j in [-1,1]  :
            if states[self.current_position[0],self.current_position[1]+j]!=1:
                possible_actions.append([i,j])
        #['N', 'S', 'O', 'E'] corresponds to [[-1,0],[1,0],[0,-1],[0,1]]
		return(possible_actions)

#testing environment initialization and plotting
random_environment=ENV(1,1,numpy.zeros((1,1)))
random_environment.create_random_environment()
random_environment.show()
