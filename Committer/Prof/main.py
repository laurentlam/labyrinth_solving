import ...

laby=Laby()
#print(laby.etats())
#print(laby.actions())
print("****************************************")
laby.show()
print("****************************************")

agent=AgentNaive()

systeme=System(laby, agent)

recompenses=systeme.runEpisode(42)
