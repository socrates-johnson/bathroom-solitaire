#!/usr/bin/env python

##############################################################################
# bathroom_solitaire.py
#
# Bathroom solitaire simulation
# Game description: http://en.wikipedia.org/wiki/One-Handed_Solitaire
# Tom Pavlak
# 12/27/14
##############################################################################

from random import shuffle
import matplotlib.pyplot as plt

##############################################################################
# Function to shuffle deck
##############################################################################
def shuffle_deck(deck, n):
	for ii in range(6):
		shuffle(deck)

##############################################################################
# Function to draw card from back of deck
##############################################################################
def draw_card(deck_down, deck_up):
	deck_up.append(deck_down[0])
	deck_down.remove(deck_down[0])

##############################################################################
# Function to check top 4 cards
##############################################################################
def check_cards(deck_up):
	test_cards = deck_up[-4:]
	if test_cards[0][0] == test_cards[3][0]:
		deck_up.remove(test_cards[1])
		deck_up.remove(test_cards[2])
		return 1
	elif test_cards[0][1] == test_cards[3][1]:
		deck_up.remove(test_cards[0])
		deck_up.remove(test_cards[1])
		deck_up.remove(test_cards[2])
		deck_up.remove(test_cards[3])
		return 1
	else:
		return 0

##############################################################################
# Main program
##############################################################################
suits = ['hearts', 'diamonds', 'clubs', 'spades']
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck_0 = [[s, c] for s in suits for c in cards]

n = 7 # shuffle deck "n" times to randomize cards
n_trials = 1000000
num_left = []
n_winners = 0

for i in xrange(n_trials):
	deck_down = deck_0[:]
	shuffle_deck(deck_down, n)
	deck_up = []
	
	# Initial four card draw
	for ii in range(4):
		draw_card(deck_down, deck_up)
	
	while len(deck_down) > 0:
		check_flag = 1
		while check_flag == 1:
			if len(deck_up) > 3:
				check_flag = check_cards(deck_up)
			else:
				check_flag = 0
		
		if len(deck_down) > 0:
			draw_card(deck_down, deck_up)
		while len(deck_up) < 4 and len(deck_down) > 0:
			draw_card(deck_down, deck_up)
	
	if len(deck_up) > 3:
		check_flag = 1
		while check_flag == 1:
			if len(deck_up) > 3:
				check_flag = check_cards(deck_up)
			else:
				check_flag = 0
	
	num_left.append(len(deck_up))
	if len(deck_up) == 0:
		n_winners += 1

# Print results of simulation #		
print ''
print 'Run Completed!'
print '%i out of %i trials were winners (%.2f%%)' % (n_winners, n_trials, 
	float(n_winners)/n_trials * 100.)
print ''

# Plot histogram #
plt.hist(num_left, bins=26, normed=True)
plt.title("10,000,000 Games of Bathroom Solitaire")
plt.xlabel("Cards Remaining")
plt.ylabel("Frequency (%)")
plt.show()
