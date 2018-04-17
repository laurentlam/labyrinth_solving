__author__ = "Florence Carton"


def default_params():
	""" Default parameters function

	Return :
		params_dict : dictionnary of parameters
	"""

	params_dict = {

	## Agent parameters
	'agent': 'AgentRandom',


	## Environment parameters"
	'env':'Environment',
	'num_cells': 100, 


	## Training parameters
	'num_training_episodes':1000,
	'max_action_per_episode':200

	}
	return params_dict


### unit test to check if param function is ok

if __name__ == '__main__':

    params = default_params()
    print('default_params = ',params)
    print('num_training_step = ', params['num_training_step'])

    params['new_param']='my_new_param' ## adding a new parameter
    print('params with new parameter',params)
