class labyrinthe:
    """Votre description"""

    def __init__(self,longueur,largeur):
        """Description de l'initialisation"""
        #DONE --> Added "states" attribut though

    def show(self):
        """Description de la methode d'affichage choisie"""
        #DONE
		...
		print("Mon labyrinthe de maniere ostensible mais simple")

    def states(self):
        """Description de la methode"""
        #NOT NEEDED ? --> states is now an attribut
		...
		return([])


    def isInitialState(self, state):
            """Description de la methode"""
            #DONE
    		...
    		return(false)

    def initialStates(self):
            """Description de la methode"""
            #DONE
    		...
    		return([])

    def isTerminalState(self, state):
        """Description de la methode"""
        #DONE
		...
		return(false)

    def terminalStates(self):
        """Description de la methode"""
        #DONE
		...
		return([])

	def currentState(self):
        """Description de la methode"""
        #TO DO --> need to have the position of the current state as an argument
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
		 reward=0
		...
		return (self.currentState, rewward)
