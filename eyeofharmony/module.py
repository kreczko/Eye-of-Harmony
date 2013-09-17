'''
Created on 17 Sep 2013

@author: phxlk
'''
from __future__ import absolute_import
from buildingblock import BuildingBlock

class Module(BuildingBlock):
    '''
    Module class
    '''
    building_blocks = []


    def __init__(self, name, ordered_list_of_building_blocks):
        '''
        Module class
        '''
        BuildingBlock.__init__(self, name)
        self.building_blocks = ordered_list_of_building_blocks
        