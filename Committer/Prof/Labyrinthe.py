import ...

class labyrinthe:
    """Votre description"""

    def __init__(self,longueur,largeur):
        """Description de l'initialisation"""
        #DONE --> Added "states" attribut

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
