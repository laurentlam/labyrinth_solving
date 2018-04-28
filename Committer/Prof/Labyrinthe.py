import ENV from environment

class labyrinthe:
    """Votre description"""

    def __init__(self,longueur,largeur):
        """Description de l'initialisation"""
        #DONE --> Added "states" attribut
        #Dimensions of the environment
        self.width = largeur
        self.length = longueur
        self.states = environment.create_random_ENV(width,length)

    def show(self):
        """Description de la methode d'affichage choisie"""
        #DONE
		...
		print("Mon labyrinthe de maniere ostensible mais simple")

    def states(self):
        """Description de la methode"""
        #NOT NEEDED --> states is now an attribut
		...
		return([])


     def isInitialState(self, state):
        """Check whether state is a starting position, return a boolean"""
		if (state.name_index!=2):
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
		if (state.name_index!="3"):
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
