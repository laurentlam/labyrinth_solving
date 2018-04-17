import ...

class labyrinthe:
    """Votre description"""

    def __init__(self,longueur,largeur):
        """Description de l'initialisation"""

    def show(self):
        """Description de la methode d'affichage choisie"""
		...
		print("Mon labyrinthe de maniere ostensible mais simple")

    def states(self):
        """Description de la methode"""
		...
		return([])

		
     def isInitialState(self, state):
        """Description de la methode"""
		...
		return(false)

    def initialStates(self):
        """Description de la methode"""
		...
		return([])

		
    def isTerminalState(self, state):
        """Description de la methode"""
		...
		return(false)

    def terminalStates(self):
        """Description de la methode"""
		...
		return([])

		
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
		return (self.currentState, rewward)
		
		
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
		
		
		
