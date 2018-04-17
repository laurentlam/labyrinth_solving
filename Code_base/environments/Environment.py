__author__ = "Florence Carton"
__credits__ = ["Florence Carton", "Freek Stulp", "Antonin Raffin"]

import random
import time
from math import sqrt

class State:

	def __init__(self,x,y,empty,reward):
		self.x = x
		self.y = y
		self.empty = empty
		self.reward = reward

class Environment:

	UP = 0
	RIGHT = 1
	DOWN = 2
	LEFT = 3

	def __init__(self,params):

		self.num_states = int(sqrt(params['num_cells']))

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
		# Decrease agent_cell by 1 if you go left, but only if you are not
        # in the left-most cell already and there is no wall ahead
        if action==Environment.UP:
            if (self.y<self.num_states-1)and(self.empty==True):
				self.y -= 1

        # Increase agent_cell by 1 if you go right, but only if you are not
        # in the right-most cell already
        if action==EnvironmentGrid1D.RIGHT:
            if (self.x<self.num_states-1)and(self.empty==True):
				self.x -= 1

        is_done = self.current_state == self.terminal_state

        if is_done:
            # If you are in the terminal state, you've found the exit: reward!
            reward = 100
        else:
            # Still wandering around: -1 penalty for each move
            reward = -1

        next_state = self.current_state

        return [next_state,reward,is_done]

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
