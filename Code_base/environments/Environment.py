__author__ = "Florence Carton"
__credits__ = ["Florence Carton", "Freek Stulp", "Antonin Raffin"]

import random
import time

class Environment:

	UP = 0
	RIGHT = 1
	DOWN = 2
	LEFT = 3

	def __init__(self):

		self.num_states = int(params['num_cells'])

        # Check if there are enough cells
        assert self.num_states>1, "Number of cells must be 2 or larger"

        # Number of actions is 4 maximum (LEFT, RIGHT, UP, DOWN)
        self.num_actions = 4

        # Set to most right cell (will change in reset(...) anyway)
        self.current_state  =  0

        # end state
        self.terminal_state = 0 # arbitrary

        self.viewer = None

	def step(self, action):
		"""Project environment one step into the future.

         Given an action, compute the reward and next state, and whether next_state is terminal

         Args:
             action : The action the agent is performing

         Returns:
			next_state : an observation of the next state
			reward : the reward the agent receives for performing action in the current state
			is_done = if the next_state is a terminal state
        """

		raise NotImplementedError('subclasses must override step()!')

	def render(self):
		""" Display the environment
		"""

		raise NotImplementedError('subclasses must override render()!')


	def reset(self):
		"""Reset the environment.

         Args:


         Returns:
			first_state : the first state
        """
		raise NotImplementedError('subclasses must override render()!')


	def close(self):
		""" Close the environment
		"""
		raise NotImplementedError('subclasses must override close()!')
