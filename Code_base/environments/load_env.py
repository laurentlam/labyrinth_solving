__author__ = "Florence Carton"

import sys
from environments.Environment import Environment



def make_env(env_name, params):

	list_environments = {
	'Environment':Environment(params)
	}

	try:
		env = list_environments[env_name]
	except:
		print('env_name not found')
		sys.exit()

	return env
