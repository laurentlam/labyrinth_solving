import numpy
from environment import ENV
from environment import state

"""def QLearning(laby,width,length,Nb_episodes):
    Q = numpy.zero(WIDTH,LENGTH)
    for n in range(Nb_episodes):
        lambda = 1
        eps = 1
        init_state_list = laby.initialStates()
        state = init_state_list[0]
        for i in range
    """

#Architecture
    #Creating quality matrix (size of environment)
    #Algorithm : Refreshing quality matrix step by step

        #Finding agent position (s)
        #Begin loop (condition : not arrived OR nb_steps<nb_steps_max)

            #CHOSING NEXT ACTION (nextAction method) : random and chosen depending on epsilon factor

            #Random value as 0<value<epsilon : Chosing random action from s position to (unknown) s' position
            #Random value as 1>value>epsilon : Chsoing acute action from s position to s' position with best quality Q(s,s')

            #Q(s,a)=L*(r+G*max(Q(s',a')) + (1-G)*Q(s,a))

            #Changing agent position

        #End of loop (Matrix should be complete and steady)

    #End of Algorithm
