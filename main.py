# Robert White
# ILLC @ UvA
# ai.robert.wangshuai@gmail.com

from agent import *
import random
import sys
from strategy import *


rounds = 5 # how many rounds of games do we iterate
# repeat = 10 # repeat ten times for each round and calculate the average payoff

ROCK = 0
PAPER = 1
SCISSORS = 2

class  Platform(object):
	
	def __init__(self, agents, domain):
		self.agents = agents
		self.domain = domain # for now, this is always 3, so hardcoded

	# the expected payoff for (pure strategy c1 against c2)
	def payoff (self, c1, c2): # zero sum game
		# rock = 0, paper = 1, scissors = 2
		# +-------------------------------------------+
		# |           | rock 0 | paper 1 | scissors 2 |  
		# | rock 0    |      0 |      -1 |          1 |
		# | paper 1   |     -1 |       0 |          1 |
		# | scissors 2|     -1 |       1 |          0 |
		# +-------------------------------------------+  

		matrix = [[0, -1, 1], [-1, 0, 1], [-1, 1, 0]]

		return matrix[c1][c2]


	# def play(self, rounds):
	# 	for i in range(rounds):
	# 		print ('this is the ', i, 'th round') # commend this out after debugging
	# 		strategies = []
	# 		# the first agent plays and the second agent reacts
	# 		c1 = self.agents[0].play()
	# 		c2 = self.agents[1].react(c1)
	# 		# zero sum game
	# 		pay1 = self.payoff(c1, c2)
	# 		pay2 = 0 - pay1
	# 		print ('\tthe payoff for agent 1 is ', pay1)
	# 		print ('\tthe payoff for agent 2 is ', pay2)

	def expectedPayoff (self, m ,n):
		# m and n can be pure or mixed strategies but here we use a uniform implementation
		# if m or n is pure strategy, then convert it to a mixed strategy and evaluate

		if type(m) == 'PureStrategy':
			m = m.convertToMixed()

		if type(n) == 'PureStrategy':
			n = n.convertToMixed()
		# for the first player (m): 
		em = 0 # expected payoff for m
		for i in range(len(m.values)):
			e = 0
			for j in range(len(n.values)):
				e += payoff(m.values[i], n.valuesp[j])* n.probabilities[j]
			em += e * m.probabilities[i]
		return em


		
def main():
	global rounds

	# to use, simply type 'python main.py x -n -r' for example
	# x is the size of domain
	# -n or -r is the agent you select
	# print ('this is a game of two players in the domain of size', sys.argv[1])
	# domain = range(int(sys.argv[1]))
	# print domain
	# print sys.argv[2], sys.argv[3]
	# agents = []
	# for i in [2,3]:
	# 	if sys.argv[i] == '-n': # an agent with naive strategy
	# 		agents.append(Agent('naive' + str(i), domain))
	# 		print ('the ', str(i-1) , 'th player uses a naive strategy')
	# 	if sys.argv[i] == '-r': # an agent with random strategy
	# 		agents.append(RandomAgent('random' + str(i), domain))
	# 		print ('the ', i-1 , 'th player uses a random strategy')

	# pl = Platform (agents, domain) # initialise the domain
	# pl.play(rounds)

	# initialise one agent that plays against computer
	r = PureStrategy(ROCK)
	p = PureStrategy(PAPER)
	s = PureStrategy(SCISSORS)
	a = Agent('bob', [r, p, s])

	a.printInfo()

if __name__ == "__main__":
	main()