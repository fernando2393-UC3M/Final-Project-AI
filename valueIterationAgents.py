# valueIterationAgents.py
# -----------------------
##
import mdp, util
import sys

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp = None, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbabilities(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        if (self.mdp != None):
            self.doValueIteration()

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """

        #"*** YOUR CODE STARTS HERE ***"

       #util.raiseNotDefined()

        #startstate=getStartState(self)
        n=0
        #anum=len(getPossibleActions(self, startstate))
        #qarray[anum]
	qvalue=0

        for sprime, probability in self.mdp.getTransitionStatesAndProbabilities(self, state, action): #It iteracts over the list of possible states and respective probabilities
		 discount=self.discount*self.values[sprime]
		 reward=self.mdp.getReward(self, state, action, sprime)
		 aux=discount+reward
		 aux=aux*probability
		 qvalue=qvalue+aux

        """
          This function is later used in doValueIteration and computeActionFromValues
          So we declare it beforehand
        """


        #"*** YOUR CODE FINISHES HERE ***"
        
        return qvalue
    

    def doValueIteration (self): #---------------PREGUNTAR SELF---------------#
        # Write value iteration code here

        print "Iterations: ", self.iterations
        print "Discount: ", self.discount
        states = self.mdp.getStates()
        maxDelta = float("-inf")


        #"*** YOUR CODE STARTS HERE ***"
        # Your code should include the implementation of value iteration
        # At the end it should show in the terminal the number of states considered in self.values and
        # the Delta between the last two iterations

	for n in range (0, self.iterations):
		for statecount in self.mdp.getStates():
			if self.mdp.isTerminal(statecount):
				auxArray[statecount]=0
			else:
				auxArray=computeActionFromValues(self, statecount)
		
		self.values=auxArray		#-----------Ask what this item should return-----------#

        

        util.raiseNotDefined()
        #"*** YOUR CODE FINISHES HERE ***"
        
    def setMdp( self, mdp):
        """
          Set an mdp.
        """
        self.mdp = mdp
        self.doValueIteration()

    def setDiscount( self, discount):
        """
          Set a discount
        """
        self.discount = discount

    def setIterations( self, iterations):
        """
          Set a number of iterations
        """
        self.iterations = iterations
       
       
    def getValue(self, state):
        """
          Return the value of the state
        """
        return self.values[state]
        


    def showPolicy( self ):

        """
          Print the policy
        """
        
        states = self.mdp.getStates()
        for state in states:
            print "Policy\n", state, self.getPolicy(state)


    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """

        #"*** YOUR CODE STARTS HERE ***"

        #util.raiseNotDefined()

	if self.mdp.isTerminal(state)==NULL:
		return None #As specified in the statement

	maximum=0
	bestaction=0
	
	for n in self.mdp.getPossibleActions(state): #n is the current action in the iteration
		value=self.computeQValueFromValues(self, state, action)
		if value>=maximum:
			maximum=value
			bestaction=n

	return bestaction

        #"*** YOUR CODE FINISHES HERE ***"

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getPolicy(self, state):
        "Returns the policy at the state (no exploration)."
        return self.getAction(state)

    
    def getQValue(self, state, action):
        "Returns the Q value."        
        return self.computeQValueFromValues(state, action)

    def getPartialPolicy(self, stateL):
        "Returns the partial policy at the state. Random for unkown states"        
        state,state_names = self.mdp.stateToHigh(stateL)
        if self.mdp.isKnownState(state):
            return self.computeActionFromValues(state)
        else:
            # random action
            return util.random.choice(stateL.getLegalActions()) 



