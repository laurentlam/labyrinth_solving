import ENV from environment

class labyrinthe:
    """Votre description"""

    def __init__(self,longueur,largeur):
<<<<<<< HEAD
        """Description de l'initialisation"""
        #DONE --> Added "states" attribut
        #Dimensions of the environment
        self.width = largeur
        self.length = longueur
        self.states = environment.create_random_ENV(width,length)
>>>>>>> 6ba381a80c6f30c639b05eddd0701a3b416cd64e

    def show(self):
        """Description de la methode d'affichage choisie"""
        #DONE
		...
		print("Mon labyrinthe de maniere ostensible mais simple")

    def states(self):
        """Description de la methode"""
<<<<<<< HEAD
        #NOT NEEDED --> states is now an attribut
		...
		return([])


     def isInitialState(self, state):
        """Description de la methode"""
        #TO DO --> easy : find the "s" states, meaning with a name_index of 2
        ...
		return(false)

    def initialStates(self):
        """Description de la methode"""
        #TO DO --> easy : lists positions of "s" states (can use isInitialState)
		...
		return([])


    def isTerminalState(self, state):
        """Description de la methode"""
        #TO DO --> easy : find the "a" (unique) state, meaning with a name_index of 3
		...
		return(false)

    def terminalStates(self):
        """Description de la methode"""
        #TO DO --> easy : lists positions of "a" states (can use isTerminalState)
        #Note : arrival state is unique in this modelization
		...
		return([])


=======
		states = self.states
		return(states)


     def isInitialState(self, state):
        """Check whether state is a starting position, return a boolean"""
		if (state.name!="s"):
		    return(False)
        else:
            return(True)

    def initialStates(self):
        """Return list of all possible starting positions"""
        initStates = []
        for i in range(length):
            for j in range(width):
                if isInitialState(self.states[i][j]):
                   initStates+=self.states[i][j]
		return(initStates)


    def isTerminalState(self, state):
        """Check whether state is a finish position, return a boolean"""
		if (state.name!="a"):
		    return(False)
        else:
            return(True)

    def terminalStates(self):
        """Return list of all possible starting positions"""
        termStates = []
        for i in range(length):
            for j in range(width):
                if isTerminalState(self.states[i][j]):
                   termStates+=self.states[i][j]
		return(termStates)


>>>>>>> 6ba381a80c6f30c639b05eddd0701a3b416cd64e
	def currentState(self):
        """Description de la methode"""
        #TO DO --> need to have the position (global variable ?) of the current state
		...
		return(self.currentState)


	def possibleActions(self):
         """Description de la methode"""
         #TO DO --> Need to find the currentState first
		...
		return(['N', 'S', 'E', 'O'])


	def runStep(self, action):
         """Description de la methode"""
		 reward=0
		...
		return (self.currentState, reward)


    def transition(self):
        """Description de la methode"""
		...
		return([])

	def possibleTransitions(self):
         """Description de la methode"""
		...
		return(['N', 'S', 'E', 'O'])

	def runTransition(self, action):
         """Description de la methode"""
		 rewward=0
		...
		return (self.currentState, rewward)
