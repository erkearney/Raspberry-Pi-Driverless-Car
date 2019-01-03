'''
keyboard_car.py
==============================================================================
This script will allow control of the RC car using the keyboard, use this for
testing and demonstration purposes.

This code was heavily inspiried by code written by Wang Zheng:
https://github.com/hamuchiwa/AutoRCCar/blob/master/test/rc_control_test.py
'''

# The pygame library is designed to be used to make games, but it gives us a
# convenient way to get keyboard input.
import pygame
from pygame.locals import *

class KeyboardCar(object):
    '''
    Use the pygame library to get keyboard input, and write out the inputted
    direction to the raspberry pi via serial output.
    '''
    def __init__(self):
        '''
        Create a pygame instance, along with a 250x250 window. There will be 
        nothing in this window, as we're not actually creating a game, but it
        still has to be there. 

        Attributes
        ----------
        loop : boolean
            Initalized to True, changed to False when the user presses the Esc
            key, ending a loop in the steer method.
        steer : method
            Handles keyboard input and serial output.
        '''
        pygame.init()
        #pygame.display.set_mode((250, 250))
        self.loop = True
        self.steer()

    def steer(self):
        ''' 
        Uses a loop to handle keyboard input and serial output.

        Attributes
        ----------
        loop : boolean
            Should have been initialized to True. The loop will continue until
            this boolean is set to False, which is done when the user presses
            the Esc key.
        '''
        while self.loop:
            # A keyboard press is an 'event' in pygame, the event.get method
            # gets the events from pygame's event queue:
            # https://www.pygame.org/docs/ref/event.html#pygame.event.get
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    key_input = pygame.key.get_pressed()

                    if key_input[pygame.K_UP]:
                        print("Forward")
                    elif key_input[pygame.K_RIGHT]:
                        print("Right")
                    elif key_input[pygame.K_LEFT]:
                        print("Left")
                    elif key_input[pygame.K_DOWN]:
                        print("Down")
                    elif key_input[pygame.K_ESCAPE]:
                        print("Exit")
                        self.loop = False
                        break

                elif event.type == KEYUP:
                    # Stop movement
                    pass

if __name__ == '__main__':
    KeyboardCar()
