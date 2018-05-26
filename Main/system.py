from environment import ENV

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

        while ((ActionCount<maxActionCount) and not(laby.isTerminalState(state))):
            print("Step:",ActionCount)
            print(state)
            laby=self.laby
            next_action=self.agent.nextAction(laby)
            reward = laby.runStep(next_action)
            totalReward+=reward
            self.laby=laby

            self.agent.ChangeParameters(reward,laby,next_action)
            #With General Agent Class :
            #self.agent.updatePolicy(reward,next_action)

            state = self.laby.currentState()
            #Don't forget the laby is actualized by runStep method
            ActionCount+=1
            if (ActionCount%10 == 0):
                laby.show()
        if (laby.isTerminalState(state)):
            print("Victory!","Reward:",totalReward)
            WinningRewards+=[totalReward]
        return(totalReward)
