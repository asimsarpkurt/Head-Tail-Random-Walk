# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 18:49:24 2021

@author: Sarp
"""

#I conducted this case study thanks to DataCamp.
#The main aim was visualizing the probability distribution of getting a tail
#The coin will be tossed 1000 turns, each turn the coin will be tossed 10 times.
#In total the coin will be tossed 10,000 times. 
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
final_tails=[]
for x in range(1000):
    tails=[0]
    for x in range(10):
        coin=np.random.randint(0,2)
        tails.append(tails[x]+coin)
    final_tails.append(tails[-1])
    
plt.hist(final_tails, bins=10)

plt.show()
        
