from environment import ENV
import os
import time
import matplotlib.pyplot as plt
debugLevel=0
graphLevel=1
lastActionLevel=0

class System:
    """System is the combination of an environment (ENV class) and an agent (General Agent Class)"""

    def __init__(self,laby,agent):
        """The system contains the environment and the agent"""
        self.laby=laby
        self.agent=agent


    def runEpisode(self, maxActionCount):

        """runs an episode of the agent searching for the arrival
        while showing the process step by step,
        returning the total reward of its steps"""

        totalReward=0;
        ActionCount=0
        state = self.laby.currentState()
        laby=self.laby
        WinningRewards=[]

        ########################################################################
        #Preparing data to be gathered
        if graphLevel>0:
            TotalRewardList=[]
        if lastActionLevel>0:
            last_action=maxActionCount
        ########################################################################

        while ((ActionCount<maxActionCount) and not(laby.isTerminalState(state))):
            laby=self.laby
            action=self.agent.nextAction(laby) # Already a General Agent Class method
            position_before_step=laby.current_position # This variable is needed because runStep changes the current position

            # Moving the agent and calculating the subsequent reward
            reward = laby.runStep(action)
            if reward==None: # runStep found no possible action, so the reward is None
                print("runEpisode is aware that runStep found no possible action")
                return totalReward
            totalReward+=reward

            ####################################################################
            #Gathering data
            if graphLevel>0:
                TotalRewardList.append(totalReward)
            ####################################################################

            self.laby.current_position=laby.current_position # Only change in laby from runStep()

            # Updating the policy of the agent after action is chosen and applied
            # Without General Agent Class :
            agent=self.agent
            agent.ChangeParameters(reward,laby,action,position_before_step)
            self.agent=agent

            # Updating criterias for the while() loop
            state = self.laby.currentState()
            ActionCount+=1
            if debugLevel>0:
                os.system('clear')
                print("Step:",ActionCount)
                laby.show()
                time.sleep(0.1)

        ########################################################################
        # Preparing plotting
        if graphLevel>0:
            ActionCountList=[i for i in range(ActionCount)]
        ########################################################################

        # If the agent arrived
        if (laby.isTerminalState(state)):
            if debugLevel>0:
                print("Victory!","Reward:",totalReward)
            if lastActionLevel>0:
                last_action=ActionCount
            WinningRewards+=[totalReward]

        ########################################################################
        # Plotting
        if graphLevel>0:
            plt.plot(ActionCountList,TotalRewardList)
            plt.xlabel("Number of iterations")
            plt.ylabel("Total reward")
            plt.show()
        ########################################################################

        # Returning total reward (sum of the reward of every step)
        if lastActionLevel>0:
            return last_action
        else:
            return totalReward
