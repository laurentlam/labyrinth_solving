import ENV from environment

class labyrinthe:
    """Votre description"""

    def __init__(self,longueur,largeur):
        #Dimensions of the environment
        self.width = largeur
        self.length = longueur
        self.states = environment.create_random_ENV(width,length)

    def show(self):
        """Description de la methode d'affichage choisie"""
		...
		print("Mon labyrinthe de maniere ostensible mais simple")

    def states(self):
        """Description de la methode"""
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


	def currentState(self):
        """Description de la methode"""
		...
		return(self.currentState)


	def possibleActions(self):
         """Description de la methode"""
		...
		return(['N', 'S', 'E', 'O'])


	def runStep(self, action):
         """Description de la methode"""
		 rewward=0
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
