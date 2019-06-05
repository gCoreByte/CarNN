import random
import copy

class AI:

    def __init__(self):
        self.previousScores = []
        self.previousActions = []
        self.currentActions = []
        self.followedActions = [] #which previous attempt
        self.currentScore = 0
    
    def newAction(self): 
        pickTurnout = random.randint(1,3) #tweakable
        if pickTurnout==1: 
            turnout = 0
        elif pickTurnout==2:
            turnout = 1
        else:
            turnout = None
        pickAcceleration = random.randint(1,8) #tweakable
        if pickAcceleration==1: 
            accel = -0.03
        elif pickAcceleration==2:
            accel = 0
        else:
            accel = 0.015
        return [turnout, accel]

    def newTurnAction(self, turn): #tweakable
        turnout = turn
        accel = 0.001
        return [turnout, accel]

    def pickActions(self): 
        maxIndex = self.previousScores.index(max(self.previousScores))
        previousBestActions = copy.deepcopy(self.previousActions[maxIndex])
        actionCount = len(previousBestActions)
        #try something different
        actionsToChange = random.randint(1,60) #tweakable
        if actionCount <= actionsToChange: 
            previousBestActions = []
        else: 
            previousBestActions = previousBestActions[:-actionsToChange]
        tryTurning = random.randint(1,5) #tweakable
        if tryTurning <= 2:
            for i in range (random.randint(5,80)): #tweakable
                previousBestActions.append(self.newTurnAction(0))
        elif tryTurning <= 4:
            for i in range (random.randint(5,80)): #tweakable
                previousBestActions.append(self.newTurnAction(1))
        return previousBestActions

    def act(self):
        if len(self.followedActions) > 0:
            action = self.followedActions.pop(0)
        else: 
            action = self.newAction()
        self.currentActions.append(action)
        return action

    #if crashed
    def newRun(self):
        self.previousActions.append(self.currentActions)
        self.previousScores.append(self.currentScore)
        self.followedActions = self.pickActions()
        self.currentActions = []
        self.currentScore = 0
