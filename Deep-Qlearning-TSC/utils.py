# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 21:55:20 2020

@author: XZ01M2
"""

import matplotlib.pyplot as plt
import numpy as np 

def _get_init_epoch( filename ):
    
    index = filename.find('_')
    str_epoch = filename[index+1]
    return int(str_epoch)

    
def plot_rewards(reward_store):
    
    x = np.mean(reward_store, axis = 0 )
    plt.plot( x , label = "Cummulative negative wait times") 
    plt.xlabel('Episodes') 
    plt.ylabel('Cummulative negative wait times') 
    plt.title('Cummulative negative wait times across episodes') 
    plt.legend() 
    plt.show() 
    
def plot_intersection_queue_size( intersection_queue_store):
    
    x = np.mean(intersection_queue_store, axis = 0 )
    plt.plot(x, label = "Cummulative intersection queue size ", color='m') 
    plt.xlabel('Episodes') 
    plt.ylabel('Cummulative intersection queue size') 
    plt.title('Cummulative intersection queue size across episodes') 
    plt.legend() 
    plt.show() 