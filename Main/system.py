from environment import ENV

class System:
    """System is the combination of an environment and an agent"""

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
            laby=self.laby
            agent=self.agent
            next_action=agent.nextAction(laby)
            totalReward+=laby.runStep(next_action)
            self.laby=laby
            #Don't forget the laby is actualized by runStep method
            #OR IS IT ? To verify because of self.laby class...
            ActionCount+=1
            laby.show()
        if (laby.isTerminalState(state)):
            print("Victory!","Reward:",totalReward)
            WinningRewards+=[totalReward]
        return(totalReward)
