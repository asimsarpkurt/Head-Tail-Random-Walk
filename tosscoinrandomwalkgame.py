# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 16:22:18 2021

@author: Asım Sarp Kurt
"""
#I conducted this case study thanks to DataCamp.
#Rules Of The Game
#Suppose we want to simulate a coin toss. First set the seed - again, this could be anything - and then use the randint() function.
#To have it randomly generate either 0 or 1, we pass two arguments: the first argument should be 0, the second one 2, because 2 is not going to be included. 
#If we print out coin, and then run the script, we get a random integer, 0. 
#You can now use this coin to play a game.
#Main objective is turning  head-tail coins toss into a Random Walk Game and visualizing it.
import numpy as np
    # Numpy is imported, seed is set
np.random.seed(3)	
# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)


    # append next_step to random_walk
    random_walk.append(step)
# Print random_walk
print(random_walk)
