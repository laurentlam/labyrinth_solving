import ...

class System:
    """System is the combination of an environment and an agent"""

    def __init__(self,laby, agent):
        """The system contains the environment and the agent"""
        self.laby=laby
        self.agent=agent


    def runEpisode(self, maxActionCount):
        """runs an episode of the agent searching for the arrival
        while showing the process step by step,
        returning the total reward of its steps"""

        totalReward=0;
        ActionCount=0
        while (ActionCount<maxActionCount) or (isTerminalState(self.laby.currentState())) :
            nextAction=self.agent.nextAction(self.laby)
            totalReward+=self.laby.runStep(nextAction)
            #Don't forget the laby is actualized by runStep method
            #OR IS IT ? To verify because of self.laby class...
            ActionCount+=1
		return(totalReward)
