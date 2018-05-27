# '''''' Environment and state classes ''''''
#numpy is needed for matrix operations ---> Need to use pure 2D-list manipulation
import numpy
#random is needed for random initialisations
import random

#Restrictions for states in the maze:
#    - A "start" or an "arrival" state is on the border of the maze.
#    - an "arrival" state is unique in a maze.
#Reminder : List_of_states=["o","x","s","e"], respectively hole, wall, start and arrival

class state:
    def __init__(self,name_index):
         """ A state is defined by its name_index, meaning the index corresponds to a state (see List_of_states)"""

         self.name_index=name_index

    def reward(self):
         """ Calculates the reward of the Agent going to this state.
         We assume here that to a state is given a unique reward.
         That can be done with the List_of_Rewards below """
################################################################################
         #List_of_Rewards=[10,-1000,0,50000]
         List_of_Rewards=[-1,-1000,-10,50000]
################################################################################
         return (List_of_Rewards[int(self.name_index)])

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
        We intentionally forget the (unique) arrival state (name_index of 3, see List_of_states) to add it in the end"""

        dice=random.randint(1,2)
        self.name_index=dice


class ENV:
    def __init__(self,width,length,states,current_position):
        """An environment is defined by its shape (width and length) ,
        its states wich is a numpy matrix (array) of indexes of states (name_index of each state),
        and the current position of the agent."""

        #Dimensions of the environment
        self.width=width
        self.length=length
        #List of states of the environment where there is a hole, a wall, a start or an end.
        self.states=states
        #current position of the agent
        self.current_position=current_position

    def show(self):
        """This method prints on the screen the matrix of states of the environment.
        For this, the matrix of states has to be created from the matrix of name_index of states (self.states).
        The transition can be done with the List_of_states.
        Plus, the current position of the agent is visualised"""

        #5 states exists : hole (can go), wall (can't go), start and end as :
        List_of_states=["o","x","s","e"]
        #conversion to python classical matrix
        List_to_print=self.states.tolist()
        #conversion of each state to its associated character
        (i,j) = self.current_position
        str = (self.length+1)*' -'
        print(str)
        for x in range(self.width):
                for y in range(self.length):
                    if (x == i) and (y == j):
                        List_to_print[x][y] = "A"
                    else:
                        List_to_print[x][y] = List_of_states[int(List_to_print[x][y])]
                        #the state we print has become its character value instead of the index
                print('|',' '.join(List_to_print[x]) ,'|')
        print(str)


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
                state_temp=state(self.states[i][j])
                if self.isInitialState(state_temp):
                   initStates.append([i,j])
        return(initStates)


    def isTerminalState(self, state):
        """Check whether state is a finish position, return a boolean"""
        if (state!=3):
            return(False)
        else:
            return(True)


    def terminalStates(self):
        """Return list of all possible finish positions"""
        termStates = []
        for i in range(self.length):
            for j in range(self.width):
                state_temp=state(self.states[i][j])
                if self.isTerminalState(state_temp):
                   termStates.append([i,j])
        return(termStates)

    def State(self,position):

        """ Returns the name_index of the state of the given position, meaning the state of the given position"""

        [i,j]=position
        name_index=int(self.states[i,j])
        return name_index


    def currentState(self):

        """Returns the name_index of the current state, meaning the state of the current position"""

        current_name_index=self.State(self.current_position)
        return current_name_index


    def possibleActions(self,position):

        """ Finds all possible motions (actions) from a given position in the maze"""


        # List_of_states=["o","x","s","e"]=[hole,wall,start,end]=[0,1,2,3]
        possible_actions=[]
        states = self.states
        [x,y] = position
        width = self.width
        length = self.length
        #checking if there is no misplacement of the agent
        #if (current_state==1) or (current_state==3):
        #    return (NULL)
            #NULL value is chosen because empty list is for another error case (see above at next return)

        #if Agent on the border of the maze
        if ((x==0) or (x==width-1) or (y==0) or (y==length-1)):
        #North and South

            if (x==0):
                if (states[x+1,y]!=1) and (states[x+1,y]!=2): # Not a wall or starting position in the South
                    possible_actions.append([1,0])
            if (x==width-1):
                if (states[x-1,y]!=1) and (states[x-1,y]!=2): # Not a wall or starting position in the North
                    possible_actions.append([-1,0])

        #West and East

            if (y==0):
                if (states[x,y+1]!=1) and (states[x,y+1]!=2): # Not a wall or starting position in the East
                    possible_actions.append([0,1])
            if (y==length-1):
                if (states[x,y-1]!=1) and (states[x,y-1]!=2): # Not a wall or starting position in the West
                    possible_actions.append([0,-1])

        #If the agent is within the maze
        else:

            for i in [-1,1]:
                if (states[x+i,y]!=1) and (states[x+i,y]!=2): #Not a wall or starting position in the North then in the South
                    possible_actions.append([i,0])

        #West and East

            for j in [-1,1]:
                if (states[x,y+j]!=1) and (states[x,y+j]!=2): #Not a wall or starting position in the West then in the East
                    possible_actions.append([0,j])

        #['N', 'S', 'O', 'E'] corresponds to [[-1,0],[1,0],[0,-1],[0,1]]
        #which are relative motions from the current position
        return(possible_actions)
        #Note : if possible_actions is empty, the agent is blocked and the maze can't be solved --> error case.

    def next_position(self,position,action):

        """ returns the next position from position if action is applied
        Args:
            action : The action to do at the current state
        Returns:
            next_position : the position of the agent if the action was applied
        """

        [i,j]=position
        i+=action[0]
        j+=action[1]
        return [i,j]

    def runStep(self, action):

         """Perform the action in the state to change the position and get the reward
         Args:
             action : The action to do at the current state
         Returns:
             The current position is updated
             Return the total associated reward
         """

         # Checking if the action is in the possible_actions
         if action not in self.possibleActions(self.current_position):
             print("action is not a possible action (runStep)")
             return None

         # 1) Next position of the agent
         self.current_position=self.next_position(self.current_position,action)

         # 2) reward : reward from the new state of the agent
         reward=state(self.State(self.current_position)).reward()

         #returning : the reward
         return reward

    def create_random_environment(self):

        """ This method initializes an environment randomly, according to the assumed restrictions
        Args:
            No arguments.
        Returns:
            self (the maze) is actualized : width, length, states and current position
        """

        #List of states
        width=self.width
        length=self.length
        states=numpy.zeros((width,length))

        #creation of states within the maze
        for i in range (1,width-1):
            for j in range (1,length-1):
                state_temp = state(0)
                #Having 1/4 probability to get a wall
                state_temp.random_intern_state()
                if (state_temp.name_index == 1):
                    state_temp.random_intern_state()
                states[i,j] = state_temp.name_index

        #creation of states around the maze
        for j in range(length):
            state_temp.random_extern_state()
            states[-1,j] = state_temp.name_index
            state_temp.random_extern_state()
            states[0,j] = state_temp.name_index
        for i in range(1,width-1): # specific borns to exclude already assigned states
            state_temp.random_extern_state()
            states[i,-1] = state_temp.name_index
            state_temp.random_extern_state
            states[i,0] = state_temp.name_index

        self.states=states

        #Creation of a list of the initial states
        initialStates_list = self.initialStates()
        if (len(initialStates_list)<2):
            return None
        #Choosing a random initial state to start with
        random_index=random.randint(0,len(initialStates_list)-1)
        #Initial state not in a corner
        while (initialStates_list[random_index]==[0,0]) or (initialStates_list[random_index]==[width-1,length-1]) or (initialStates_list[random_index]==[0,length-1]) or (initialStates_list[random_index]==[width-1,0]):
            random_index=random.randint(0,len(initialStates_list)-1)
        self.current_position = initialStates_list[random_index]
        start_position = self.current_position
        #Making the initial state accessible
        if (start_position[0]==0):
            states[start_position[0]+1,start_position[1]]=0
        if (start_position[0]==width-1):
            states[start_position[0]-1,start_position[1]]=0
        if (start_position[1]==0):
            states[start_position[0],start_position[1]+1]=0
        if (start_position[1]==length-1):
            states[start_position[0],start_position[1]-1]=0

        #creation of the arrival (substitution to a starting state)
        initialStates_list.pop(random_index) #list of starts without the agent starting position
        random_index=random.randint(0,len(initialStates_list)-1)
        #Terminal state not in a corner
        while (initialStates_list[random_index]==[0,0]) or (initialStates_list[random_index]==[width-1,length-1]):
            random_index=random.randint(0,len(initialStates_list)-1)
        arrival_position = initialStates_list[random_index]
        states[arrival_position[0],arrival_position[1]] = 3
        #Making the terminal state accessible
        if (arrival_position[0]==0):
            states[arrival_position[0]+1,arrival_position[1]]=0
        if (arrival_position[0]==width-1):
            states[arrival_position[0]-1,arrival_position[1]]=0
        if (arrival_position[1]==0):
            states[arrival_position[0],arrival_position[1]+1]=0
        if (arrival_position[1]==length-1):
            states[arrival_position[0],arrival_position[1]-1]=0

        #Other unused initial states become a wall
        initialStates_list.pop(random_index) #list of starts without the agent finish position
        for position in initialStates_list:
            states[position[0],position[1]] = 1
        initialStates_list = [start_position[0],start_position[1]]
        #States of the environment are now fully randomly created in accordance with every restriction
        self.states=states
