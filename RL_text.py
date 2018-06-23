# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 16:39:36 2018

@author: user
"""

import gym
from gym.envs.registration import register
#import sys,tty,termios


register(
        id='FrozenLake-v3',
        entry_point='gym.envs.toy_text:FrozenLakeEnv',
        kwargs={'map_name':'4x4','is_slippery':False}
        )

env=gym.make("FrozenLake-v3")
env.render()

#class _Getch:
#    def __call__(self):
#        fd=sys.stdin.fileno()
#        old_settings=termios.tcgetattr(fd)
#        try:
#            tty.setraw(sys.stdin.fileno())
#            ch=sys.stdin.read(3)
#        finally:
#            termios.tcsetattr(fd,termios.TCSADRAIN,old_settings)
#            
#        return ch

from msvcrt import getch
#inkey=msvcrt.getch()

LEFT=0
DOWN=1
RIGHT=2
UP=3

arrow_keys={72:UP,
                  80:DOWN,
                  77:RIGHT,
                  75:LEFT}
while True:
    key=getch()
    #print(ord(key))
    if ord(key)==224:
        key=ord(getch())
        #print(key)
    if key not in arrow_keys.keys():
        print("Game aborted!")
        break
    
    action=arrow_keys[key]
    state,reward,done,info=env.step(action)
    
    
    
    env.render()
    
    print("State ",state,"Action ",action, "Reward: ", reward, "Info: ",info)
    
    if done:
        print("Finished with reward",reward)
        break
    



